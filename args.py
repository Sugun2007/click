import click
@click.command()
@click.argument("name")
def args(name):
    click.echo(f"heyya {name}")

if __name__=="__main__":
    args()