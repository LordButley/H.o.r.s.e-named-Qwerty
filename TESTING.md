# Testing

 ## Python

 - No errors were returned when passing through http://pep8online.com/. 

## User Stories Testing
1. As a user visiting the site for the first time, I want to navigate the site intuitively.
    * A user is greeted on the home page with a menu and clear instructions on how to navigate 
    * A how to play page is signposted from the second you start the application
    * There are descriptions through out of the buttons required to press.
    * There is exception handling throughout catching incorrect input
2. As a user visiting the site for the first time, I want to play the game quickly and easily.
    * A user can start a game as within a minute after giving their name and choosing the type of quiz
    * Once the game is set up, playing the typing game is simply typing in the words.
3. As a user, I want to be provided with feedback such as correct answers.
    * All input that is incorrect is fed back to the user and asked to try again.
    * Whilst playing the quiz, the score and lives are shown and updated after each question
    * After entering your name, the console will say hi then your name
4. As a user, I want to be able to choose a theme of questions.
    * A user can easily choose the theme of the questions.
5. As a user, I want to be able to set the difficulty of the quiz
    * A user is able to choose whether to play the game in easy, normal or hard.
    * An explanation of the effect the difficulty has on the game is given when choosing the difficulty and also in the how to play section 
6. As a user, I want the questions to be randomised to keep the game interesting.
    * The answers are randomised so each time you play, they appear in a different order
    * There are enough answers that you cannot get to the end of the set in one game
    * Questions cannot be repeated in a single game
7. As a user, I do not want to break the program by putting in unexpected inputs
    * All inputs are checked and fed back to the user if they are unexpected.


## Manual Testing 

I have robustly testing the application completing the following actions:

* Navigation - Repeated steps on all pages
    * Enter the corresponding number for each section on the menu to see if it directs to the right page.
    * Complete the above check on each page of the game to see if their are any glitches that are page specific.
    * Check that exitting the game works as expected.
    
* Input and error handling - Repeated steps on all input sections.
    * Enter values which do not correspond to menu items.
    * Enter no value at all.

* Quiz
    * Check that the score counter counts correctly.
    * Check that the game times out correctly.
    * Check that the correct score is presented after the quiz.
    * Check that the difficulty multiplier is correctly applied.
    * Check that all answers appear correctly and are spelled correctly.
    * Check to see if it is possible to type all the answers in one game (it's not :) ).
    
* Leaderboard
    * Check that data is set to the database correctly.
    * Check that data is retrieved from the database correctly.


## Bugs

### Resolved Bugs

1. - Issue - Upon entering an integer, the menu did not redirect at planned

- Resolution - All terminal inputs are strings and my code was looking for an integer. I reset my if statements to look for strings

2. - Issue - The quiz class __init__ function was not correctly assigned attributes of theme and difficulty to itself.

- Resolution - The theme and difficulty are set using functions which are defined with the class. This means that you need to call them using self.function. This has initially been left out.

3. - Issue - When correct input was put into the code for quiz difficulty, the input was asked for again instead of continuing

- Resolution - This was fixed by refactoring the number of while and for loops that were running at the same time. Now the code is much more straight forward.

4. - Issue - The same question was asked on repeat

- Resolution - The index number for the list which contains all the questions was initialised inside of the loop and so was reset for each iteration. This was simply moved outside

### Existing Bugs

There are no known bugs at the point of deployment.

### Testing deployed site.

*   Additional testing was completed on the deployed website to ensure that it matched the final development version. All inputs, sections and content were checked.
