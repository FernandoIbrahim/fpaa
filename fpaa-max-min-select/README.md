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

# **Atenálise da Complexidade pelo Teorema Mestre**

O algoritmo segue um padrão de **divisão e conquista**, e sua recorrência pode ser expressa como:  

```
T(n) = 2T(n/2) + O(1)
```

onde:  
- **\(a = 2\)** → O problema é dividido em **duas chamadas recursivas**.  
- **\(b = 2\)** → Cada chamada processa **metade do tamanho original**.  
- **\(f(n) = O(1)\)** → O custo da etapa de combinação (comparação de máximos e mínimos) é constante.  

## **Aplicação do Teorema Mestre**  

O Teorema Mestre avalia a complexidade de recorrências da forma:  

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
