
import tkinter as tk

def calcular_valor():
    m_padrao = float(entry_m_padrao.get())
    custo = float(entry_custo.get())
    m_especial = float(entry_m_especial.get())

    r = custo / m_padrao
    valor = (r * m_especial) + 10/100

    resultado_label.config(text=f'O valor para medida especial é R${valor:,.1f}')

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora de Valor")

# Elementos da Interface
label_m_padrao = tk.Label(janela, text="Metro Quadrado Padrão:")
entry_m_padrao = tk.Entry(janela)

label_custo = tk.Label(janela, text="Custo da Tabela:")
entry_custo = tk.Entry(janela)

label_m_especial = tk.Label(janela, text="Medida Especial:")
entry_m_especial = tk.Entry(janela)

calcular_button = tk.Button(janela, text="Calcular", command=calcular_valor)

resultado_label = tk.Label(janela, text="Resultado aparecerá aqui.")

# Layout dos Elementos
label_m_padrao.pack()
entry_m_padrao.pack()

label_custo.pack()
entry_custo.pack()

label_m_especial.pack()
entry_m_especial.pack()

calcular_button.pack()

resultado_label.pack()

# Iniciar o loop de eventos
janela.mainloop()
