import click
@click.command()
@click.option('--count', default=1, help="number of greetings")
@click.option('--name', prompt="your name   ", help="type your name")
def options(name, count):
    for i in range(0,count):
        click.echo(f"hello, {name}")

if __name__=="__main__":
    options()