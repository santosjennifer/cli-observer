# dx-observe

**dx-observe** é uma CLI escrita em Python focada em **observabilidade local**, permitindo analisar, filtrar e visualizar arquivos de log no formato **JSONL**.

O objetivo é facilitar o trabalho de Developer Experience e engenheiros que lidam diariamente com logs durante debugging ou desenvolvimento.

---

## 🚀 Funcionalidades

- **Pretty-print** estilizado para logs JSONL (usando `rich`)
- **Stats**: estatísticas rápidas dos logs
- **Filter**: filtragem por nível ou trecho de texto
- Suporte a arquivos grandes (streaming linha a linha)
- CLI construída com **Typer**

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/santosjennifer/cli-observer.git
```

### 2. Instale e ative o ambiente com Poetry

```bash
poetry install
poetry env activate
```

### ▶️ Como executar

Você pode rodar qualquer comando assim:

```bash
poetry run dx-observe <comando> [args]
```

```bash
poetry run dx-observe --help
```

### 📌 Comandos Disponíveis

#### 🖼️ pretty
Exibe logs JSONL com formatação amigável.

```bash
poetry run dx-observe pretty example.jsonl
```

#### 📊 stats
Mostra estatísticas básicas sobre o arquivo:

```bash
poetry run dx-observe stats example.jsonl
```

#### 🔎 filter
Filtra logs por nível ou texto dentro da mensagem.

```bash
poetry run dx-observe filter example.jsonl --level INFO
poetry run dx-observe filter example.jsonl --contains=failed
poetry run dx-observe filter example.jsonl --contains timeout
```