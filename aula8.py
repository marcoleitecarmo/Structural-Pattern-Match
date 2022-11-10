# With dicts
# case {'name': _, 'last': 'Doe'}:
# case {'name': 'Otávio' as name, 'last': 'Doe'} as data:


def execute_command(command):
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            print('Deu match')
            for directory in command['directories']:
                print('$ listing ALL directories from', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command({'command': 'ls', 'directories': []})
execute_command('ls /one/')
