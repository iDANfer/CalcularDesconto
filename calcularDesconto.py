import tkinter as tk

def calcular_desconto():
    preco_produto = float(entry_preco.get())
    desconto_produto = float(entry_desconto.get())

    resultado_desconto = preco_produto * desconto_produto / 100
    resultado_final = preco_produto - resultado_desconto

    label_resultado_desconto.config(text=f"O Valor do Desconto é: {resultado_desconto:.2f}")
    label_resultado_final.config(text=f"O Valor Final é: {resultado_final:.2f}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Desconto")

# Criar e posicionar os widgets na janela
label_preco = tk.Label(janela, text="Informe o preço do produto:")
label_preco.pack()

entry_preco = tk.Entry(janela)
entry_preco.pack()

label_desconto = tk.Label(janela, text="Informe o Valor do Desconto:")
label_desconto.pack()

entry_desconto = tk.Entry(janela)
entry_desconto.pack()

button_calcular = tk.Button(janela, text="Calcular", command=calcular_desconto)
button_calcular.pack()

label_resultado_desconto = tk.Label(janela, text="O Valor do Desconto é: ")
label_resultado_desconto.pack()

label_resultado_final = tk.Label(janela, text="O Valor Final é: ")
label_resultado_final.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()
