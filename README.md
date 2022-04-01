# BATTLESHIPS


![Image of Battleships Welcome to Game](./assets/images/welcom-to-battleships.jpg)


This Battleship game is a Python terminal Game, which runs in the Code Institutemock terminal on Heroku.

Users can try and beat the computer by finding the computers hidden battleship before their shot(turns) have run out.
Each battleship occupies one(-) on the board. The user selcts a row number and column letter to target their shot.
A direct hit destroys 1 of 5 Battleships and and a turn is taken. If they miss they they still loose a turn and a chance to win the game.
when all 5 ships have sunk the user will win the game.

here iss a live version of the Python terminal game Battleship: **here iss a live version pf my project**
//insert multi device image of code //

## How to Play
Based on the classic Battleship board game.
The user is prompted with a choice of row and number to select coordinates to attack on the battle ground.
They cannot see where the ships are located on the hidden board but they make a choice on where to attack. 
If they miss the battle ship the board, it will mark a '0' on the user board.
If they hit the target the board will mark an 'X' on the user board.
The user is only allocated a limited amount of turns to make their choices to make it harder to find all the ships.
Every choice they make the user is deducted a turn.
If their turns runs out before they find all the ships, they loose and the game will restart.
If they find all 5 before their turns run out, they will then win the game.
## User Story

![Image flow of Features](./assets/images/user-story-flow.jpg)

We want to create an interactive guessing game written in Python where the user can choose where a battle ship may be hidden and attack it.
The challenge is that they only have a limited amount of turns in order to find all the hidden battle ships
* First we would need to create two boards. 
  * One would be hidden with the randomly delected 5 ships marked on the board.
  * The second would be visable and blank for the user to show were he has previously attached and where they have sunk battleships.

* The user would then be prompted to input a row and a number for the co-ordinates of where they would like to stike

* If it is a 'Direct Hit' where the user has selected the exact location of the randomaly generated location 
  * 'X' will be marked on the visable board 
  * -1 turn will be taken away from their total turns

* If the user has 'Missed' their target
  * a '0' will be marked on the visable board 
  * -1 turn will be taken away from their total turns

* If the incorrect data is inputed outside the scope of the board, an eroor will be displayed and the user will select a new location.

* If all 10 of the turns have been used up without finding all of the battle ships
  * The computer wins and the user looses

* When all 5 hidden ships have been hit
  * The User wins the game


## User Story Testing
* While testing if the games works, I chose to print() the hidden board so that I could see exaclt where the computer had randomly selected to put the battleships.

![Testing if the game works with showing Hidden board](./assets/images/test-game-show-hidden.jpg)

* When selecting the row and number for the co-ordinate of the attack we need to create a while not in statement to specify that only the numbers and letters in this range can be chosen otherwise the code cannot run because the location would not exist. 
* We also need to ensure that if the same location is inputed that it does not deduct a turn twice and the user is prompted to chosse a different location.
* We need to create a limit on how many times the user can guess on the hidden board by giving the user only 10 turns to guess the location.
* The game will end when all 5 ships have been found or all 10 turns have been used.
## Features
### Exisiting Features
* Board Generation
  * 5 random computer selected ship locations are marked on a hidden board 
  * The user will use one turn to guess where they are by selecting a number and letter
  * each guess they make deducts a turn from their total amount of turns, 10

![Opening blank board](./assets/images/welcom-to-battleships.jpg)

* GAme asks for user input of a row, number and a column, letter for the coordinates of the attack
  * KeyError is propted if the incorrect number or letter range is given and asks for correct input

![Insert correct Key for input](./assets/images/valid.jpg)

  * If the user has already stuck in the same location the computer will prompt a second selection because they hit in the same place, wothout them loosing a turn

![Input previously used](./assets/images/already-chosen.jpg)

* The inputs are then marked on the board with an 'X' and missed hits are marked with a '0'
* If all 5 ships are found before the users 10 turns have been used, the user is the winner

![Input previously used](./assets/images/winner.jpg)
### Further Features 
* Chose of how many turns avaiable 
* Chose of how many ships are hidden
* have ships larger than 1 block

# Testing
I have manually tested this project by doing the following:
* Passing the run.py file through a PEP8 linter and confirmed there are now no problems.
* Given invalid inputs: strings instead of integers, multiple inputs instead of single, out of bound inputs and the same input twice.
* Tested in my local terminal and the Code Instatute Heroku terminal
## Validator Testing
* PEP8

![PEP8 Validator testing with 16 errors](./assets/images/PEP8-results-16.jpg)

* When instering my python code into the PEP8 validator, there were several issues to deal with.
  * Trailing white space
  * Line too long
  * Insert 2 blank lines before the def

![PEP8 Validator testing with 0 errors](./assets/images/PEP8-results-0.jpg)


* After editing the errors in the validator
  * No errors were returned from PEP8online.com
## Bugs
* When I wrote the code, i had a lot of errors with white space becasue I could not see it when looking through my code, but when I put it through the PEP8 validator I was able to find them
* If a user inputs nothing and enters their row and column no input error arrises but after the input returns an error displayed in the terminal

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

## Deployment
This project was deplyed using Code Institue's mock terminal fo rHeroku.

* Steps for deployment:

  * Clone the repository 
  * Create a new Heroku app
When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`
  * Set the buildbacks to Python and NodeJS in that order
  * Link the Heroku appto the repository
  * Click on Deploy

## Credits 
* Code Institue for the deployment terminal
* Code Institue 'Sample README.md file' 
- (https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/)

* Wikipedia for details of the Battleship game
- (https://en.wikipedia.org/wiki/Battleship)
* 'guachilimbo' an examply of Python code of Battleship played in the terminal
- (https://github.com/guachilimbo/battleship/blob/main/Battleship.py/)

* Making a Python Battleship Game With Source Code
- (https://pythondex.com/python-battleship-game)