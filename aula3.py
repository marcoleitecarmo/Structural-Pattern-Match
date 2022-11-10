# Case with or inside a list
# case ['enjoy' | 'love', food]:


def execute_command(command):
    match command.split():
        case ['ls' | 'list', path, *_]:
            print('$ listing files from', path)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command('ls /home/ /Users /mais')
execute_command('list /home/ /Users /mais')
