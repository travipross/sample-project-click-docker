import click 
from sample_project.tools import cmd1, cmd2, cmd3

@click.group()
def cli():
    print("Parent CLI command executed")

cli.add_command(cmd1)
cli.add_command(cmd2)
cli.add_command(cmd3)
