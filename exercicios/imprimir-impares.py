import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Exemplo de Confirmação (Sim/Não)
resposta = messagebox.askyesno("Confirmação", "Você deseja continuar?")
if resposta:
    print("Usuário clicou em Sim")
else:
    print("Usuário clicou em Não")


tamanho = int(tk.simpledialog.askstring("Imprimir Números Impares", "Digite o tamanho da lista:"))

for i in range(tamanho+1):

    if i % 2 == 0:
        continue
    messagebox.showinfo("Impares", i)