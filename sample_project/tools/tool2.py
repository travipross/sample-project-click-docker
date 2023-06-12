import click

def command2(arga, argb):
    print(f"Command 2 executed with arga={arga}, argb={argb}")

@click.command()
@click.option("--arga")
@click.option("--argb")
def cmd2(arga, argb):
    command2(arga=arga, argb=argb)