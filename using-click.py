import click

@click.command()

@click.option('--greeting',help='Type your greets',default='How are you do')
@click.option('--name',default='Steve', help='Type your name')

def clickers(greeting,name):
    click_module=f'{greeting} {name}'
    print(click_module)

if __name__ == '__main__':
    clickers()

