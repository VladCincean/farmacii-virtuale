; 13. Four bytes are given. Obtain in AX the sum of the integer numbers represented on the bits 4-6 of the four bytes.

ASSUME cs:code, ds:data
data SEGMENT
	b1 db 11001100b
	b2 db 01010101b
	b3 db 00100100b
	b4 db 11100011b
data ENDS
code SEGMENT
start:
	mov ax, data
	mov ds, ax
	
	mov ax, 0 ; AX:=0 (the final result will be stored in AX)
	
	mov bl, b1 ; BL:=b1 ; BL = a7 a6 a5 a4 a3 a2 a1 a0
	shl bl, 1 ; BL = a6 a5 a4 a3 a2 a1 a0 0
	mov cl, 5
	shr bl, cl ; BL = 0 0 0 0 0 a6 a5 a4
	mov bh, 0 ; BX = 0 ... 0 a6 a5 a4 (BL: 0000 0100 = 4h)
	add ax, bx ; AX = 0h + 4h = 4h
	
	mov bl, b2 ; BL:=b1 ; BL = a7 a6 a5 a4 a3 a2 a1 a0
	shl bl, 1 ; BL = a6 a5 a4 a3 a2 a1 a0 0
	mov cl, 5
	shr bl, cl ; BL = 0 0 0 0 0 a6 a5 a4
	mov bh, 0 ; BX = 0 ... 0 a6 a5 a4 (BL: 0000 0101 = 5h)
	add ax, bx ; AX = 4h + 5h = 9h

	mov bl, b3 ; BL:=b1 ; BL = a7 a6 a5 a4 a3 a2 a1 a0
	shl bl, 1 ; BL = a6 a5 a4 a3 a2 a1 a0 0
	mov cl, 5
	shr bl, cl ; BL = 0 0 0 0 0 a6 a5 a4
	mov bh, 0 ; BX = 0 ... 0 a6 a5 a4 (BL: 0000 0010 = 2h)
	add ax, bx ; AX =  9h + 2h = Bh
	
	mov bl, b4 ; BL:=b1 ; BL = a7 a6 a5 a4 a3 a2 a1 a0
	shl bl, 1 ; BL = a6 a5 a4 a3 a2 a1 a0 0
	mov cl, 5
	shr bl, cl ; BL = 0 0 0 0 0 a6 a5 a4
	mov bh, 0 ; BX = 0 ... 0 a6 a5 a4 (BL: 0000 0110 = 6h)
	add ax, bx ; AX = Bh + 6h = 11h
	

	mov ax, 4C00h
	int 21h
	
code ENDS
END start