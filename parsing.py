import sys

def user_greeting(greeting,name):
    pesan = f'{greeting} {name}'
    print(pesan)

if __name__ == '__main__':
    greeting='Hello'
    name='User'

    if '--help' in sys.argv:
        help_message = f'Usage :  {sys.argv[0]} --name {name} --greeting {greeting}'
        print(help_message)
        sys.exit()
# +1 mean for index input 1 [a word after --name]
    if '--name' in sys.argv:
        name_index=sys.argv.index('--name') + 2
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

# +1 mean for index input 1 [a word after --greeting]
    if '--greeting' in sys.argv:
        greeting_index=sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]
            
user_greeting(greeting,name)