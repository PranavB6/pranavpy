import typer

app = typer.Typer()

@app.command()
def main(name: str = typer.Option(..., help="Your name")):
    """My awesome CLI tool."""
    typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()