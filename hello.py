import click
@click.command()
def hello():
    click.echo("hello cli")

if __name__=="__main__":
    hello()