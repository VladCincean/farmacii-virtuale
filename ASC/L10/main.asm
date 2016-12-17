;11. Se citesc mai multe siruri de caractere. Sa se determine daca primul apare ca subsecventa in fiecare din celelalte si sa se dea un mesaj corespunzator.

assume cs:code, ds:data, es:data

data segment public
	max_lenS1 db 250
	lenS1 db ?
	S1 db 250 dup (?)
	max_lenS2 db 250
	lenS2 db ?
	S2 db 250 dup (?)
	m1 db 'Introduceti sirul 1: $'
	m2 db 'Introduceti un sir SAU tasta ENTER pentru a termina: $'
	m3 db 'Primul sir apare ca subsecventa in fiecare din celelalte.$'
	m4 db 'Exista un sir in care primul sir NU apare ca subsecventa.$'
	e1 db 'Eroare! Ati introdus un sir mai scurt decat primul sir. Programul s-a incheiat.$'
data ends

code segment public

extrn compara:proc

print PROC
;input: DS:DX - pointer to character string to print on the screen
;			remark: the string must be terminated with a '$' (dollar-sign)
	mov ah, 09h
	int 21h
	RET
print ENDP

read PROC
;input: DS:DX - pointer to an input buffer
;			remark: offset 0 (first byte) specifies the maximum buffer length
;output: at offset 1 - the no of bytes read
	mov ah, 0ah
	int 21h
	RET
read ENDP

start:
	mov ax, data
	mov ds, ax
	mov es, ax
	
	;"Introduceti sirul 1:"
	lea dx, m1
	CALL print
	
	;citim sirul 1
	LEA dx, max_lenS1
	CALL read
	
	mov al, lenS1
	xor ah, ah
	mov si, ax
	mov S1[si], 0
	
	mov cx, 256
	repeta:
		;"Introduceti sirul 2:"
		lea dx, m2
		call print
	
		;citim sirul 2
		lea dx, max_lenS2
		CALL read
		
		mov al, lenS2
		cmp al, 0 ;verificamm daca am citit ceva
		JE iesire ;daca nu am citit un alt sir, iesim din bucla 'repeta'
		xor ah, ah
		mov si, ax
		mov S2[si], 0
		
		lea si, S1
		lea di, S2
		push cx
		mov cl, lenS1
		mov ch, lenS2
		cmp cl, ch
		JA er
		;comparam sirul 1 cu sirul 2
		CALL compara
		
		CMP AL, 0 ; daca exista subsecventa
		je ok
		CMP AL, 1 ; daca NU exista subsecventa
		je nu_exista
		CMP AL, 2 ; daca len(S1)<len(S2)
		
		ok:
			pop cx
	LOOP repeta
	iesire:
	
	;exista
	lea dx, m3
	call print
	jmp finish
	
	er:
		lea dx, e1
		call print
		jmp finish
	
	nu_exista:
		lea dx, m4
		call print
		
	finish:
		mov ax, 4c00h
		int 21h
code ends
end start