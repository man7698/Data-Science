# -*- coding: utf-8 -*-
"""Aula_3_Estruturas_de_Repeticao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/storopoli/ciencia-de-dados/blob/master/notebooks/Aula_3_Estruturas_de_Repeticao.ipynb

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/storopoli/ciencia-de-dados/master?filepath=notebooks%2FAula_3_Estruturas_de_Repeticao.ipynb)
<br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/storopoli/ciencia-de-dados/blob/master/notebooks/Aula_3_Estruturas_de_Repeticao.ipynb)

# Estruturas de Repetição (`FOR` e `WHILE`)

**Objetivos**: Apresentar as estruturas de repetição (`FOR` e `WHILE`)

O conceito de  **repetição** (looping ou laço) é utilizado quando se deseja repetir um certo trecho de instruções por um número de vezes.

As estruturas de repetição em Python se dividem em `WHILE` (enquanto) e `FOR` (para). Para determinamos qual é a estrutura mais adequada para determinado programa, devemos saber qual o número de vezes que o trecho do programa vai ser executado (laços contados) ou a condição para que ele aconteça (laços condicionais).

## Cálculo da média aritmética
"""

av1 = float(input("Informe AV1: \n"))
assert av1 <= 10, "A nota AV1 deve ser entre 0 e 10"

av2 = float(input("Informe AV2: \n"))
assert av2 <= 10, "A nota AV2 deve ser entre 0 e 10"

media = (av1 + av2) / 2

print("Média do aluno foi de: ", media)

"""## `WHILE` (enquanto)

Consiste de uma estrutura de controle do fluxo de execução que permite repetir diversas vezes um mesmo trecho do programa, porém, sempre verificando antes de cada execução se é permitido executar o trecho do programa ou não.

A estrutura de repetição `WHILE` a condição de repetição é verificada antes de entrar no laço de repetição, isto é, se o resultado for verdadeiro, o bloco de instrução será executado. Enquanto o valor da condição for verdadeiro, as ações dos comandos são executadas. No momento em que a condição se torna falsa, o processamento da rotina é desviado para fora do laço. Se a condição for falsa logo de início, os comandos não são executados nenhuma vez.

```python
while (<condição>):
    <instruções a serem executadas enquanto condição verdadeira>
```
"""

repetir = "S"
while (repetir=="S"):
    av1 = float(input("Informe AV1: \n"))
    assert av1 <= 10, "A nota AV1 deve ser entre 0 e 10"
    
    av2 = float(input("Informe AV2: \n"))
    assert av2 <= 10, "A nota AV2 deve ser entre 0 e 10"
    
    media = (av1 + av2) / 2
    print("Média do aluno foi de: \n", media)
    
    repetir = input("Digite S caso deseje calcular nova média ou outro valor caso contrário")
print("Fim do Programa")

"""## `FOR` (para)

Os laços que possuem um número finito de execuções poderão ser processados por meio de estrutura de laço FOR. Com a estrutura FOR podemos executar um determinado conjunto de instruções certo número de vezes. Além disso, este tipo de estrutura prevê uma condição e limites fixos.

A estrutura for é utilizada quando precisamos repetir um conjunto de comandos um número pré-definido de vezes.

```python
for <variável> in range(<valor inicial>, <valor limite - menor que>, <incremento a cada etapa>):
    <instruções a serem repetidas>
```
"""

for i in range(2, 17, 3):
    print(i)

qtde = int(input("Quantidade de alunos: \n"))
for x in range(0, qtde, 1):
    av1 = float(input("Informe AV1: \n"))
    assert av1 <= 10, "A nota AV1 deve ser entre 0 e 10"
    
    av2 = float(input("Informe AV2: \n"))
    assert av2 <= 10, "A nota AV1 deve ser entre 0 e 10"
    
    media = (av1 + av2) / 2
    print("Média do aluno foi de: ", media)
print("Fim do Programa")

"""## Atividade `WHILE`

1. Defina um número aleatório entre $0$ e $10$ com a função `randint()` da biblioteca `random` e designe-o para a variável `numero_aleatorio`)
2. Crie uma variável `palpites_restantes` igual a $3$
3. Use a estrutura enquanto (`WHILE`) para que o usuário continue adivinhando o valor da varíavel `numero_aleatorio` enquanto `palpites_restantes` é maior que $0$
4. Pergunte ao usuário o seu palpite sobre o valor da variável `numero_aleatorio`
5. Se ele acertar o palpite quebre o `while` com `break` e imprima "Você acertou!"
6. Se ele errar reduza `palpites_restantes` em $1$
7. Use um desvio condicional `else` depois do `while` que imprima "Você perdeu todas suas chances"
"""

from random import randint

numero_aleatorio = randint(0, 10)
palpites_restantes = $$

while(palpites_restantes > $$):
    palpite = int(input("Qual é o seu palpite? Número entre 0 e 10 \n"))
    assert palpite >= 0 and palpite <= 10, "Coloque um número inteiro entre 0 e 10"
    
    if numero_aleatorio == palpite:
        print("Você acertou")
        break 
    palpites_restantes -= $$
    print("Você errou! Tente de novo")
    
    if (palpites_restantes == $$):
        print("Você perdeu todas suas chances")
print(numero_aleatorio)

"""## Atividade `FOR`

Filtre o caractere `a` e `á` da string abaixo

```python
frase = "Mais vale um pássaro..."
```

1. Faça um `for` para cada caractere da frase
2. Se o caractere for `a` ou `á`, imprima `X` ao invés do caractere
3. Ou (`else`), imprima o caractere original da frase
"""

frase = "Mais vale um pássaro..."

for $$$ in $$$:
    if $$ == "a" or $$ == "á":
        print("X")
    else:
        print($$)