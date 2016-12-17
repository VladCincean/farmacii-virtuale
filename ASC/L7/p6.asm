;6. Being given a string of words, obtain the string (of bytes) of the digits in base 10 of each word from this string.
;Ex.: being given the string: sir DW 12345, 20778, 4596 
;the result will be 1, 2, 3, 4, 5, 2, 0, 7, 7, 8, 4, 5, 9, 6.
;12345/10 = 1234 rest 5

ASSUME cs:code, ds:data
data SEGMENT
	sir DW 12345, 20778, 4596
	len EQU ($-sir)/2 ; the length of the string (in words)
	; the maximum decimal number stored in one word is 65535 (5 digits)
	; so, we need 5 times the length of the string of words in order to store all its words' decimal digits
	dest DB 5*len DUP(?) ; 3*len is the maximum length of the string (of bytes) of the digits
	zece DW 10 ; used in order to divide a doubleword by 10
data ENDS

code SEGMENT
start:
	mov ax, data
	mov ds, ax
	
	mov si, offset sir + 2*len - 2 ; in ds:si store the FAR address of the string 'sir'
	mov ax, seg sir
	mov ds, ax
	mov di, offset dest + 5*len - 1 ; in es:di store the FAR address of the string 'dest'
	mov ax, seg dest
	mov es, ax

	STD ; DF = 1; parse the string frrom right to left
	mov cx, len ; parse the elements of the string in a loop with len iterations.
	repeta:
		LODSW ; the word from adr <DS:SI> is loaded in AX; SI:=SI-2
		getDigit:
			CWD ; the number will be stored in DX:AX
			div zece ; AX:= DX:AX mod 10 (the last decimal digit); DX:= DX:AX / 10
			xchg ax, dx ; exchange AX with DX ; now, AX contains the digit (it is a digit -> it is stored only in AL, and AH is 0)
			add ax, '0' ; ** the digit is converted to its ASCII code
			STOSB ; the byte AL (the digit) is stored into the byte from address <ES:DI>; DI:=DI-1
			xchg ax, dx ; exchange AX with DX ; now, AX contains the quotient (the number) and DX the remainder (the digit)
			cmp ax, 0 ; check if the number is not zero (if there exists more digits)
			jne getDigit; if so, get another digit
		loop repeta ; if there are more numbers/words in the string 'sir', we compute another one
	
	mov ax, 4C00h
	int 21h
code ENDS

END start