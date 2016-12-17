; (8-a*b*100+c)/d
; a,b,d-byte; c-doubleword
; unsigned interpretation

ASSUME cs: code, ds: data
data SEGMENT
	a db 2
	b db 3
	d db 10
	c dd 800
data ENDS
code SEGMENT
start:
	mov ax, data
	mov ds, ax
	
	mov al, a ; al:=a=2=2h
	mul b ; ax:=al*b=2*3=6=6h
	
	mov bx, 100 ; bx:=100=64h
	mul bx ; dx:ax := ax*bx=6*100=600=258h
	
	mov bx, word ptr c
	mov cx, word ptr c+2
	; cx:bx := c = 800 = 320h
	
	; cx:bx := cx:bx - dx:ax = 800 - 600 = 200 = C8h
	sub bx, ax
	sbb cx, dx
	
	; dx:ax := cx:bx = 200 = C8h
	mov ax, bx
	mov dx, cx

	; dx:ax := dx:ax + 8 = 200 + 8 = 208 = D0h	
	add ax, 8
	adc dx, 0
	
	mov bl, d ; bl:=d=10=Ah
	mov bh, 0 ; bx:=bl=10=Ah
	div bx
	; ax := dx:ax div bx = 208 div 10 = 20 = 14h
	; dx := dx:ax mod bx = 208 mod 10 = 8 = 8h
	; Valoarea expresiei este: AX rest DX
	; In cazul nostru 20 rest 8 (14h rest 8h)
	
	mov ax, 4C00h
	int 21h
	
code ENDS
END start