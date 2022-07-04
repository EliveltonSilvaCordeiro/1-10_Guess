# 1-10_Guess
![1-10 Guess Logo (3)](https://user-images.githubusercontent.com/105513033/177086025-00f17591-46c1-480a-aba0-98a7554992ca.png)

<span>
  <img src="https://img.shields.io/badge/STATUS-FINISHED-success" alt="Status: Finalizado">
  <img src="https://img.shields.io/badge/RELEASE_DATA-JUNE%202022-informational" alt="Release Data: June 2022">
  <img src="https://img.shields.io/badge/LICENCE-NONE-important" alt="LICENCE: NONE">
</span>

&nbsp;

This program is a game where the user tries to guess a number between 1 to 10, the base functions depends of the random and datetime libraries and a self created file, this project was made with intention of colecting my friends play data to aproximate their luck.

## :hammer: Funcionalidades do projeto

- `start_game` : This function is the own game, it asks for a player name and collect the data of the attempts saving it in a csv file

- `show_score` : Shows the score in a ranking based in 6 types of data collected in the game

- `create_file` : Creates a new file that can be named, blank spaces are replaced by underlines ( _ )

- `use_existing_file` : Use a pre-existing file that was created in past games, using any other kind of file will result in errors

- `summarize_player` : Write the name of one player, to see their total data for all their games and their winning chances
