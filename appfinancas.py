import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt


movimentacoes = []

#funcao

def adicionar_receita():
    descricao = entry_descricao.get()
    valor = entry_valor.get()

    if descricao == "" or valor == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    try:
        valor = float(valor)
    except ValueError:
        messagebox.showwarning("Erro", "Digite um valor numérico!")
        return

    movimentacoes.append({
        "tipo": "Receita",
        "descricao": descricao,
        "valor": valor
    })

    atualizar_extrato()
    limpar_campos()

def adicionar_despesa():
    descricao = entry_descricao.get()
    valor = entry_valor.get()

    if descricao == "" or valor == "":
        messagebox.showwarning("Erro", "Preencha todos os campos!")
        return

    try:
        valor = float(valor)
    except ValueError:
        messagebox.showwarning("Erro", "Digite um valor numérico!")
        return

    movimentacoes.append({
        "tipo": "Despesa",
        "descricao": descricao,
        "valor": -valor
    })

    atualizar_extrato()
    limpar_campos()

def atualizar_extrato():
    texto_extrato.delete("1.0", tk.END)

    saldo = 0
    for mov in movimentacoes:
        texto_extrato.insert(
            tk.END,
            f"{mov['tipo']} - {mov['descricao']} : R$ {mov['valor']:.2f}\n"
        )
        saldo += mov["valor"]

    label_saldo.config(text=f"Saldo: R$ {saldo:.2f}")

def limpar_campos():
    entry_descricao.delete(0, tk.END)
    entry_valor.delete(0, tk.END)

def mostrar_grafico():
    total_receitas = 0
    total_despesas = 0

    for mov in movimentacoes:
        if mov["valor"] > 0:
            total_receitas += mov["valor"]
        else:
            total_despesas += abs(mov["valor"])

    if total_receitas == 0 and total_despesas == 0:
        messagebox.showinfo("Aviso", "Não há dados para gerar o gráfico.")
        return

    plt.bar(["Receitas", "Despesas"], [total_receitas, total_despesas])
    plt.title("Resumo Financeiro")
    plt.ylabel("Valor (R$)")
    plt.show()

#interface

janela = tk.Tk()
janela.title("App Finanças Pessoais")
janela.geometry("420x550")
janela.resizable(False, False)

tk.Label(janela, text="Descrição").pack(pady=2)
entry_descricao = tk.Entry(janela, width=30)
entry_descricao.pack()

tk.Label(janela, text="Valor").pack(pady=2)
entry_valor = tk.Entry(janela, width=30)
entry_valor.pack()

tk.Button(
    janela,
    text="Adicionar Receita",
    command=adicionar_receita,
    bg="green",
    fg="white",
    width=25
).pack(pady=5)

tk.Button(
    janela,
    text="Adicionar Despesa",
    command=adicionar_despesa,
    bg="red",
    fg="white",
    width=25
).pack(pady=5)

tk.Button(
    janela,
    text="Ver Gráfico",
    command=mostrar_grafico,
    width=25
).pack(pady=10)

label_saldo = tk.Label(
    janela,
    text="Saldo: R$ 0.00",
    font=("Arial", 12, "bold")
)
label_saldo.pack(pady=10)

texto_extrato = tk.Text(janela, width=45, height=15)
texto_extrato.pack()

# ==============================
# INICIAR APP
# ==============================
janela.mainloop()
