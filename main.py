import datetime
import winsound


def salvar_historico(operacao, num1, num2, resultado):
    with open("historico_calculadora.txt", "a") as file:
        file.write(f"{datetime.datetime.now()} - {operacao}: {num1}, {num2} = {resultado}\n")


def beep():
    # No Windows, use 'beep' do sistema operacional
    # Altere conforme necessário para outros sistemas operacionais
    #os.system("echo \a")  # O comando 'echo \a' tenta emitir um beep no terminal
    winsound.Beep(1000, 1000)  # Frequência de 1000 Hz, duração de 200 ms

def calculadora():
    while True:
        print("Opções:")
        print("Digite 'add' para adicionar dois números")
        print("Digite 'subtract' para subtrair dois números")
        print("Digite 'multiply' para multiplicar dois números")
        print("Digite 'divide' para dividir dois números")
        print("Digite 'exit' para sair do programa")
        user_input = input(": ")

        if user_input == "exit":
            break
        elif user_input in ('add', 'subtract', 'multiply', 'divide'):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = None

            if user_input == 'add':
                resultado = num1 + num2
            elif user_input == 'subtract':
                resultado = num1 - num2
            elif user_input == 'multiply':
                resultado = num1 * num2
            elif user_input == 'divide':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    print("Não é possível dividir por zero.")
                    continue

            print("Resultado: ", resultado)
            salvar_historico(user_input, num1, num2, resultado)
            beep()
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    calculadora()
