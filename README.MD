# Tradutor de assembly para hexadecimal

## Como funciona

O arquivo assembly.txt deverá ser carregado com o codigo em assembly, porem tem que ser indicado qual flag pretende usar (tabela das flags abaixo), e qual o formato da instrução (2,3 ou 4)

![tabela flags](https://i.ibb.co/mbt1dnq/Screenshot-from-2023-11-27-21-41-19.png)

No fim o assembly.txt ficará assim:

LDA 20 flag 13 3\
ADD 10 flag 13 3\
STA 16 flag 13 3\
LDB 33 flag 13 3\
MULTR A B\
STB 21 flag 13 3\
COMPR A B\
LDA 21 flag 1 3

Apenas execute o arquivo python e pronto, program.txt terá o cod em hexadecimal
