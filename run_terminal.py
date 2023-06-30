from module import *

origem = input("Informe a origem: ")
destino = input("Informe o destino: ")

# Validação da data inicial
while True:
    data_inicial = input("Informe a data inicial (formato: DD/MM/AAAA): ")
    try:
        date_inicial = datetime.strptime(data_inicial, "%d/%m/%Y")
        if date_inicial.date() >= datetime.now().date():
            break
        else:
            print("Data inicial deve ser posterior ou igual ao dia de hoje.")
    except ValueError:
        print("Formato de data inválido. Por favor, insira no formato DD/MM/AAAA.")

# Validação da data final
while True:
    data_final = input("Informe a data final (formato: DD/MM/AAAA): ")
    try:
        date_final = datetime.strptime(data_final, "%d/%m/%Y")
        if date_final.date() >= date_inicial.date():
            break
        else:
            print("Data final deve ser posterior ou igual à data inicial.")
    except ValueError:
        print("Formato de data inválido. Por favor, insira no formato DD/MM/AAAA.")


obter_lowest_points(origem, destino, data_inicial, data_final)

#for resultado in resultados:
 #   print(resultado)