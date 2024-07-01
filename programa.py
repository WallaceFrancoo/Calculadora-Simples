import tkinter as tk
from tkinter import Label, Button, StringVar, Entry
import parametros
import funcoes

tela = tk.Tk()
tela. title("Calculadora Simples")

def FazerCalculo(operador):
    resultado = funcoes.Calculadora(campValor1.get(), campValor2.get(), operador)
    textoResultado.config(text=f"O Resultado é: {resultado}")

tela.geometry(f"{parametros.Largura}x{parametros.Altura}")

textValor1 = Label(tela, text="Digite o 1 valor:")
textValor1.grid(row=0, column=0,padx=5,pady=5)
campValor1 = Entry(tela)
campValor1.grid(row=0, column=1, padx=5, pady=5)

textValor2 = Label(tela, text="Digite o 2 valor:")
textValor2.grid(row=1, column=0,padx=5,pady=5)
campValor2 = Entry(tela)
campValor2.grid(row=1, column=1, padx=5, pady=5)

# Frame para os botões
Botoes = tk.Frame(tela)
Botoes.grid(row=2, column=0, columnspan=2, pady=5)

botaoSoma = tk.Button(Botoes, text="+",width=3, command=lambda: FazerCalculo(botaoSoma.cget("text")))
botaoSoma.grid(row=2, column=0, padx=1, pady=5)

botaoSubtracao = tk.Button(Botoes, text="-",width=3, command=lambda: FazerCalculo(botaoSubtracao.cget("text")))
botaoSubtracao.grid(row=2, column=1, padx=1, pady=5)

botaoMultiplicacao = tk.Button(Botoes, text="*",width=3, command=lambda: FazerCalculo(botaoMultiplicacao.cget("text")))
botaoMultiplicacao.grid(row=2, column=2, padx=1, pady=5)

botaoDivisao = tk.Button(Botoes, text="/",width=3, command=lambda: FazerCalculo(botaoDivisao.cget("text")))
botaoDivisao.grid(row=2, column=3, padx=1, pady=5)


Resultado = tk.Frame(tela)
textoResultado = Label(tela, text=f"O Resultado é:""")
textoResultado.grid(row=3, column=0, padx=1, pady=5)


tela.mainloop()



print("Funcionou")