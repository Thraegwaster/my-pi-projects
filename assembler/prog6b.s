@ 64-bit addition

/* Add two 64-bit numbers together */

	.global _start
_start:
	MOV R2, #0xFFFFFFFF @ low half of first number
	MOV R3, #0x1 @ high half of first number
	MOV R4, #0xFFFFFFFF @ low half of 2nd number
	MOV R5, #0xFF @ high half of 2nd number
	ADDS R0,R2,R4 @ add low halves, set flags
	ADCS R1,R3,R5 @ add high halves with carry
	MOV R7, #1 @ exit through syscall
	SWI 0
