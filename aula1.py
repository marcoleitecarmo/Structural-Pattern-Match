# BASIC
# case 'batata': = if case == 'batata':
# case _: == else (default case)


def execute_command(command):
    match command:
        case 'ls':
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command('pwd')
