/*
For each command line argument launch two subprocesses that will race to establish:
- the length of the longest line, if the argument is a file (using popen and wc).
- the size in bytes if the argument is a directory (using popen and du).
Each process, before send the result to the parent, will sleep between one and five seconds (using sleep call).
The communication between processes we will use a single pipe channel.
Each process will send to the parent a structure that contains his pid, the argument and the established result.
The parent will print only the n/2 received results (n being the number of arguments), the rest will be ignored.
*/

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/wait.h>

typedef struct{
    int myPid;
    int arg;
    int result;
} Result;

int main(int argc, char* argv[]){
    int p1, p2, fd[2], i;
    FILE* f;
    if (pipe(fd) == -1) {
        perror("Error. Can't create pipe.\n");
        exit(EXIT_FAILURE);
    }
    p1 = fork();
    if (p1 > 0) {
        p2 = fork();
    }
    if (p1 == 0 || p2 == 0){
        Result r;
        struct stat sb;
        int secondsToSleep;
        close(fd[0]);
        r.myPid = getpid();
        for (i = 1; i < argc; i++) {
            char cmd[100], rez[100];
            r.arg = i;
            if (stat(argv[i], &sb) == -1) {
                perror("Error at stat functions.\n");
                exit(EXIT_FAILURE);
            }
            if ((sb.st_mode & S_IFMT) == S_IFREG) {
                strcpy(cmd, "cat ");
                strcat(cmd, argv[i]);
                strcat(cmd, " | wc --max-line-length\0");
                f = popen(cmd, "r");
            }
            else if ((sb.st_mode & S_IFMT) == S_IFDIR) {
                strcpy(cmd, "du -b ");
                strcat(cmd, argv[i]);
                strcat(cmd, " | cut -f1\0");
                f = popen(cmd, "r");
            }
            if (fgets(rez, sizeof(rez), f) != NULL) {
                r.result = atoi(rez);
            }
            else {
                r.result = 0;
            }
            pclose(f);
            srand(time(0));
            secondsToSleep = rand() % 4 + 1;
            sleep(secondsToSleep);
            write(fd[1], &r, sizeof(Result));
        }
        close(fd[1]);
        exit(0);
    }
    close(fd[1]);
    for (i = 1; i <= (argc - 1)/2;) {
        Result r;
        read(fd[0], &r, sizeof(Result));
        if (r.arg == i) {
            printf("%d. pid = %d, result = %d for the argument %s\n",
                i, r.myPid, r.result, argv[i]);
            i++;
        }
    }
    close(fd[0]);
    printf("Parent: I am waiting for a child\n");
    wait(0);
    printf("Parent: I am waiting for the other child\n");
    wait(0);
    printf("Parent: done\n");
    return 0;
}

