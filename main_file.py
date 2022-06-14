if __name__ == '__main__':
    pass

from file_functions import *

file_name = "Score"
file_number = 0

file_name, file_number = process_file(file_name, file_number)


terminate_program = False
while not terminate_program:
    print('\n_________________________Entry_________________________\n'
          '\nType "1" to play'
          '\nType "2" to see the score'
          '\nType "3" to create a new score'
          '\nType "4" to use an existing score file'
          '\nType "5" to see a player total data'
          '\nType "6" to exit')

    try:
        main_var = int(input("\nWhat do you want to do?: "))

        if main_var < 1 or main_var > 6:
            raise unexpected_input("Does not match any of the options")

    except:
        print("\nEnter a number according to the operation you want")

    else:
        if main_var == 1:
            start_game(file_name, file_number)

        elif main_var == 2:
            show_score(file_name, file_number)

        elif main_var == 3:
            file_name = input("\nGive the new score a filename: ")
            file_name = file_name.replace(" ", "_")
            file_number = 0

            file_name, file_number = create_file(file_name, file_number)

        elif main_var == 4:
            file_name, file_number = use_existing_file(file_name, file_number)

        elif main_var == 5:
            summarize_player(file_name, file_number)

        elif main_var == 6:
            terminate_program = True
