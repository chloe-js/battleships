![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

#BATTLESHIP
This Battleship game is a Python terminal Game, which runs in the Code Institutemock terminal on Heroku.

Users can try and beat the computer by finding the computers hidden battleship before their shot(turns) have run out.
Each battleship occupies one(-) on the board. The user selcts a row number and column letter to target their shot.
A direct hit destroys 1 of 5 Battleships and and a turn is taken. If they miss they they still loose a turn and a chance to win the game.
when all 5 ships have sunk the user will win the game.

here iss a live version of the Python terminal game Battleship: **here iss a live version pf my project**
//insert multi device image of code //

## How to Play

## Features
### Exisiting Features
* 
** 

## Data Model


## Testing

## Bugs
If a user inputs nothing and enters their row and column no input error arrises but after the input returns an error displayed in the terminal

## Validator Testing
* PEP8
**

## Deployment
This project was deplyed using Code Institue's mock terminal fo rHeroku.

* Steps for deployment:

** Clone the repository 
** Create a new Heroku app
** Set the buildbacks to Python and NodeJS in that order
** Link the Heroku appto the repository
** Click on Deploy

## Credits 
* Code Institue for the deployment terminal
* Code Institue 'Sample README.md file' 
//**  https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+PE_PAGPPF+2021_Q2/courseware/b3378fc1159e43e3b70916fdefdfae51/605f34e006594dc4ae19f5e60ec75e2e/ ***////
* Wikipedia for details of the Battleship game
* 'guachilimbo' an examply of Python code of Battleship played in the terminal
///// **** https://github.com/guachilimbo/battleship/blob/main/Battleship.py   ****//////



///////////////////////////////////////////////////////////////////////////////

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!