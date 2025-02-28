# Descrição do Projeto: 

O objetivo deste projeto é implementar o algoritmo de multiplicação eficiente proposto por Anatolii Alexeevitch Karatsuba. Esse método reduz a complexidade da multiplicação tradicional de dois números grandes, utilizando a técnica de divisão e conquista.  


A implementação foi feita na classe `Karatsuba`, com um método estático chamado `multiply`, conforme mostrado abaixo:  


```python
class Karatsuba:
    @staticmethod
    def multiply(x, y):
        # Implementação do algoritmo
  
```

Inicialmente é verificado se os parâmetros x e y são menores que 10, caso sejam a multiplicação é realizada normalmente pela aplicação.

```python

def multiply(x , y):
    if(x < 10 or y < 10):
        return x * y

    else: 

    #...

```

  
Caso contrário, determina-se o número de dígitos do maior entre os dois números e armazena-se esse valor em `n`. Em seguida, calcula-se sua metade e armazena-se o resultado na variável `half`.


```python


else: 
    n = max(len(str(x)), len(str(y)))
    half = n // 2
	#...

```
  

Em seguida, os números x e y são divididos em suas partes superiores e inferiores, que são armazenadas nas variáveis a, b, c e d. 


``` python
#...

else:

n = max(len(str(x)), len(str(y)))

    half = n // 2

	a = x // (10 ** half) # Parte superior de x
	b = x % (10 ** half)  # Parte inferior de x
	c = y // (10 ** half) # Parte superior de y
	d = y % (10 ** half)  # Parte inferior de y

#...
```

  
Durante seus estudos, Karatsuba descobriu que o produto de X e Y pode ser calculado utilizando a seguinte fórmula:

`XY = ac x 10ˆn + ((ad) + (bd) x 10ˆn/2 )+ bc`

Onde `a` e `b` são, respectivamente, as partes superior e inferior de `X`, e `c` e `d` são as partes superior e inferior de `Y`.

Além disso, ele observou que a expressão (ad + bc) pode ser simplificada ao reescrevê-la como (a + b)(c + d) - ac - bd.


Uma vez que:

```

(a+b)(c+d) - ac - bd

= (ac + ad + bc + bd ) - ( ac + bd )

= ad + bc

```

  
Essa simplificação possibilita a eliminação de uma **multiplicação adicional**, tornando o algoritmo mais eficiente. Logo, em nosso algoritmo chegamos no seguinte resultado:


``` python 

@staticmethod

def multiply(x, y):

	if x < 10 or y < 10:
		return x * y

	else:

		n = max(len(str(x)), len(str(y)))
		half = n // 2

		a = x // (10 ** half)
		b = x % (10 ** half)
		c = y // (10 ** half)
		d = y % (10 ** half)

		ac = Karatsuba.multiply(a, c)
		bd = Karatsuba.multiply(b, d)
		ad_plus_bc = Karatsuba.multiply(a + b, c + d) - ac - bd

		return ac * (10 ** (2 * half)) + (ad_plus_bc * (10 ** half)) + bd

```

Isso propõe uma abordagem mais eficiente para realizar cálculos de multiplicação com números grandes, otimizando o desempenho de algoritmos que lidam com operações envolvendo números extensos.


# Execução

A execução do projeto pode ser realizada através da execução do seguinte comando:

```
python3 main.py
```


# Relatório Técnico

## Fluxo de Controle da função

![[Screenshot 2025-02-21 at 19.32.32.png]]

Assim, utilizamos da formula de calculo da complexidade ciclomática (𝑀 = 𝐸 − 𝑁 + 2𝑃) para 

Logo temos:

E = 9
N = 9
P = 1

M = 9 - 9 + 2
M = 2