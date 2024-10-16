import customtkinter as ctk
import tkinter as tk

# Configurando o modo escuro
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Função que será executada ao clicar no círculo (transição para a segunda tela)
def iniciar_analise():
    # Remove todos os widgets da janela para a troca de tela
    for widget in janela.winfo_children():
        widget.pack_forget()
    # Mostra a segunda tela (resultado)
    mostrar_resultado()

# Função para verificar se o clique está dentro do círculo
def clique_dentro_do_circulo(event):
    x, y = event.x, event.y
    # Verificando se o clique está dentro dos limites do círculo
    if 30 <= x <= 270 and 30 <= y <= 270:
        iniciar_analise()

# Função que cria a primeira tela
def criar_primeira_tela():
    # Criando o texto de boas-vindas
    texto_bem_vindo = ctk.CTkLabel(janela, text="Intelligent Network Security System", font=("Arial", 24))
    texto_bem_vindo.pack(pady=20)

    # Pegando a cor de fundo da janela (CTk) para usar no Canvas
    cor_fundo = janela.cget("bg")

    # Criando o Canvas para desenhar os círculos
    canvas = tk.Canvas(janela, width=300, height=300, bg=cor_fundo, highlightthickness=0)
    canvas.pack(pady=20)

    # Desenhando o círculo externo (borda maior)
    circulo_externo = canvas.create_oval(30, 30, 270, 270, outline="white", width=5)

    # Desenhando o círculo interno (borda menor)
    circulo_interno = canvas.create_oval(40, 40, 260, 260, outline="white", width=3)

    # Colocando o texto dentro do círculo
    canvas.create_text(150, 130, text="Iniciar", font=("Arial", 18), fill="white")
    canvas.create_text(150, 160, text="Análise de rede", font=("Arial", 14), fill="white")

    # Associando o clique ao Canvas inteiro para verificar se foi dentro do círculo
    canvas.bind("<Button-1>", clique_dentro_do_circulo)

    # Criando um frame sem borda para organizar os campos
    frame_com_borda = ctk.CTkFrame(janela, fg_color=cor_fundo)
    frame_com_borda.pack(pady=20, padx=10)

    # Criando um frame interno para os campos na mesma linha
    frame_campos = ctk.CTkFrame(frame_com_borda, fg_color=cor_fundo)
    frame_campos.pack(pady=10, padx=10)

    # Adicionando o campo de HostName no frame
    label_hostname = ctk.CTkLabel(frame_campos, text="HostName", font=("Arial", 14))
    label_hostname.grid(row=0, column=0, padx=10)
    entrada_hostname = ctk.CTkEntry(frame_campos, placeholder_text="HostName")
    entrada_hostname.grid(row=1, column=0, padx=10)

    # Adicionando o campo de Senha no frame
    label_senha = ctk.CTkLabel(frame_campos, text="Senha", font=("Arial", 14))
    label_senha.grid(row=0, column=1, padx=10)
    entrada_senha = ctk.CTkEntry(frame_campos, placeholder_text="Senha", show="*")
    entrada_senha.grid(row=1, column=1, padx=10)

    # Adicionando o menu suspenso de nível de análise no frame
    label_nivel = ctk.CTkLabel(frame_campos, text="Nível", font=("Arial", 14))
    label_nivel.grid(row=0, column=2, padx=10)
    opcoes_nivel = ctk.CTkOptionMenu(frame_campos, values=["Análise de nível 1", "Análise de nível 2", "Análise de nível 3"])
    opcoes_nivel.set("Análise de nível 2")
    opcoes_nivel.grid(row=1, column=2, padx=10)

# Função que cria a segunda tela (resultado da análise)
def mostrar_resultado():
    # Criando o texto de resultado da análise
    texto_resultado = ctk.CTkLabel(janela, text="Resultado da Análise", font=("Arial", 24))
    texto_resultado.pack(pady=20)

    cor_fundo = janela.cget("bg")

    # Criando o Canvas para desenhar o círculo com a pontuação
    canvas = tk.Canvas(janela, width=300, height=300, bg=cor_fundo, highlightthickness=0)
    canvas.pack(pady=20)

    # Desenhando o círculo externo (borda maior)
    circulo_externo = canvas.create_oval(30, 30, 270, 270, outline="white", width=5)

    # Desenhando o círculo interno (borda menor)
    circulo_interno = canvas.create_oval(40, 40, 260, 260, outline="white", width=3)

    # Colocando o texto da pontuação dentro do círculo
    canvas.create_text(120, 120, text="750", font=("Arial", 30), fill="white")
    canvas.create_text(160, 127, text="/1000", font=("Arial", 16), fill="white", anchor="w")
    canvas.create_text(150, 180, text="Score", font=("Arial", 22), fill="white")

    
    # Criando o botão para baixar relatório
    botao_relatorio = ctk.CTkButton(janela, text="Baixar relatório detalhado", font=("Arial", 12), width=220, command=lambda: print("Baixar relatório"))
    botao_relatorio.pack(pady=40)

# Inicializando a janela
janela = ctk.CTk()
janela.geometry("600x430")
janela.title("Intelligent Network Security System")

# Criar a primeira tela ao iniciar a aplicação
criar_primeira_tela()

# Iniciando a janela
janela.mainloop()
