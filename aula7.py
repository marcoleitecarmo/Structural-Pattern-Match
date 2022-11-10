# With generic placeholders
# case ['A', 'B', _, _]:
# case ['A', 'B', _, _, *_, 'Z']:


def execute_command(command):
    match command.split():
        case ['ls' | 'list', _, *directories, _]:
            for directory in directories:
                print('$ listing ALL directories from', directory)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command('ls /home/ /Users /mais')
execute_command('ls /one/')
