assume cs:code, ds:data, es:data
data segment public
	lS1 db 3
	lS2 db 6
	S1 db '000$'
	S2 db '892052$'
	check db 0
data ends

code segment public
public compara
compara:
;input: SI - offset of the source string (sirul de comparat)
;		DI - offset of the destination string (sirul cu care se compara)
;		CL - no of bytes to compare (lenght of string 1)
;		CH - (lenght of string 2)
;			precondition: CL<CH
;output: AL = 0, if S2 is a subsequence of S1
;		 AL = 1, otherwise
start:
	mov ax, data
	mov ds, ax
	mov es, ax
	
	lea si, S1
	lea di, S2
	mov cl, lS1
	mov ch, lS2
	
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
	JMP-nu_bine
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
		
		mov ax, 4c00h
		int 21h
	
code ends
end start