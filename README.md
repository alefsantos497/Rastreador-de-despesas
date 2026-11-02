# Projeto Rastreador de Despesas Diárias

Projeto de controle de despesas diárias em Python, executado no terminal.

- **Autor:** Alef Santos Viana
- **Versão:** 1.0
- **Data:** 22-10-2026

## Descrição

Aplicação de linha de comando (CLI) para registrar e acompanhar despesas
diárias. As despesas são armazenadas em **memória** durante a execução do
programa (em uma lista).

> Observação: as despesas **não são salvas em arquivo**. Ao encerrar o programa,
> os dados são perdidos.

## Funcionalidades

O menu principal oferece as seguintes opções:

1. **Adicionar uma nova despesa** (`Add a new expense`)
2. **Visualizar todas as despesas** (`View all expenses`)
3. **Calcular total e média das despesas** (`Calculate total and average expense`)
4. **Limpar todas as despesas** (`Clear all expenses`)
5. **Sair** (`Exit`)

Regras de comportamento:

- Ao adicionar, o valor da despesa é lido como número decimal (`float`).
- A visualização lista as despesas numeradas, com duas casas decimais.
- O cálculo exibe o total e a média; se não houver despesas, informa que nenhuma
  foi adicionada.
- Limpar remove todas as despesas registradas.
- Escolhas fora do intervalo 1–5 exibem uma mensagem de erro e o menu é mostrado
  novamente.

## Estrutura do projeto

```
rastrear_despesas/
└── rastrear_despesas.py   # Ponto de entrada: menu, loop principal e lógica
```

## Requisitos

- Python 3.x

Não há dependências externas — o projeto usa apenas a biblioteca padrão do Python.

## Como executar

Execute o programa a partir da pasta do projeto:

```bash
cd rastrear_despesas
python3 rastrear_despesas.py
```

Use o menu digitando o número da opção desejada (1 a 5).

## Exemplo de uso

```
Welcome to the Daily Expense Tracker!
-----------------
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit
-----------------
Enter your choice (1-5): 1
Enter the expense amount: 25.50
Expense added successfully!
Enter your choice (1-5): 3
Total Expenses: 25.50
Average Expense: 25.50
```

## Possíveis melhorias futuras

- Persistir as despesas em arquivo (JSON/CSV) ou banco de dados (SQLite).
- Tratar entradas inválidas (valores não numéricos) sem encerrar o programa.
- Categorizar despesas e gerar relatórios por período.
- Adicionar descrição e data a cada despesa.
