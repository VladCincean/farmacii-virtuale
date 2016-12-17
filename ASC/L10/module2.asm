assume cs:code, ds:data, es:data
data segment public
	lS1 db ?
	lS2 db ?
	check db 0
data ends

code segment public
public compara
compara:
;input: SI - offset of the source string (sirul de comparat)
;		DI - offset of the destination string (sirul cu care se compara)
;		CL - no of bytes to compare (length of string 1)
;		CH - (length of string 2)
;			precondition: CL<CH
;output: AL = 0, if S2 is a subsequence of S1
;		 AL = 1, otherwise
	mov check, 0
	push si ;salvam offsetul inceputului lui S1
	cld
	mov lS1, cl ;salvam lungimea sirului S1
	mov lS2, ch ;salvam lungimea sirului S2
	xchg cl, ch
	mov ch, 0 ; now, CX = lenS2
	L:
		CMPSB
		JZ sari
		;daca gasim o neconcordanta
		mov check, 0
		pop si ;daca gasim o neconcordanta, in sirul 1 revenim la primul byte
		push si ;salvam offsetul inceputului lui S1
	LOOP L
	JMP nu_bine ;daca am iesit din bucla pe aici, inseamna ca S1 nu e subsecventa pentru S2
		sari:
			mov bl, check
			add bl, 1
			mov check, bl
			cmp bl, lS1
			JE bine
		LOOP L
	
	nu_bine:
		mov AL, 1
		jmp return
	
	bine: ; daca exista subsecventa
		mov AL, 0
		
	return:
		pop si
		RET
	
code ends
end