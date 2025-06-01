# 💼 Sistema de Ferramentaria com CustomTkinter

Este projeto consiste em uma aplicação desktop para controle de ferramentas e empréstimos, desenvolvida com **Python** e a biblioteca **CustomTkinter**, utilizando **SQLite** como banco de dados local.

## 🎯 Objetivo

Fornecer uma interface moderna, funcional e leve para o controle de empréstimo de ferramentas, voltada para uso em ambientes de manutenção, ferramentarias e almoxarifados.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **SQLite**
- **CustomTkinter** – Interface gráfica moderna
- **Tkinter padrão** (com melhorias do CustomTkinter)

---

## 🌙 Interface Inicial

A interface possui os seguintes elementos:

### `set_appearance_mode("dark")`

Define o modo de aparência:

- `"dark"` → Modo escuro (padrão)
- `"light"` → Modo claro
- `"system"` → Acompanha o sistema operacional

### `set_default_color_theme("blue")`

Define o tema de cor principal:

- `"blue"` (padrão)
- `"green"`
- `"dark-blue"`

### Janela Principal

```python
self.title("Sistema de Ferramentaria")
self.geometry("600x400")
self.resizable(False, False)
```
