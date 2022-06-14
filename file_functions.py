if __name__ == '__main__':
    pass

"""
user cannot access this function
it was made for registering the time of the game
it is only used when the user plays the game
"""


def time_register(start, finish):
    from datetime import datetime

    start = start.strftime("%H.%M.%S")
    finish = finish.strftime("%H.%M.%S")

    time_1 = datetime.strptime(start, "%H.%M.%S")
    time_2 = datetime.strptime(finish, "%H.%M.%S")

    return time_2 - time_1


"""
user cannot access this function
it was made for sum up the user's playtime in the game 
it is used in the last function
"""


def time_sum(play_time, add_time):
    import datetime as dt

    time_1 = dt.datetime.strptime(str(play_time), "%H:%M:%S")

    (h, m, s) = add_time.split(":")
    time_2 = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

    play_time = (time_1 + time_2).time()

    return play_time


"""
creates a new file, takes base of the two variables, "file_name" and "file_number"
if another file with the same name and number exists it will add 1 to the "file_number" and search again
if no file with the same name and number exists, it will create a new file
"""


def create_file(file_name, file_number):
    file_check = False
    while not file_check:

        try:
            with open(f"{file_name} ({file_number}).csv", "x") as score_table:
                score_table.write("Players,"
                                  "Attempts,"
                                  "Time,"
                                  "Close,"
                                  "Almost,"
                                  "Missed,"
                                  "Errors\n")

        except:
            file_number += 1

        else:
            print(f'\nThe file "{file_name} ({file_number}).csv" will store new scores')
            return file_name, file_number


"""
this function is for the user search and use for an existing file
the option of giving up is given if there is error
in this case happen it will make use of the "create_file" function
"""


def use_existing_file(file_name, file_number):
    check_existing_file = False
    print("\nFirst enter the filename, then the number in parentheses")

    while not check_existing_file:
        file_name = input("\n_______________________________________________________\n\nEnter the filename: ")

        try:
            file_number = int(input("\nNow enter the file's number: "))

        except:
            print("\nUse the number in parentheses after the filename")
            try_again = input("\nDo you want to try again? Y or N?: ").upper()

            if try_again == "YES" or try_again == 'Y':
                check_existing_file = False

            else:
                file_name = "Score"
                file_number = 0

                return create_file(file_name, file_number)

        else:

            try:
                open(f"{file_name} ({file_number}).csv", "r")

            except:
                print("\nFile does not exist")
                try_again = input("\nDo you want to try again? Y or N?: ").upper()

                if try_again == "YES" or try_again == 'Y':
                    check_existing_file = False

                else:
                    file_name = "Score"
                    file_number = 0

                    return create_file(file_name, file_number)

            else:
                print(f'\nThe file "{file_name} ({file_number}).csv" will store more scores')
                return file_name, file_number


"""
this function was made to make make the user choice the file
it only activates at the start of the program
that's because there needs to be a file in order to use the other functions
"""


def process_file(file_name, file_number):
    print("Welcome to the 1-10 Guess program, before starting\n"
          '\nType "1" to continue normally'
          '\nType "2" to use an existing score file')

    confirm_file_process = False

    while not confirm_file_process:

        try:
            initial_input = int(input("\nWhich option will be?: "))

            if initial_input < 1 or initial_input > 2:
                raise unexpected_input("Number does not match any of the options")

        except:
            print("\nEnter 1 or 2")

        else:
            if initial_input == 1:
                return create_file(file_name, file_number)

            if initial_input == 2:
                return use_existing_file(file_name, file_number)


"""
this function is the own game
it makes use of "random.randint" function to make the random number
it ask for a player name and collect the data of the attempts
"""


def start_game(file_name, file_number):
    player = input("\n_________________________Play!_________________________\n\nEnter the player's name: ")

    from random import randint
    from datetime import datetime

    random_number = 1

    user_attempts = 0
    user_errors = 0
    random_close = 0
    random_almost = 0
    random_missed = 0

    print('\nIf you want to give up, type "-1"')

    start = datetime.now()

    while random_number != 0:

        guesses = 10
        random_number = randint(1, guesses)
        user_attempts += 1

        try:
            user_attempt = int(input(f"\n________________________Attempt {user_attempts}________________________"
                                     f"\n\nEnter a number from 1 to 10: "))

            if user_attempt < 1 and user_attempt != -1 or user_attempt > 10:
                raise unexpected_input("Only numbers from one to ten")

        except:
            print("\nUse only integers from one to ten")
            user_errors += 1

        else:

            if user_attempt == -1:
                random_number = 0

            elif random_number == user_attempt:
                finish = datetime.now()
                play_time = time_register(start, finish)

                print(f"\nThe number was {random_number}!\nYou Won!\n"
                      f"\nPlay Time: {play_time}\n"
                      f"\nThere was an error:       {user_errors} times"
                      f"\nGot close:                {random_close} times"
                      f"\nAlmost won:               {random_almost} times"
                      f"\nMissed it:                {random_missed} times")

                with open(f"{file_name} ({file_number}).csv", "a") as score_table:
                    score_table.write(f"{player},"
                                      f"{user_attempts},"
                                      f"{play_time},"
                                      f"{user_errors},"
                                      f"{random_close},"
                                      f"{random_almost},"
                                      f"{random_missed}\n")

                random_number = 0

            else:
                if user_attempt - 1 == random_number or user_attempt + 1 == random_number:
                    print(f"\nThe number was {random_number}!\nClose!")
                    random_close += 1

                elif user_attempt - 2 == random_number or user_attempt + 2 == random_number:
                    print(f"\nThe number was {random_number}!\nAlmost There!")
                    random_almost += 1

                else:
                    print(f"\nThe number was {random_number}!\nMissed it!")
                    random_missed += 1


