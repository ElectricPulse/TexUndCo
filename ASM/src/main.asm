.globl _start
.section .text

_start:
	## file descriptor
	mov x0, #1

	adrp x1, message
	add x1, x1, :lo12:message

	# write
	## message length
	mov x2, 13
	mov x8, #64
	svc #0

	# exit
	mov x8, #93
	mov x0, #42
	svc #0

	ret

.section .rodata
message:
	.asciz "Hello world!\n"
