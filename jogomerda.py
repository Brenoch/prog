import tkinter as tk
from tkinter import ttk
import random

def jogar_cara_coroa(jogador):
    resultado = random.choice(["Cara", "Coroa"])
    if jogador == "Breno":
        label_resultado_breno.config(text=resultado)
    elif jogador == "Thiago":
        label_resultado_thiago.config(text=resultado)

# Configuração da janela
janela = tk.Tk()
janela.title("Jogo de Cara ou Coroa")
janela.geometry("400x300")
janela.configure(bg='#e6f2ff')

# Estilo do notebook
style = ttk.Style(janela)
style.theme_use('clam')
style.configure('TNotebook', background='#e6f2ff')
style.configure('TFrame', background='#e6f2ff')

# Notebook para separar os jogadores
notebook = ttk.Notebook(janela)
notebook.pack(pady=10)

# Frame para Breno
frame_breno = ttk.Frame(notebook)
frame_breno.pack(fill='both', expand=True)

# Rótulos para exibir o resultado de Breno
label_breno = tk.Label(frame_breno, text="Breno", font=("Arial", 16), bg='#e6f2ff')
label_breno.pack(pady=5)

label_resultado_breno = tk.Label(frame_breno, text="", font=("Arial", 24), bg='#e6f2ff')
label_resultado_breno.pack(pady=10)

# Botão para jogar de Breno
botao_jogar_breno = tk.Button(frame_breno, text="Jogar Breno", font=("Arial", 14), bg='#008CBA', fg='white', padx=10, pady=5, command=lambda: jogar_cara_coroa("Breno"))
botao_jogar_breno.pack()

# Adicionando o frame de Breno ao notebook
notebook.add(frame_breno, text="Breno")

# Frame para Thiago
frame_thiago = ttk.Frame(notebook)
frame_thiago.pack(fill='both', expand=True)

# Rótulos para exibir o resultado de Thiago
label_thiago = tk.Label(frame_thiago, text="Thiago", font=("Arial", 16), bg='#e6f2ff')
label_thiago.pack(pady=5)

label_resultado_thiago = tk.Label(frame_thiago, text="", font=("Arial", 24), bg='#e6f2ff')
label_resultado_thiago.pack(pady=10)

# Botão para jogar de Thiago
botao_jogar_thiago = tk.Button(frame_thiago, text="Jogar Thiago", font=("Arial", 14), bg='#4CAF50', fg='white', padx=10, pady=5, command=lambda: jogar_cara_coroa("Thiago"))
botao_jogar_thiago.pack()

# Adicionando o frame de Thiago ao notebook
notebook.add(frame_thiago, text="Thiago")

# Execução da janela
janela.mainloop()
