#  Como Executar o Código

##  1. Verificar se o Java já está instalado  

Abra o **Prompt de Comando** (Windows) ou **Terminal** (macOS/Linux) e digite:  

```
java -version
```


##  2. Baixar o Java (JDK)

Caso não esteja instalado baixe a versão mais recente do Java pelo link e complete sua instalação:

- **Oracle JDK** (oficial): [Clique aqui](https://www.oracle.com/java/technologies/javase-jdk17-downloads.html) 


## 3. Execute o código

Após escolher a IDE, siga os passos abaixo:

1. Abra a IDE e selecione o diretório onde está o arquivo Java.

2. Abra o arquivo Java que contém o método main.

3. Execute o código


# Algoritmo de Seleção do Máximo e Mínimo em um Array

## Descrição
Este código implementa um algoritmo de **divisão e conquista** para encontrar o maior e o menor valor em um array de inteiros.

## Funcionamento do Código

1. A função `maxMinSelect` recebe um array e os índices **start** e **end**, representando os limites da parte do array que está sendo analisada.
2. Se houver apenas um elemento na parte analisada (`start == end`), ele é retornado como máximo e mínimo.
3. Caso contrário, o array é dividido ao meio e a função é chamada recursivamente para ambas as partes.
4. A função `findMaxMin` combina os resultados das duas metades, determinando o maior e o menor valor entre elas, retornando as em um array {maior, menor}.


```java
public class MaxMinSelection {
    public static int[] maxMinSelect(int[] arr, int start, int end) {
        if (start == end) {
            return new int[]{arr[start], arr[start]};
        }

        int mid = (start + end) / 2;
        int[] left = maxMinSelect(arr, start, mid);
        int[] right = maxMinSelect(arr, mid + 1, end);

        return findMaxMin(left, right);
    }

    public static int[] findMaxMin(int[] left, int[] right) {
        int max = Math.max(left[0], right[0]);
        int min = Math.min(left[1], right[1]);
        return new int[]{max, min};
    }
}
```

# **Análise da Complexidade pelo Teorema Mestre**

O algoritmo segue um padrão de **divisão e conquista**, e sua recorrência pode ser expressa como:  

```
T(n) = 2T(n/2) + O(1)
```

onde:  
- **\(a = 2\)** → O problema é dividido em **duas chamadas recursivas**.  
- **\(b = 2\)** → Cada chamada processa **metade do tamanho original**.  
- **\(f(n) = O(1)\)** → O custo da etapa de combinação (comparação de máximos e mínimos) é constante.  

 avaliamos a complexidade de recorrências da forma:  

```
T(n) = aT(n/b) + f(n)
```

Para determinar a complexidade, verificamos o valor de:  

``` 
n^log_b a = n^log_2 2 = n^1 = n
```

Agora, comparamos ``f(n) com  n^log_b a``:  

Como \( f(n) = O(1) \) é menor que \( n^1 \), o problema se encaixa no **Caso 1**, e a complexidade assintótica é:  

T(n) = O(n).

# **Análise da Complexidade Contagem de Operações**

O algoritmo divide recursivamente o array em duas metades até que os subarrays contenham apenas um ou dois elementos. Para cada divisão, ele realiza comparações para combinar os valores máximo e mínimo de cada metade.

• **Divisão:** O array de tamanho n é dividido em duas metades de tamanho n/2.
- Cada divisão da origem outras 2 chamadas da mesma função

```
C(n) = 2C(n/2);
```

``` java
   public static int[] maxMinSelect(int[] arr, int start, int end) {
1        if (start == end) {
           return new int[]{arr[start], arr[start]};
         }

2        int mid = (start + end) / 2;
3        int[] left = maxMinSelect(arr, start, mid);
4        int[] right = maxMinSelect(arr, mid + 1, end);

5        return findMaxMin(left, right);
    }
```

Pior caso:

1- Comparação `if (start == end)` (1)
2- atribuição `mid (start + end) / 2; (3)
3- atribuição `left = Calculo maxMinSelect` (1)
4-  atribuição `right = Calculo maxMinSelect` (1)

5- retorno com a chamada do método `findMaxMin()` (1)  + (5) do método;


```java
    public static int[] findMaxMin(int[] left, int[] right) {
1        int max = Math.max(left[0], right[0]);
2        int min = Math.min(left[1], right[1]);
3        return new int[]{max, min};
    }

```


1-Atribuição e Comparação (2)
2-Atribuição e Comparação  (2)
3- retorno; (1)