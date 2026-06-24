import typer

app = typer.Typer()

@app.command()
def main(name: str = typer.Option(..., help="Your name")):
    """My awesome CLI tool."""
    
    if "pranav" == name.lower():
        typer.echo("""
        ██████  ██████   █████  ███    ██  █████  ██    ██ 
        ██   ██ ██   ██ ██   ██ ████   ██ ██   ██ ██    ██ 
        ██████  ██████  ███████ ██ ██  ██ ███████ ██    ██ 
        ██      ██   ██ ██   ██ ██  ██ ██ ██   ██  ██  ██  
        ██      ██   ██ ██   ██ ██   ████ ██   ██   ████   
        """)
    
    typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()