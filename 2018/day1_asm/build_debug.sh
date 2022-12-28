nasm -f elf64 -g -F dwarf -l main.lst main.s && ld -m elf_x86_64 -o debug main.o
