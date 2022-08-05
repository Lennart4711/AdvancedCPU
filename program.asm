VAR gpu_start 128
VAR x 0


.loop
    J .w_pressed

.w_pressed
    LDA 192
    ADI 0
    JZ .a_pressed
    LDA x
    SBI 8
    STA x
    J .a_pressed
.a_pressed
    LDA 193
    ADI 0
    JZ .s_pressed
    LDA x
    SBI 1
    STA x
    J .s_pressed
.s_pressed
    LDA 194
    ADI 0
    JZ .d_pressed
    LDA x
    ADI 8
    STA x
    J .d_pressed
.d_pressed
    LDA 195
    ADI 0
    JZ .draw
    LDA x
    ADI 1
    STA x
    J .draw
.draw
    LDA gpu_start
    ADD x
    TAX
    LDI 1
    SAX
    OUT
    J .loop