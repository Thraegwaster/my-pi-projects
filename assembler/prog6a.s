@ Simple 32-bit addition

/* Perform R0=R1+R2 */

	.global _start
_start:
	MOV R1, #50 @ Get 50 into R1
	MOV R2, #60 @ Get 60 into R2
	ADDS R0,R1,R2 @ R0=R1+R2
	MOV R7, #1 @ exit through syscall
	SWI 0
