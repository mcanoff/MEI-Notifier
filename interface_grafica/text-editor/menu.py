import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

class Menu:
    def __init__(self, windows, ai_settings, text_write, status_bar, toolbar):
        # Inheritance
        self.root = windows                         # Janela principal
        self.ai_settings = ai_settings            # Um objeto para gerenciar configurações do aplicativo
        self.text_write = text_write               # Um editor de texto embutido na interface
        self.statusbar = status_bar               # Barra de status
        self.tool_bar_show = toolbar            # Barra de ferramentas

        # Menu configuration
        self.menu = ctk.CTkMenu(self.root)  # Cria o menu principal e associa ele à janela
        self.root.configure(menu=self.menu)

        # File Menu
        file_menu = ctk.CTkMenu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Arquivo", menu=file_menu)
        
        # Comandos do menu de Arquivo
        file_menu.add_command(label="Novo", command=self.new_file)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Salvar", command=self.save_file)
        file_menu.add_command(label="Salvar Como", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.exit_program)

        # Edit Menu
        edit_menu = ctk.CTkMenu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Editar", menu=edit_menu)
        
        # Comandos do menu de Editar
        edit_menu.add_command(label="Copiar", command=self.copy_text)
        edit_menu.add_command(label="Colar", command=self.paste_text)
        edit_menu.add_command(label="Cortar", command=self.cut_text)
        edit_menu.add_command(label="Limpar Tudo", command=self.clear_text)

    # Funções para os comandos do menu
    def new_file(self):
        self.text_write.delete(1.0, ctk.END)
        self.statusbar.config(text="Novo arquivo criado.")
    
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text_write.delete(1.0, ctk.END)
                self.text_write.insert(1.0, file.read())
            self.statusbar.config(text=f"Arquivo aberto: {file_path}")
    
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_write.get(1.0, ctk.END))
            self.statusbar.config(text=f"Arquivo salvo: {file_path}")
    
    def save_as_file(self):
        self.save_file()

    def exit_program(self):
        self.root.quit()

    def copy_text(self):
        self.text_write.clipboard_clear()
        self.text_write.clipboard_append(self.text_write.get(1.0, ctk.END))
        self.statusbar.config(text="Texto copiado.")
    
    def paste_text(self):
        text = self.text_write.clipboard_get()
        self.text_write.insert(ctk.END, text)
        self.statusbar.config(text="Texto colado.")
    
    def cut_text(self):
        self.copy_text()
        self.text_write.delete(1.0, ctk.END)
        self.statusbar.config(text="Texto cortado.")
    
    def clear_text(self):
        self.text_write.delete(1.0, ctk.END)
        self.statusbar.config(text="Texto apagado.")