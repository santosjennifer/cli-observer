from __future__ import annotations
import json
from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel

app = typer.Typer(help="dx-observe: Ferramenta para observar logs localmente")
console = Console()

@app.command()
def version():
    """Mostra a versão da CLI"""
    console.print("[bold green]dx-observe v1.0.0[/]")

@app.command()
def pretty(
    file: Path = typer.Argument(..., exists=True, readable=True, help="Arquivo de logs (JSONL)")
):
    """
    Pretty-print para um arquivo JSONL.
    """
    try:
        with file.open("r", encoding="utf-8") as f:
            for line_no, raw in enumerate(f, start=1):
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError:
                    console.print(f"[yellow]Linha {line_no}: JSON inválido — pulando[/]")
                    continue
                level = data.get("level", "INFO").upper()
                msg = data.get("message", "")
                ts = data.get("timestamp", "-")
                border = "green" if level == "INFO" else "red" if level == "ERROR" else "yellow"
                console.print(Panel(f"[bold]{level}[/]\n{msg}", title=str(ts), border_style=border))
    except Exception as exc:
        console.print(f"[red]Erro ao processar o arquivo:[/] {exc}")
        raise typer.Exit(code=1)
    

@app.command()
def stats(
    file: Path = typer.Argument(..., exists=True, readable=True, help="Arquivo de logs (JSONL)")
):
    """
    Mostra estatísticas básicas dos logs.
    """
    total = 0
    levels = {}
    keys = {}

    try:
        with file.open("r", encoding="utf-8") as f:
            for raw in f:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError:
                    continue

                total += 1

                lvl = data.get("level", "UNKNOWN")
                levels[lvl] = levels.get(lvl, 0) + 1

                for k in data.keys():
                    keys[k] = keys.get(k, 0) + 1

        console.rule("[bold blue]Stats[/]")

        console.print(f"[bold]Total linhas:[/] {total}")

        console.print("\n[bold]Por nível:[/]")
        for lvl, count in levels.items():
            console.print(f"  - {lvl}: {count}")

        console.print("\n[bold]Chaves mais comuns:[/]")
        for k, count in sorted(keys.items(), key=lambda x: x[1], reverse=True):
            console.print(f"  - {k}: {count}")

        console.rule()

    except Exception as exc:
        console.print(f"[red]Erro ao processar o arquivo:[/] {exc}")
        raise typer.Exit(code=1)
    

@app.command()
def filter(
    file: Path = typer.Argument(..., exists=True, readable=True, help="Arquivo de logs (JSONL)"),
    level: str = typer.Option(None, help="Filtrar por nível (INFO, ERROR, etc)"),
    contains: str = typer.Option(None, help="Filtrar logs que contenham este texto"),
):
    """
    Filtra o JSONL por nível ou texto contido.
    """
    try:
        with file.open("r", encoding="utf-8") as f:
            for raw in f:
                raw = raw.strip()
                if not raw:
                    continue

                try:
                    data = json.loads(raw)
                except json.JSONDecodeError:
                    continue

                if level and data.get("level") != level:
                    continue

                if contains and contains.lower() not in json.dumps(data).lower():
                    continue

                console.print_json(data=data)

    except Exception as exc:
        console.print(f"[red]Erro ao processar o arquivo:[/] {exc}")
        raise typer.Exit(code=1)

    
if __name__ == "__main__":
    app()
