# Programa para rastrear despesas diarias
# Autor: Alef Santos Viana
# Versao: 1.0
# Data: 22-10-2026

#O funcionamento do programa é o seguinte:
# 1. O usuário insere uma nova despesa.
# 2. O programa armazena a despesa em uma lista.
# 3. O usuário pode visualizar todas as despesas.
# 4. O programa pode calcular o total e a média das despesas.
# 5. O usuário pode limpar todas as despesas.
# 6. O usuário pode sair do programa.


## Menu principal
print("Welcome to the Daily Expense Tracker!")
print("-----------------")
print("""Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit""")
# Lista para armazenar as despesas
despesas = []
# Loop principal
print("-----------------")
while True:
    choice = int(input("Enter your choice (1-5): "))
    # Validação da escolha
    if choice not in range(1,6):
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue
    # Opções do menu
    if choice == 1:# Opção 1: Adicionar uma nova despesa
        expense = float(input("Enter the expense amount: "))
        despesas.append(expense)
        print("Expense added successfully!")
    elif choice == 2:# Opção 2: Visualizar todas as despesas
        if not despesas:
            print("No expenses added yet.")
        else:
            print("All Expenses:")
            for index, expense in enumerate(despesas,start=1):
                print(f"{index}. {expense:.2f}")
    elif choice == 3:# Opção 3: Calcular o total e a média das despesas
        if not despesas:
            print("No expenses added yet.")
        try:
            total = sum(despesas)
            average = total / len(despesas)
            print(f"Total Expenses: {total:.2f}")
            print(f"Average Expense: {average:.2f}")
        except ZeroDivisionError:
            print("No expenses added yet.") 
    elif choice == 4:# Opção 4: Limpar todas as despesas
        despesas.clear()
        print("All expenses cleared successfully!")

    elif choice == 5:# Opção 5: Sair do programa
        print("Goodbye!")
        break