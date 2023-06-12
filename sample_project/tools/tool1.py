import click

def command1(arg1, arg2):
    print(f"Command 1 executed with arg1={arg1}, arg2={arg2}")

@click.command()
@click.option("--arg1")
@click.option("--arg2")
def cmd1(arg1, arg2):
    command1(arg1=arg1, arg2=arg2)