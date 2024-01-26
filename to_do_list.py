import tkinter as tk

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
        salvar_tarefas()
        
def remover_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        lista_tarefas.delete(selecao)
        salvar_tarefas()
        
def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        tarefas = lista_tarefas.get(0, tk.END)
        arquivo.writelines(tarefa + "\n" for tarefa in tarefas)
        
def carregar_tarefas():
    try:
        with open("tarefas.txt", "r") as arquivo:
            for linha in arquivo:
                tarefa = linha.strip()
                if tarefa:
                    lista_tarefas.insert(tk.END, tarefa)
    except FileNotFoundError:
        pass
    
janela = tk.Tk()

janela.title("To-Do List")
bg_color = "#EAEAEA"
font_family = "Arial"
font_size = 12

janela.configure(bg=bg_color)

entrada_tarefa = tk.Entry(janela, width=30, 
                          font=(font_family, font_size))
entrada_tarefa.pack(pady=10, side=tk.LEFT)

botao_adicionar = tk.Button(janela, text="✓", 
                            command=adicionar_tarefa, 
                            bg="#4CAF50", fg="white", 
                            font=(font_family, font_size))
botao_adicionar.pack(side=tk.LEFT, padx=5)

botao_remover = tk.Button(janela, text="X", 
                          command=remover_tarefa, 
                          bg="#F44336", fg="white", 
                          font=(font_family, font_size))
botao_remover.pack(side=tk.LEFT, padx=5)

lista_tarefas = tk.Listbox(janela, width=40, 
                           font=(font_family, font_size))
lista_tarefas.pack()

carregar_tarefas()
janela.mainloop()
