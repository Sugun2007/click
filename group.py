import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('filename')
def init(filename):
    click.echo(f"Creating presentation: {filename}")

@cli.command()
@click.argument('slide_content')
def add(slide_content):
    click.echo(f"Adding slide: {slide_content}")

if __name__ == "__main__":
    cli()
