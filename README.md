# Problem Set 1: Algoritmo de Luhn - Validação de cartão de crédito

Projeto feito como requisito avaliativo da disciplina de *Linguagens de Programação* na Universidade Vila Velha

## Pré-requisitos para execução
- Python (Testado apenas na versão 3.10.6)

## Executando o projeto

Para realizar a execução, é bem simples, basta digitar:

```sh
$ python3 credit.py
```
ou dependendo da sua instalação do python
```sh
$ py credit.py
```

Após isso, o programa irá lhe pedir para inserir um número de um cartão de crédito, caso o número for inválido, ele irá repetir e te pedir novamente para inserir um número válido. Caso o cartão seja inválido ou a bandeira não seja VISA, AMEX ou MSTERCARD, o programa responderá: `INVÁLIDO\n`.


## Exemplos de respostas do programa

### Inserção de números inválidos um número inválido
```sh
$ python3 credit.py
Número: 37144963539843d
Número: 3714 4539 8431
Número: 371445398431
INVÁLIDO

```

### Inserção de números válidos dentro das bandeiras identificadas
```sh
$ python3 credit.py
Número: 371449635398431
AMEX

```

### Inserção de números válidos de bandeiras diferentes de AMEX, VISA ou MASTERCARD
```sh
$ python3 credit.py
Número: 3530111333300000
INVÁLIDO

```