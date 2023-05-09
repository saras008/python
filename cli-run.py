import click

@click.group()
def cli():
    pass

@click.group(help='Worker related commands')
def workers():
    pass
#register workers group as a command
cli.add_command(workers)

@workers.group(help='Spawn new worker')


def worker():
    worker_name = 'Main worker'
    print(f"{worker_name} is now spawning")

@workers.command(help="list all the workers")

def list_worker():
    workers_list=['alpha','bravo','omega']
    print(f"Workers: {','.join(workers_list)}")

@cli.command(help='Talk to worker')
@click.option('--greeting', default='Whats up bro?',help='Greeting from admin')
@click.argument('name')

def admins(greeting,name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    cli()
