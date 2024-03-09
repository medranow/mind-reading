# Mind Reading Math Tricks

### Video Demo: (https://youtu.be/9czsqn1N8Sk)

This is my final project for CS50's Programming with Python. I named it "Mind Reading Math Tricks." The program prompts you to learn or, if you prefer, to play three different math tricks you might have encountered at some point in you life. 

The program was written exclusively in python because of its flexibility and code friendly structure.

In terms of the structure of the program, it requires a series of inputs from the user to work. For this reason, I decided to create a `class Number` that initializes with a variable `number `. The purpose of the class is to simplify the code to be used for each function that will perform a math trick. A `@classmethod` was used to obtain the first input that initializes the game and code defensevely against the user giving an input that was not an interger or a number not displayed on the screen.

The program calls for a `main()` function. `main` in turn contains three functions for each of the math tricks the user can select to play. For the user to select a trick, we abstract the instruction through the function `get_trick()`. `get_trick()` asks for input from the user to select a math trick to play and raises exceptions if the user inputs a string or a trick that does not show on the screen. 

The functions are very simple. They construct an object of the `class Number` by calling its method `get()` to obtain a number between 1 and 10 to start the game. Next, a series of inputs are asked with cues as to what math operation the user must calculate in order for the game to work. In the end, the user is giving a drum rolling with emojis with the result he should have solved.