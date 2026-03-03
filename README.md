# Calculadora em Python com Script de Automação

## Descrição

Este projeto consiste em uma calculadora simples desenvolvida em Python, acompanhada de um script Shell (.sh) responsável por automatizar sua execução.

O objetivo do projeto é praticar conceitos básicos de:

- Programação em Python
- Execução de scripts no Linux
- Automação com Shell Script
- Versionamento com Git e GitHub

## Decisões de Projeto

O professor deu liberdade para que a calculadora pudesse ser simples (com poucas linhas de código) ou mais robusta.

Optei por desenvolver uma versão intermediária, contendo os 5 operadores mais utilizados no dia a dia:

- Soma
- Subtração
- Multiplicação
- Divisão
- Porcentagem

A aplicação foi projetada para operar com dois números por vez (inteiros ou reais), retornando imediatamente o resultado após a escolha da operação.

Além da lógica matemática, meu foco principal foi a experiência do usuário.  
Implementei validações para evitar que o programa fosse interrompido caso o usuário digitasse:

- Caracteres inválidos no lugar de números
- Operadores que não estão entre as opções disponíveis

O objetivo foi tornar a aplicação mais estável e evitar que o código "quebrasse" diante de entradas inesperadas.
  
## Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/miranda-data/calculadora.git
```

### 2. Acesse a pasta do projeto
```bash
cd calculadora
```
### 3. Dê permissão de execução ao script
```bash
chmod +x executarcalculadora.sh
```
### 4. Execute o script
```bash
./executarcalculadora.sh
```

## Explicação técnica 
O código começa com uma estrutura while True, que basicamente fica repetindo até que o usuário digite algo válido.

Dentro desse while, eu uso um try para tentar converter o valor digitado para float.
Se der certo, o programa executa o break e sai do loop.
Se o usuário digitar qualquer coisa que não seja número, entra no except ValueError e exibe a mensagem pedindo para digitar apenas números.

Faço isso duas vezes: uma para o primeiro número e outra para o segundo.

Depois disso, o programa pede para o usuário digitar qual operação deseja realizar.

Em seguida entra em uma estrutura condicional com if, elif e else.
Ali eu verifico qual operador foi digitado:

Se for "+", ele soma.

Se for "-", ele subtrai.

Se for "*", ele multiplica.

Se for "/", ele divide.

No caso da divisão, eu acrescentei uma verificação extra:
Se o segundo número for igual a 0, o programa mostra a mensagem dizendo que não é possível dividir por zero.
Se não for zero, ele realiza a divisão normalmente.

Também incluí o operador "%", que retorna o resto da divisão.

Por fim, no else, caso o usuário digite um operador que não esteja entre os permitidos, o programa informa que a operação é inválida e mostra quais operadores são aceitos.

A ideia principal foi evitar que o programa quebrasse caso o usuário inputasse uma entrada inválida, tratando tanto erros de entrada numérica quanto operadores inválidos.

## Estrutura do projeto
calculadora.py              # Lógica principal da aplicação
executarcalculadora.sh      # Script responsável por executar o programa
README.md                   # Documentação do projeto

## Sobre este projeto
Este é meu primeiro projeto publicado.
Primeira aplicação, primeiro script, primeira documentação — primeiro tudo.

E isso, por si só, já significa muito para mim.

Escrever e documentar esse projeto foi uma experiência especial. Existe um sentimento de nostalgia nisso. Lembro de quando eu baixava softwares e jogos e sempre vinha um README bem autoral, escrito por alguém que claramente dominava o que estava fazendo. Eu lia aquilo e pensava: “O cara faz parecer fácil… um dia eu quero chegar nesse nível.”

Hoje estou escrevendo o meu.

Ainda estou no começo, mas estou construindo passo a passo.

Deixo aqui meu agradecimento à comunidade de tecnologia como um todo, que compartilha conhecimento e abre portas para quem quer aprender.

Um agradecimento especial à EBAC e ao professor Rodrigo Rebouças, pela didática leve e pela forma como conduz as aulas. Ele tem o dom de despertar em nós a vontade de aprender mais.

Não sei se algum dia muitas pessoas vão ler este README.
Mas independentemente disso, o aprendizado já é meu — e isso ninguém pode tirar.

Obrigado.
