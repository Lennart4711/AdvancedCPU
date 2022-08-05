VAR result 0
VAR A 27
VAR B 41
VAR counter 0
VAR one 1

.loop
    LDA result
    ADD B
    STA result
    LDA counter
    ADD one
    STA counter
    SUB A
    JZ .end
    J .loop

.end
    LDA result
    OUT
    HLT