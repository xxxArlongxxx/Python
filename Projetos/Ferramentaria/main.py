import customtkinter as ctk
import sqlite3

# Configurações iniciais da aparência
ctk.set_appearance_mode("dark")  # "dark", "light" ou "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"


def connect_db():
    """Conecta ao banco SQLite e ativa foreign keys."""
    conn = sqlite3.connect('ferramentaria.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def criar_banco():
    """Cria tabelas do banco de dados, seguindo as três formas normais."""
    with connect_db() as conn:
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ferramentas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                codigo TEXT UNIQUE NOT NULL,
                descricao TEXT,
                disponivel INTEGER DEFAULT 1
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pessoas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                email TEXT UNIQUE,
                telefone TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emprestimos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_ferramenta INTEGER NOT NULL,
                id_pessoa INTEGER NOT NULL,
                data_emprestimo TEXT NOT NULL,
                data_devolucao TEXT,
                FOREIGN KEY (id_ferramenta) REFERENCES ferramentas(id),
                FOREIGN KEY (id_pessoa) REFERENCES pessoas(id)
            )
        ''')

        conn.commit()


class FerramentariaApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Ferramentaria")
        self.geometry("800x500")
        self.resizable(False, False)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_rowconfigure(5, weight=1)

        self.btn_home = ctk.CTkButton(
            self.sidebar, text="Início", command=self.show_home)
        self.btn_cadastrar_ferramenta = ctk.CTkButton(
            self.sidebar, text="Cadastrar Ferramenta", command=self.show_cadastrar_ferramenta)
        self.btn_emprestimo = ctk.CTkButton(
            self.sidebar, text="Solicitar Empréstimo", command=self.show_emprestimo)
        self.btn_cadastrar_pessoa = ctk.CTkButton(
            self.sidebar, text="Cadastrar Pessoa", command=self.show_cadastrar_pessoa)

        self.btn_home.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.btn_cadastrar_ferramenta.grid(
            row=1, column=0, padx=20, pady=10, sticky="ew")
        self.btn_emprestimo.grid(
            row=2, column=0, padx=20, pady=10, sticky="ew")
        self.btn_cadastrar_pessoa.grid(
            row=3, column=0, padx=20, pady=10, sticky="ew")

        # Container para as telas
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.frames = {}
        for F in (HomeScreen, CadastrarFerramentaScreen, SolicitarEmprestimoScreen, CadastrarPessoaScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_home()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_home(self):
        self.show_frame("HomeScreen")

    def show_cadastrar_ferramenta(self):
        self.show_frame("CadastrarFerramentaScreen")

    def show_emprestimo(self):
        self.show_frame("SolicitarEmprestimoScreen")

    def show_cadastrar_pessoa(self):
        self.show_frame("CadastrarPessoaScreen")


class HomeScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Bem-vindo ao Sistema de Ferramentaria",
                             font=ctk.CTkFont(size=20, weight="bold"))
        label.pack(pady=100)


class CadastrarFerramentaScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Cadastrar Ferramenta (Em desenvolvimento)",
                             font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(pady=100)


class SolicitarEmprestimoScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Solicitar Empréstimo (Em desenvolvimento)",
                             font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(pady=100)


class CadastrarPessoaScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ctk.CTkLabel(self, text="Cadastro de Pessoas",
                             font=ctk.CTkFont(size=18, weight="bold"))
        label.pack(pady=20)

        self.nome_entry = ctk.CTkEntry(self, placeholder_text="Nome")
        self.nome_entry.pack(pady=10, fill="x", padx=50)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="E-mail")
        self.email_entry.pack(pady=10, fill="x", padx=50)

        self.telefone_entry = ctk.CTkEntry(self, placeholder_text="Telefone")
        self.telefone_entry.pack(pady=10, fill="x", padx=50)

        self.status_label = ctk.CTkLabel(self, text="", text_color="red")
        self.status_label.pack(pady=10)

        btn_salvar = ctk.CTkButton(
            self, text="Salvar Pessoa", command=self.salvar_pessoa)
        btn_salvar.pack(pady=10)

    def salvar_pessoa(self):
        nome = self.nome_entry.get().strip()
        email = self.email_entry.get().strip()
        telefone = self.telefone_entry.get().strip()

        if not nome:
            self.status_label.configure(
                text="O nome é obrigatório.", text_color="red")
            return

        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pessoas (nome, email, telefone) VALUES (?, ?, ?)",
                           (nome, email, telefone))
            conn.commit()
            conn.close()

            self.status_label.configure(
                text="Pessoa cadastrada com sucesso!", text_color="green")
            self.nome_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.telefone_entry.delete(0, "end")

        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: pessoas.nome" in str(e):
                self.status_label.configure(
                    text="Nome já cadastrado.", text_color="red")
            elif "UNIQUE constraint failed: pessoas.email" in str(e):
                self.status_label.configure(
                    text="E-mail já cadastrado.", text_color="red")
            else:
                self.status_label.configure(
                    text="Erro no cadastro.", text_color="red")


if __name__ == "__main__":
    criar_banco()
    app = FerramentariaApp()
    app.mainloop()
