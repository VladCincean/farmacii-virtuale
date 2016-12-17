;13. A character string S is given. Obtain the string D which contains all the digit characters of S.
;Exemple:
;S: '+', '4', '2', 'a', '8', '4', 'X', '5'
;D: '4', '2', '8', '4', '5'

ASSUME cs:code, ds: data
data SEGMENT
	S DB '+', '4', '2', 'a', '8', '4', 'X', '5'
	len EQU $-S
	D DB len DUP(?)
	;we allocate space for the 'D' string, whose maximum length is egual to the length of the initial string ('S')
data ENDS

code SEGMENT
start:
	mov ax, data
	mov DS, ax
	mov cx, len ;we initialise CX with the length of the string 'S'
	mov SI, 0 ;we use SI as index for the string 'S'
	mov DI, 0 ;we use DI as index for the string 'D'
	
	jcxz Sfarsit ;we will use the loop instruction CX=len times
	Repeta:
		mov al, S[SI]
		inc SI ;we increment the index of the string 'S' for the next instruction
		cmp al, '0'
		jb NuAdauga ;if AL<'0' we do not copy the element to the destination string
		cmp al, '9'
		ja NuAdauga ;if AL>'9' we do not copy the element to the destination string
		;else, we add the element S[SI-1] to D[DI]
		mov D[DI], al
		inc DI
		NuAdauga:
	loop Repeta
	Sfarsit: ; we end the program
	
	mov ax, 4C00h
	int 21h
code ENDS
END start