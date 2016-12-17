; (8-a*b*100+c)/d
; a,b,d-byte; c-doubleword
; signed interpretation

ASSUME cs: code, ds: data
data SEGMENT
	a db -2
	b db 3
	d db 16
	c dd 200
data ENDS
code SEGMENT
start:
	mov ax, data
	mov ds, ax
	
	mov al, a ; al:=a=-2 -> al=FEh
	neg al ; al:=-al=2 -> al=02h
	mov bl, b ; bl:=b=3 -> bl=03h
	imul bl ; ax:=al*bl=2*3=6 -> ax=0006h
	mov bx, 100 ; bx:=100 -> bx=0064h
	imul bx ; dx:ax := ax*bx=6*100=600 = 0000 0010 0101 0000
	; -> ax=0258h, dx=0000h
	
	; dx:ax := dx:ax + 8 = 600 + 8 = 608 -> ax=0260h, dx=0000h
	add ax, 8
	adc dx, 0
	
	; cx:bx := c = 200 -> bx=00C8h, cx=0000h
	mov bx, word ptr c
	mov cx, word ptr c+2
	
	; cx:bx := cx:bx + dx:ax = 200 + 608 = 808 = 0000 0011 0010 1000
	; -> bx=0328h, cx=0000h
	add bx, ax
	adc cx, dx
	
	mov al, d ; al:=d=16 -> al=10h
	cbw ; ax:=al -> ax=0010h
	
	mov dx, ax ; dx:=ax=16 -> dx=0010h
	mov ax, bx ; ax:=bx -> ax=0328h
	mov bx, dx ; bx:=dx=16 -> bx=0010h
	mov dx, cx ; dx:=cx -> cx=0000h
	;in urma acestor operatii dx:ax= 608 si bx=16
	; ax=0328h, dx=0000h, bx=0010h
	
	; ax := dx:ax div bx = 808 div 16 = 50 -> ax=0032h
	; dx := dx:ax mod bx = 808 mod 16 = 8 -> dx=0008h
	idiv bx
	
	; valoarea expresiei este ax mod dx
	; in cazul nostru 50 mod 8 (32h mod 8h)
	
	mov ax, 4C00h
	int 21h
	
code ENDS
END start