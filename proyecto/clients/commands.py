import click

@click.group()# combierte a la funcion clients en otro decorador
def clients():
    """Manages the clients lifecycle"""
    pass

@clients.command()
@click.pass_context
def create(ctx,name,company,email,position):
    """create a new client"""
    pass


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""

    pass


@clients.command()
@click.pass_context
def update(ctx,clien_uid):
    """Updates a client"""
    pass

@clients.command()
@click.pass_context
def delete(ctx,cliend_uid):
    """Deletes a client"""
    pass

all = clients # alias , la variable apunta a la cuncion clients 
