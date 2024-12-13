import customtkinter as ctk
from PIL import Image
from tkinter import filedialog

def validate_login(username_entry, password_entry, feedback_label, parent_window):
    username = username_entry.get()
    password = password_entry.get()

    if username and password:  # Valida se os campos não estão vazios
        feedback_label.configure(text="Login efetuado com sucesso.", text_color="green")
        open_dir_window(parent_window)
    else:
        feedback_label.configure(text="Por favor, insira um usuário e senha válidos.", text_color="red")

def open_dir_window(parent_window):
    dir_window = ctk.CTkToplevel(parent_window)
    dir_window.title("Painel de controle de E-mails")
    dir_window.geometry("700x450")

    # Configura o número de linha e colunas na página
    dir_window.grid_rowconfigure((0, 10), weight=1)
    dir_window.grid_columnconfigure((0, 4), weight=1)

    dir_label = ctk.CTkLabel(
        dir_window, text="Clique no espaço abaixo para selecionar \na pasta onde estão os dados a serem processados:", font=("Roboto", 16)
    )
    dir_label.grid(row=2, column=2, padx=10, pady=10, sticky="nswe")

    # Variáveis de controle
    selected_dir = ""

    def select_directory():
        nonlocal selected_dir
        selected_dir = filedialog.askdirectory(title="Selecione a pasta")
        if selected_dir:
            dir_entry.configure(text=f"{selected_dir}")
            select_repo_button.grid(row=6, column=2, padx=20, pady=10, sticky="we")  # Torna o botão visível quando uma pasta for selecionada

    # Função para abrir o editor de texto
    def open_text_editor():
        pass

    # Botão para selecionar o diretório 
    dir_entry = ctk.CTkButton(
        dir_window, text="      ", command=select_directory,
        font=("Roboto", 14), fg_color="#FFFFFF", hover_color="#FFFFFF" 
    )
    dir_entry.grid(row=5, column=2, padx=20, pady=20, sticky="we")

    # Botão para abrir a outra janela
    select_repo_button = ctk.CTkButton(
        dir_window, text="Selecionar Repositório", command=open_text_editor,
        font=("Roboto", 14), fg_color="#800000",
        hover_color="#A52A2A", state="hidden"  # Começa escondido
    )
    select_repo_button.grid(row=7, column=2, padx=20, pady=10, sticky="we")

def create_login_window():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # Janela principal
    login_window = ctk.CTk()
    login_window.geometry("700x450")
    login_window.title("Login")
    login_window.resizable(width=False, height=False)

    # Configuração de layout
    login_window.grid_rowconfigure((0, 10), weight=1)
    login_window.grid_columnconfigure((0, 4), weight=1)
    login_window.grid_rowconfigure(1, weight=2)

    # Frame para logo
    logo_frame = ctk.CTkFrame(login_window, fg_color="#F5F5F5", corner_radius=10)
    logo_frame.grid(row=0, column=0, rowspan=11, padx=10, pady=10, sticky="nswe")
    logo_frame.grid_rowconfigure((0, 10), weight=1)
    logo_frame.grid_columnconfigure(0, weight=1)

    # Adicionar imagem ao logo
    logo_image_path = r"C:\Users\miria\OneDrive\Área de Trabalho\mbk-email-mei-projeto\interface_grafica\logo_sem_fundo.jpg"
    logo_image = Image.open(logo_image_path)
    logo_ctk_image = ctk.CTkImage(light_image=logo_image, dark_image=logo_image, size=(150, 120))

    logo_label = ctk.CTkLabel(logo_frame, image=logo_ctk_image, text="") 
    logo_label.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", rowspan=3)

    # Título
    title_label = ctk.CTkLabel(
        login_window, text="PAINEL DE CONTROLE\nDE E-MAILS",
        font=("Bebas Neue", 24, "bold"), text_color="#3A3A3A"
    )
    title_label.grid(row=1, column=2, padx=20, pady=10, sticky="nswe")

    # Instruções para login
    instruction_label = ctk.CTkLabel(
        login_window, text="Faça Login para continuar:",
        font=("Roboto", 14), text_color="#5A5A5A", anchor="w"
    )
    instruction_label.grid(row=2, column=2, padx=20, pady=10, sticky="w")

    # Campos de entrada
    username_label = ctk.CTkLabel(
        login_window, text="Usuário:", font=("Roboto", 14), text_color="#5A5A5A", anchor="w"
    )
    username_label.grid(row=3, column=2, padx=20, pady=5, sticky="w")

    username_entry = ctk.CTkEntry(
        login_window, height=35, corner_radius=8, border_width=1, border_color="#D0D0D0", fg_color="#F9F9F9"
    )
    username_entry.grid(row=4, column=2, padx=20, pady=5, sticky="we")

    password_label = ctk.CTkLabel(
        login_window, text="Senha:", font=("Roboto", 14), text_color="#5A5A5A", anchor="w"
    )
    password_label.grid(row=5, column=2, padx=20, pady=5, sticky="w")

    password_entry = ctk.CTkEntry(
        login_window, height=35, corner_radius=8, border_width=1, border_color="#D0D0D0", fg_color="#F9F9F9", show="*"
    )
    password_entry.grid(row=6, column=2, padx=20, pady=5, sticky="we")

    # Feedback de validação
    feedback_label = ctk.CTkLabel(
        login_window, text="", font=("Roboto", 12), text_color="#5A5A5A", anchor="w"
    )
    feedback_label.grid(row=7, column=2, padx=20, pady=10, sticky="w")

    # Botão de login
    login_button = ctk.CTkButton(
        login_window, text="Entrar", font=("Roboto", 16, "bold"), fg_color="#800000",
        hover_color="#A52A2A", corner_radius=10, height=40,
        command=lambda: validate_login(username_entry, password_entry, feedback_label, login_window)
    )
    login_button.grid(row=8, column=2, padx=20, pady=20, sticky="we")

    login_window.mainloop()

# Inicializar o programa
create_login_window()
