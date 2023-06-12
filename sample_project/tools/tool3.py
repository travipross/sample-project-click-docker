import click

def command3(argx, argxx):
    print(f"Command 3 executed with argx={argx}, argxx={argxx}")

@click.command()
@click.option("--argx")
@click.option("--argxx")
def cmd3(argx, argxx):
    command3(argx=argx, argxx=argxx)