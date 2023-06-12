import click 
from sample_project.tools import command1, command2, command3

@click.group()
def cli():
    print("Parent CLI command executed")

@cli.command()
@click.option("--arg1")
@click.option("--arg2")
def cmd1(arg1, arg2):
    command1(arg1=arg1, arg2=arg2)

@cli.command()
@click.option("--arga")
@click.option("--argb")
def cmd3(arga, argb):
    command2(arga=arga, argb=argb)

@cli.command()
@click.option("--argx")
@click.option("--argxx")
def cmd3(argx, argxx):
    command3(argx=argx, argxx=argxx)