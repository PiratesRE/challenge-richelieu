; nasm -f elf64 jmp_rsp.asm -o jmp_rsp.o
; objdump -d jmp_rsp.o
global _start
  _start:
  jmp rsp
