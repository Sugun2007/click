import click

@click.group()
def cli():
    pass

@cli.command()
@click.option("--name", prompt="Enter file name")
def file_creation(name):
    try:
        click.echo(f"Creating file: {name}")
        with open(name, "x") as file:
            pass
    except FileExistsError:
        click.echo("Error: File already exists")

@cli.command()
@click.option("--text", prompt="Enter text to be added")
def add_text(text):
    name = click.prompt("Enter file name with extension")
    try:
        with open(name, "a") as file:
            file.write(text + "\n")
        click.echo(f"Text added to {name}")
    except FileNotFoundError:
        click.echo("Error: File does not exist")

if __name__ == "__main__":
    cli()
