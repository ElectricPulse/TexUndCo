.globl _start
.extern printf
.section .text

_start:
	mov x8, #64
	mov x0, #1
	mov x1, #4
	mov x2, 13
	svc #0

	# exit
	mov x8, #93
	mov x0, #0
	svc #0

	ret

.section .rodata
result_msg:
	.asciz "Result: "
newline:
	.asciz "\n"
