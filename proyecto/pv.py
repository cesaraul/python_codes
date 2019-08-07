import click
from clients import commands as clients_commands

@click.group() # para indicar que es nuestro punto de entrada
@click.pass_context #crear contexto
def cli():
    pass


cli.add_commands(clients_commands.all)
