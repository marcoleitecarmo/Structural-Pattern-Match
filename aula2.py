# Commands in match
# match command_food.split(' '): # split two values
#     case ['like', food, ]: # get a literal and a variable

def execute_command(command):
    match command.split():
        case ['ls', path, *_]:
            print('$ listing files from', path)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


execute_command('ls')
execute_command('ls /home/ /Users /mais')
execute_command('cd /Users/')
