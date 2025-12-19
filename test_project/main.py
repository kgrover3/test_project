from rich import print
from test_project.utils.http_client import get_json

def main():
    print("[bold green]Hello from your first pyenv project[/bold green]")

    try:
        data = get_json("https://httpbin.org/json")
        print(data)
    except RuntimeError as err:
        print(f"[bold red]Error:[/bold red] {err}")

if __name__ == "__main__":
    main()
