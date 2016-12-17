;14. Read a word and the name of a file from the keyboard. Print a suitable
;message on the screen if the word exists or does not exist in the given file.

assume CS:code, DS:data
data segment
	msg_word db 'Cuvantal: $'
	maxWordLenght db 30
	lenWord db ?
	cuvant db 30 dup (?)

	msg_file db 'Numele fisierului: $'
	maxFileName db 20
	lFileName db ?
	fileName db 20 dup (?)
	
	buffer db 100 dup (?), '$'
	
	ans1 db 'Cuvantul exista in fisier.$'
	ans2 db 'Cuvantul NU exista in fisier.$'
	
	openErrorMsg db 'Fisierul nu exista.$'
	readErrorMsg db 'Nu se poate citi din fisier.$'
	
	gasit db 0
data ends
code segment
start:
	mov ax, data
	mov ds, ax
	
	citire_cuvant:
		; afisam mesajul care solicita cuvantul
		mov ah, 09h
		mov dx, offset msg_word
		int 21h
	
		; citim de la tastatura numele fisierului
		mov ah, 0ah
		mov dx, offset maxWordLength
		int 21h
		; in urma citirii de la adresa maxWordLength + 2 = cuvant se memoreaza numele fisierului citit
		; la adresa maxWordLength + 1 = lenWord se memoreaza dimensiunea sirului de caractere care reprezinta cuvantul
	
		; transformam cuvantul intr-un sir ASCIIZ (sir ce se termina cu byte-ul zero)
		mov al, lenWord
		xor ah, ah
		mov si, ax
		mov fileName[si], 0
	
	citire_fisier:
		; afisam mesajul care solicita numele fisierului
		mov ah, 09h
		mov dx, offset msg_file
		int 21h

		; citim de la tastatura numele fisierului cu ajutorul functiei 0ah, int 21h
		mov ah, 0ah
		mov dx, offset maxFileName
		int 21h
		; in urma citirii la adresa maxFileName + 2 = fileName se memoreaza numele fisierului citit
		; la adresa maxFileName + 1 = lFileName se memoreaza dimensiunea sirului de caractere care reprezinta numele fisierului
 
		; transformam numele fisierului intr-un sir ASCIIZ (sir ce se termina cu byte-ul zero)
		mov al, lFileName
		xor ah, ah
		mov si, ax
		mov fileName[si], 0

	deschideFisier:
		; deschidem fisierul cu functia 3dh, int 21h
		mov ah, 3dh
		mov al, 0 ; deschidem fisierul pentru citire
		mov dx, offset fileName
		int 21h
	
		jc openError ; eroare la deschiderea fisierului daca CF e setat
		mov bx, ax ; salvam identificatorul fisierului in registrul bx
	
	citeste_din_fisier:
		mov ah, 3fh
		mov dx, offset buffer
		mov cx, 100 ; citim maxim 100 caractere
		int 21h
		
		jc readError ; daca va avea loc o eroare, se seteaza CF=1
		
		mov si, 0
		mov bx, 0
		
		mov cx, 100
		repeta:
			xor ah, ah
			mov al, buffer[si]
			cmp al, cuvant[bx]
			JNE de_la_inceput ; daca gasim o nepotrivire, reluam cautarea (BX:=0)
			add bx, 1
			mov al, lenWord
			mov ah, 0
			cmp bx, ax
			JNE mai_departe
			mov gasit, 1 ; daca bx = ax (= lungima cuvant), inseamna ca am gasit cuvantul
		
			de_la_inceput:
				mov bx, 0
			mai_departe:
				inc si
		LOOP repeta
	
	check:
		cmp gasit, 1
		je exista
		jmp nu_exista
	
	exista:
		; afisam mesajul de confirmare
		mov ah, 09h
		mov dx, offset ans1
		int 21h
		jmp endPrg
		
	nu_exista:
		; afisam mesajul de infirmare
		mov ah, 09h
		mov dx, offset ans2
		int 21h
		jmp endPrg

	openError:
		mov ah, 09h
		mov dx, offset openErrorMsg
		int 21h
		jmp endPrg 

	readError:
		mov ah, 09h
		mov dx, offset readErrorMsg
		int 21h 
		jmp endPrg

	endPrg:
		mov ax,4c00h
		int 21h
code ends
end start