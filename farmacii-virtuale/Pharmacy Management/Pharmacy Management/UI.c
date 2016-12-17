#include <stdio.h>
#include "UI.h"

UI createUI(MedicineController *medCtrl) {
	UI ui;
	ui.controller = medCtrl;
	return ui;
}

void printMenu() {
	printf("1 - ADD a medication\n");
	printf("2 - UPDATE a medication\n");
	printf("3 - REMOVE a medication\n\n");

	printf("4 - SEARCH for a medication\n");
	printf("5 - SHOW ALL\n\n");
	printf("0 - EXIT\n");
}

/*
Verifies if a command is valid
Input: cmd - integer
Output: 1, if command is valid
		0, otherwise
*/
int validCommand(int cmd) {
	if (cmd >= 0 && cmd <= 3) {
		return 1;
	}
	return 0;
}

/*
Reads an integer number from the keyboard. Asks for number while read errors encoutered.
Input: the message to be displayed when asking the user for input.
Returns the number.
*/
int readIntegerNumber(const char* message)
{
	char s[16];
	int res = 0;
	int flag = 0;
	int r = 0;

	while (flag == 0)
	{
		printf(message);
		scanf("%s", s);

		r = sscanf(s, "%d", &res);	// reads data from s and stores them as integer, if possible; returns 1 if successful
		flag = (r == 1);
		if (flag == 0)
			printf("Error reading number!\n");
	}
	return res;
}

int addMedicineUI(UI *ui) {
	char name[40], concentration[10];
	int quantity, price;
	printf("    name: ");
	scanf("%19s", name);
	printf("    concentration: ");
	scanf("%9s", concentration);
	quantity = readIntegerNumber("    quantity: ");
	price = readIntegerNumber("    price: ");
	return addMedicine(ui->controller, name, concentration, quantity, price); //return 1;
}

int removeMedicineUI(UI *ui) {
	char name[40], concentration[10];
	printf("    name: ");
	scanf("%19s", name);
	printf("    concentration: ");
	scanf("%9s", concentration);
	return removeMedicine(ui->controller, name, concentration);
}

int updateMedicineUI(UI *ui) {
	char name[40], concentration[10];
	int quantity, price;
	printf("    name: ");
	scanf("%19s", name);
	printf("    concentration: ");
	scanf("%9s", concentration);
	quantity = readIntegerNumber("    new quantity: ");
	price = readIntegerNumber("    new price: ");
	return updateMedicine(ui->controller, name, concentration, quantity, price);
}

void printRepo(MedicineRepository *repo) {
	/*printf("   %30s|%8s|%11s\n", "Name", "Quantity", "Price (RON)");
	printf("---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---\n");
	for (int i = 0; i < getLength(repo); ++i) {
		printf("%-2d. %20s %10s|%8d|%11d\n", i, getName(&(repo->data[i])), getConcentratio(&(repo->data[i])), getQuantity(&(repo->data[i])), getPrice(&(repo->data[i])));
	}*/
	for (int i = 0; i < getLength(repo); ++i) {
		char s[256];
		toString(&repo->data[i], s);
		printf("%2d. %s\n", i+1, s);
	}
	if (getLength(repo) == 0) {
		printf("Nothing here...\n");
	}
}

void searchUI(UI *ui) {
	char name[20];
	printf("    search for: ");
	scanf("%20s", &name);
	MedicineRepository toPrint = search(ui->controller, name);
	printRepo(&toPrint);
}

void printAll(UI *ui) {
	MedicineRepository toPrint = search(ui->controller, "");
	printRepo(&toPrint);
}

void startUI(UI *ui) {
	while (1) {
		printMenu();
		int cmd = readIntegerNumber("Enter command: ");
		if (cmd == 0) {
			break;
		}
		switch(cmd) {
			case 1: {
				if (addMedicineUI(ui)) {
					printf("Medicine successfully added.\n");
				}
				else {
					printf("Error! Medicine not added.\n");
				}
				break;
			}
			case 2: {
				if (updateMedicineUI(ui)) {
					printf("Medicine successfully updated.\n");
				}
				else {
					printf("Error! Medicine not updated.\n");
				}
			}
			case 3: {
				if (removeMedicineUI(ui)) {
					printf("Medicine successfully removed.\n");
				}
				else {
					printf("Error! Medicine not found.\n");
				}
				break;
			}
			case 4: {
				searchUI(ui);
				break;
			}
			case 5: {
				printAll(ui);
				break;
			}
			default:
				printf("Wrong command!\n");
				break;
		}
	}
	printf("Bye!\n");
}