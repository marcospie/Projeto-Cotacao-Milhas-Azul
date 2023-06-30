import sys
import threading
import os
from tkinter import Tk, Label, Button, Text, Scrollbar, messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from ttkthemes import ThemedTk
from module import obter_lowest_points
from module import cotacoes_folder

class TextOutput(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert("end", text)

    def flush(self):
        pass


def obter_lowest_points_thread(origem, destino, data_inicial, data_final):
    try:
        resultados = obter_lowest_points(origem, destino, data_inicial, data_final)

        menor_valor = float('inf')
        data_menor_valor = ''
        for resultado in resultados:
            lowest_points = resultado['Lowest Points']
            if isinstance(lowest_points, int) or isinstance(lowest_points, float):
                if lowest_points < menor_valor:
                    menor_valor = lowest_points
                    data_menor_valor = resultado['Data']

        # Atualizar o rótulo com o menor valor e sua data
        label_valor_data.config(text=f"Menor Valor: {menor_valor} (Data: {data_menor_valor})")

        # Atualizar o rótulo com o menor valor e sua data
        label_valor_data.config(text=f"Menor Valor: {menor_valor} (Data: {data_menor_valor})")

        text_output.insert("end", "Foi gerada a cotação nas datas solicitadas\n")
        text_output.see("end")

        resposta = messagebox.askquestion("Abrir Arquivo", "Deseja abrir o arquivo de cotação?", icon="question")

        if resposta == "yes":
            data_inicial = data_inicial.replace("/", "_")
            data_final = data_final.replace("/", "_")
            data_inicial = data_inicial[:-5]
            data_final = data_final[:-5]
            cotacao_filename = "Cotacao_" + origem + destino + "_" + data_inicial + "ate" + data_final + ".xlsx"
            if os.path.exists(cotacoes_folder + cotacao_filename):
                os.startfile(cotacoes_folder + cotacao_filename)
            else:
                print("O arquivo de cotação não foi encontrado.")

    except Exception as e:
        text_output.insert("end", f"Ocorreu um erro: {str(e)}\n")
        text_output.see("end")
    finally:
        button_cotar.config(state="normal")


def obter_lowest_points_gui():
    origem = entry_origem.get()
    destino = entry_destino.get()
    data_inicial = entry_data_inicial.get_date().strftime("%d/%m/%Y")
    data_final = entry_data_final.get_date().strftime("%d/%m/%Y")

    button_cotar.config(state="disabled")

    sys.stdout = TextOutput(text_output)

    text_output.insert("end", "Carregando... Por favor, aguarde.\n")
    text_output.see("end")
    text_output.update()

    thread = threading.Thread(target=obter_lowest_points_thread, args=(origem, destino, data_inicial, data_final))
    thread.start()


root = ThemedTk(theme='yaru')
root.title("Cotação de Milhas Azul")
root.configure(bg='#76d1f0')


window_width = 400
window_height = 530
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

label_origem = ttk.Label(root, text="Origem:")
entry_origem = ttk.Entry(root)

label_destino = ttk.Label(root, text="Destino:")
entry_destino = ttk.Entry(root)

label_data_inicial = ttk.Label(root, text="Data Inicial:")
entry_data_inicial = DateEntry(root, date_pattern="dd/mm/yyyy")

label_data_final = ttk.Label(root, text="Data Final:")
entry_data_final = DateEntry(root, date_pattern="dd/mm/yyyy")

button_cotar = ttk.Button(root, text="Obter Cotação", command=obter_lowest_points_gui)

label_menor_valor = ttk.Label(root, text="Menor Valor:")

label_valor_data = ttk.Label(root, text="")

text_output = Text(root, height=30, wrap="word")
scrollbar = Scrollbar(root, command=text_output.yview)
text_output.configure(yscrollcommand=scrollbar.set)

label_origem.pack(pady=10)
entry_origem.pack()

label_destino.pack(pady=10)
entry_destino.pack()

label_data_inicial.pack(pady=10)
entry_data_inicial.pack()

label_data_final.pack(pady=10)
entry_data_final.pack()

button_cotar.pack(pady=20)

label_menor_valor.pack(pady=10)

label_valor_data.pack(pady=10)

text_output.pack(pady=10)
scrollbar.pack(side="right", fill="y")

root.mainloop()