"""
this function shows the score in a rank based in 6 data collect in the game
"All Attempts", "Play Time", "Errors", "Close Attempts", "Almost Attempts" and "Missed Attempts"
all these, ordered by each condition respectively
"""


def show_score(file_name, file_number):
    count_order = 0
    records = []

    with open(f"{file_name} ({file_number}).csv", "r") as score_table:
        lines = score_table.readlines()

        for line in lines[1:len(lines)]:
            line = line.split(",")

            records.append([line[0], line[1], line[2], line[3], line[4], line[5], line[6]])

        score_table.close()

    def attempts(store):
        return int(store[1])

    def play_time(store):
        return int(store[2])

    def errors(store):
        return int(store[3])

    def close(store):
        return int(store[4])

    def almost(store):
        return int(store[5])

    def missed(store):
        return int(store[6])

    set_order = sorted(records, key=missed and almost and close and errors and play_time and attempts)

    print('\n_________________________Score_________________________\n')

    if len(set_order) > 3:
        print("\nPodium")

        for order in set_order[0:3]:
            count_order += 1

            print(f"\n{count_order}° {order[0]} \n\n"
                  f"Attempts:  {order[1]}   \n"
                  f"Play Time: {order[2]} \n\n"
                  f"Errors:    {order[3]}   \n"
                  f"Close:     {order[4]}   \n"
                  f"Almost:    {order[5]}   \n"
                  f"Missed:    {order[6]}   \n")

        print("\n_______________________________________________________\n")

        print("\nPlayers")
        for order in set_order[3:len(set_order)]:
            count_order += 1

            print(f"\n{count_order}° {order[0]} \n\n"
                  f"Attempts:  {order[1]}   \n"
                  f"Play Time: {order[2]} \n\n"
                  f"Errors:    {order[3]}   \n"
                  f"Close:     {order[4]}   \n"
                  f"Almost:    {order[5]}   \n"
                  f"Missed:    {order[6]}   \n")

    else:
        for order in set_order:
            count_order += 1

            print(f"\n{count_order}° {order[0]} \n\n"
                  f"Attempts:  {order[1]}   \n"
                  f"Play Time: {order[2]} \n\n"
                  f"Errors:    {order[3]}   \n"
                  f"Close:     {order[4]}   \n"
                  f"Almost:    {order[5]}   \n"
                  f"Missed:    {order[6]}   \n")


"""
This function sum up all the data of a single player and shows it
and also have a formula to approximate the player's luck:
All Attempts multiplied by the chances of winning (10%) divided by the number of different plays
Resulting in the user's chances of not guessing it right, that, minus 100, completes the formula
"""


def summarize_player(file_name, file_number):
    finish_checking = False
    while not finish_checking:

        order = 0

        play_counter = 0

        play_time = "0:00:00"

        user_attempts = 0
        user_errors   = 0
        random_close  = 0
        random_almost = 0
        random_missed = 0

        with open(f"{file_name} ({file_number}).csv", "r") as score_table:
            score = score_table.readlines()

            print("\n_______________________________________________________\n")

            print("\nRegister of the Score:\n")

            for game_register in score[1:len(score)]:
                game_register = game_register.split(",")

                order += 1

                print(f"{order}° Play: {game_register[0]}\n")

            print("\n_______________________________________________________\n")

            search_for = input("\nView total data of which player?: ")

            for game_register in score[1:len(score)]:
                game_register = game_register.split(",")

                if game_register[0] == search_for:
                    play_counter += 1

                    play_time = time_sum(play_time, game_register[2])

                    user_attempts += int(game_register[1])
                    user_errors   += int(game_register[3])
                    random_close  += int(game_register[4])
                    random_almost += int(game_register[5])
                    random_missed += int(game_register[6])

            score_table.close()

        if user_attempts != 0:
            print(f"\nPlayer {search_for} results in {play_counter} plays:\n\n"
                  f"Attempts:   {user_attempts} \n"
                  f"Play Time:  {play_time}   \n\n"
                  f"Errors:     {user_errors}   \n"
                  f"Close:      {random_close}  \n"
                  f"Almost:     {random_almost} \n"
                  f"Missed:     {random_missed} \n")

            print(f'Approximately, "{search_for}" chances in guessing a random number of 1-10 are of: ')
            print(f'\n{100 - user_attempts / play_counter * 1.1:.2f}%')

            if user_errors > 0:

                print(f'Without counting "{search_for}" errors, the chances are of: ')
                print(f"{100 - (user_attempts - user_errors) / play_counter * 1.1:.2f}%\n")

            search_again = input("\nSee results of another player? Y or N?: ").upper()

            if search_again == "YES" or search_again == 'Y':
                finish_checking = False

            else:
                finish_checking = True

        else:
            print(f'\nThere is no player with the name of "{search_for}"')
            search_again = input("\nSee results of a player? Y or N?: ").upper()

            if search_again == "YES" or search_again == 'Y':
                finish_checking = False

            else:
                finish_checking = True
