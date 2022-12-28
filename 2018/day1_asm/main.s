%define char_r      r11
%define char_e      r11d
%define char_b      r11b
%define sum         r12d ;the register we are using for the running total
                        ;12 because december is 12th month
%define temp_int    r13 ;register for converting string to number
%define etemp_int   r13d ;register for converting string to number
%define buf_i       r14 ;register for buffer index
%define buf_len     r15 ;register for data length in buffer


%macro clear 1
    xor %1, %1 ;hey im lazy ok
%endmacro


section .data
    buf times 1024 db 0x00   ;1kb buffer for stdin
    buflen equ $ - buf

    unrec_msg db "Unrecognized start to token.\n"
    unrec_msg_len equ $ - unrec_msg

    notnum_msg db "Encountered something that wasn't a number :\\\n"
    notnum_msg_len equ $ - notnum_msg


section	.text
   global _start     ;must be declared for linker (ld)
	

_start:
    clear sum
    clear temp_int
    clear buf_i
    clear buf_len

add_next_number:
    call get_int
    add sum, eax
    cmp buf_len, 0
    jne add_next_number

    call finish


read_input_chunk:
    mov rax, 0      ;syscall read
    mov rdi, 0      ;stdin file descripor
    mov rsi, buf    ;buf to read into
    mov rdx, buflen ;how much to read
    syscall
    ret

    
get_char:
    inc buf_i
    cmp buf_i, buf_len
    jl return_char
refill:
    call read_input_chunk   ;get new chunk
    mov buf_len, rax        ;move the read length to buf_len
    clear buf_i             ;set buf_i to 0
return_char:
    clear char_r
    mov char_b, byte [buf + buf_i]
    ret


get_int:
    clear temp_int

    call get_char
    cmp buf_len, 0
    je finish

    cmp char_b, 0x2B ;hex for +
    je positive
    cmp char_b, 0x2D ;hex for -
    je negative
    jmp unrecognized_start
negative:
    mov r10d, -1
    jmp get_digit
positive:
    mov r10d, 1
get_digit:
    call get_char

    cmp buf_len, 0  ;if we've reached EOF
    je return_int   ;return what we have

    cmp char_b, 0x0a ;if we've reached end of line
    je return_int           ;return what we have

    cmp char_b, 0x30 ;if we're expecting a number, but the byte is before '0'
    jl not_a_number         ;its not a number

    cmp char_b, 0x39 ;same if it's above '9'
    jg not_a_number         ;@notanumber

    sub char_b, 0x30 ;subtract 0x30 to convert ascii number to actual int
    mov eax, 10     ;move the running int for our string to int conversion to eax
    mul etemp_int   ;multiply by 10
    add eax, char_e ;finally add the converted number to the int

    mov etemp_int, eax

    jmp get_digit ;jump back to positive to get more numbers
return_int:
    mov rax, temp_int
    imul r10d
    ret


unrecognized_start:
    mov rax, 1       ;syscall write
    mov rdi, 1       ;file descriptor (stdout)
    mov rsi, unrec_msg     ;message to write
    mov rdx, unrec_msg_len       ;message length
    syscall

    mov rax, 60      ;syscall exit
    mov rdi, 1      ;exit status code 0
    syscall


not_a_number:
    mov rax, 1       ;syscall write
    mov rdi, 1       ;file descriptor (stdout)
    mov rsi, notnum_msg     ;message to write
    mov rdx, notnum_msg_len     ;message length
    syscall

    mov rax, 60      ;syscall exit
    mov rdi, 1      ;exit status code 0
    syscall


finish:
    clear buf_i
    clear r11

    mov r10d, 10    ; just put 10 somewhere for us to use
    mov eax, sum    ; this will be useful when doing div
                    ; because div acts on eax

    test eax, eax   ; and eax on itself to check if negative
    jns calc_length ; if it isnt negative, skip to writing out the numbers
    mov byte [buf], 0x2D ; hex for - 
                         ; if it is negative, then write out -
    neg eax              ; get rid of negative
    inc buf_i

    
calc_length:
    ; now we will calculate the length of the number
    ; instead of having 1, 2, 3, etc for the length
    ; we will put in 10^(1-1), 10^(2-1), 10^(3-1), etc
    ; this will be useful later

    ; we start out by putting 10^(1-1) by default since no number
    ; will have less than one character

    mov r11d, 1

    ; 2 digits
    cmp eax, 10
    mov r9d, 10
    cmovge r11d, r9d
    
    ; 3 digits
    cmp eax, 100
    mov r9d, 100
    cmovge r11d, r9d

    ; 4 digits
    cmp eax, 1000
    mov r9d, 1000
    cmovge r11d, r9d
    
    ; 5 digits
    cmp eax, 10000
    mov r9d, 10000
    cmovge r11d, r9d
    
    ; 6 digits
    cmp eax, 100000
    mov r9d, 100000
    cmovge r11d, r9d
    
    ; 7 digits
    cmp eax, 1000000
    mov r9d, 1000000
    cmovge r11d, r9d
    
    ; 8 digits
    cmp eax, 10000000
    mov r9d, 10000000
    cmovge r11d, r9d
    
    ; 9 digits
    cmp eax, 100000000
    mov r9d, 100000000
    cmovge r11d, r9d

write_next_digit:
    ;sum is already in eax
    cdq
    div r11d
    ;12345
    ;r11 - 10000
    ;edx - remainder - 2345
    ;eax - quotient  - 1
    add eax, 0x30
    mov [buf + buf_i], eax
    inc buf_i

    mov sum, edx ; 2345

    mov eax, r11d
    cdq
    div r10d
    mov r11d, eax

    mov eax, sum

    test r11d, r11d
    jnz write_next_digit


    mov byte [buf + buf_i], 0x0a
    inc buf_i


    mov rax, 1       ;syscall write
    mov rdi, 1       ;file descriptor (stdout)
    mov rsi, buf     ;message to write
    mov rdx, buf_i   ;message length
    syscall

    mov rax, 60      ;syscall exit
    mov rdi, 0      ;exit status code 0
    syscall

