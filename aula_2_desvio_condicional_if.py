# -*- coding: utf-8 -*-
"""Aula_2_Desvio_Condicional_IF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/storopoli/ciencia-de-dados/blob/master/notebooks/Aula_2_Desvio_Condicional_IF.ipynb

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/storopoli/ciencia-de-dados/master?filepath=notebooks%2FAula_2_Desvio_Condicional_IF.ipynb)
<br>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/storopoli/ciencia-de-dados/blob/master/notebooks/Aula_2_Desvio_Condicional_IF.ipynb)

# Desvio Condicional (`IF`)

**Objetivos**: Apresentar desvio condicional em Python (`IF`)

Os desvios condicionais, também chamados de estruturas de seleção ou decisão, são
utilizados quando existe a necessidade de verificar condições para a realização de uma
instrução ou de uma sequência de instruções. Os testes de seleção também podem ser
utilizados para verificar opções de escolha.

## Desvio Condicional Simples

Esse tipo de desvio é representado por uma instrução que avalia uma expressão lógica, resultando um valor que pode ser verdadeiro ou falso. Ele deve ser utilizado caso seja necessário executar instruções somente se uma condição for verdadeira.

**Cuidado com indentação (*identation*)**

```python
if (condição):
    instruções condição verdadeira
instruções independentemente da condição ser verdadeira ou não
```
"""

a = 5
b = 5
c = 0

if (a == b):
    print('a é igual a b')
    c +=2
print('Valor de c: ', c)

a = 5
b = 5
c = 0
if (a != b):
    print('a é diferente de b')
    c +=2
print('Valor de c: ', c)

a = 5
b = 5
c = 0

if (a == b):
    print('a é igual a b')
    if (c + 5 == a):
        print('c mais cinco é igual a a')
        c += 2
    c +=2
print('Valor de c: ', c)

a = 5
b = 5
c = 0

if (a == b):
    print('a é igual a b')
    if (c + 6 == a):
        print('c mais seis é igual a a')
        c += 2
    c +=2
print('Valor de c: ', c)

"""## Desvio Condicional Composto
O desvio condicional composto prevê uma condição com 2 conjuntos de instruções para serem realizados de acordo com a avaliação da resposta: um bloco de instruções para resposta verdadeiro e um bloco de instruções para resposta falso.

```python
if (condição):
    instruções condição verdadeira
else:
    instrução condição falsa
instruções independentemente da condição ser verdadeira ou não
```
"""

a = 5
b = 5
c = 0

if (a == b):
    print('a é igual a b')
    if (c + 5 == a):
        print('c mais cinco é igual a a')
        c += 2
else:
    c +=3
print('Valor de c: ', c)

a = 5
b = 5
c = 0

if (a != b):
    print('a é diferente de b')
    if (c + 6 == a):
        print('c mais seis é igual a a')
        c += 2
else:
    c +=3
print('Valor de c: ', c)

"""## Desvio Condicional Encadeado
Um desvio condicional encadeado é uma sequência de testes de seleção, os quais serão executados ou não de acordo com o resultado das condições e de acordo com o encadeamento dos testes.

Existem casos em que é necessário estabelecer algumas verificações lógicas de condições definidas sucessivamente. A ideia aqui apresentada sugere a possibilidade de usar uma condição dentro de outra condição, o que leva a uma estrutura de decisão encadeada ou aninhada.

```python
if (condição_1):
    instruções condição_1 verdadeira
elif (condição_2):
    instruções condição_2 verdadeira
elif (condição_3):
    instruções condição_3 verdadeira
else:
    instrução condições falsas
instruções independentemente das condições serem verdadeiras ou não
```
"""

c = 0
a = int(input("informe valor de a: \n"))

if (a==1):
    c = 10
elif (a==2):
    c = 11
elif (a==3):
    c = 12
elif (a==4):
    c = 13
elif (a==5):
    c = 14
else:
    c = 20
print(c)

"""## Atividade

1. Designe uma variável `x` com o valor $8$
2. Designe uma variável `y` com o valor $15$
3. Crie 2 desvios condicionais:
    * O primeiro deve imprimir "Ao menos uma das condições foi satisfeita" se `x` maior que $3$ **ou** `y` é número par
    * O segundo deve imprimir "Nenhuma condição foi satisfeita" se `x` menor ou igual a $3$ **e** `y` é número ímpar


Observação: use o módulo `%` para identificar número *ímpar* e *par*
"""

###