![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome LordButley,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

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



# TypeKwondo!

Welcome to TypeKwondo! 

As all developers will tell you, being able to type quickly and accurately is an invaluable skill. Not staring at your index fingers whilst trying to work out where the missing semi-colon is actually really useful.

And what do developers love? Gamification! Introducing TypeKwondo, where you get to improve your typing skills, whilst competitively playing a typing game in a theme of your choosing. On top of this, you can also compare your scores with the leaderboard and try and make it into the top 5 best typers ever (*not an official title) 

You can visit the live website [here](https://lordbutley.github.io/JapanEasy/)

![Am I Responsive image of how the landing page looks across different browser sizes](assets/images/responsivescreens.JPG)

# Contents

# UX

## Project Goals

* Create a user-friendly and accessible website.
* Create a learning game that is straight forward to start, play and restart.
* Create a translation game that can be played with questions in English or Hiragana.
* Ensure that questions are randomised and not repeated
* Ensure that answers are randomised so that the language is learnt rather than the questions
* Provide the user with constant feedback on their progress through the game and through the site. 
* Give the website a Japanese feel through imagery.
* Ensure the website is viewable across devices of all sizes.
* To create a website that would be immediately useful when live but also has scope to be expanded.

## User Stories

* As a user visiting the site for the first time, I want to be able to navigate the website intuitively.
* As a user visiting the site for the first time, I want to be able to play the game quickly and easily
* As a user, I want to be able to access the website on desktop, tablet and mobile devices to ensure convenience.
* As a user, I want to be able to easily access the social media accounts of "JapanEasy". 
* As a user, I want to be provided with feedback such as correct and incorrect scores to allow me to monitor my learning progress.
* As a user, I want to be able to choose whether the questions are in English or Hiragana.
* As a user, I want to be able to set the difficulty of the quiz
* As a user, I want the questions *and* answers to be randomised to help with learning.

## Target Audience

The target audience of this website is any person who :

* wants to learn Japanese
* is learning Japanese and wants a helpful learning aid
* has learnt Japanese and wants a revision aid

## Structure

The website is focussed entirely on the learning quiz. As such there is a single HTML page that is manipulated through CSS and JavaScript so not to distract from the site's goals. This manipulation results in 3 distinct parts:

- Welcome page - This contains and introduction and brief explanation of the quiz and well as the intuitive controls.
- Quiz page - This is generated through JavaScript and contains a question and a number of answers determined by the difficulty setting.
- End game page - This contains the score achieved in the quiz and feedback.


## Skeleton

The initial ideas were taken from the structure planning and a visual mock up was created using Balsamiq. Mobile and Tablet wireframes are all available [here.](wireframes/wireframes.pdf). Note Desktop and Tablet wireframes are identical with the only difference being a larger background image and as such have not been included.

## Surface

### Imagery

### Colour Palette

### Typography

### Language / Tone

From my experience learning Japanese, I found that one of the most important things with a learning tool such as this, is the simplicity of use. As such I have minimised the amount of text through the website. Additionally, where there is text, I have ensured that it has a positive tone due to the difficulty faced in learning a language like Japanese. As anyone who's tried learning a foreign language before will know, motivation is key.

# Features

## Existing Features

### Game container

- All content appears within a container that has a background image of a light wood to match that of an Ema. If this background image cannot load, a background colour has been added which has been plucked from the image. The container has a maximum absolute size to make sure that at full screen it bears resemblance to an Ema and a maximum relative size to ensure that you can always see the background image on all screen sizes. It additionally has a border style and shadow to give it the 3d look you would expect from a wooden tile.

### Header

- Logo "JapanEasy" in large unmissable font sets the tone of the website. The Logo is a hyperlink back to the homepage in keeping with current web standards. This is consistent on every page

The header becomes underlines when hovered over.

![Screen shot of the header of "JapanEasy"](assets/images/header.JPG) -->

### Footer

- The Footer contains links to the "JapanEasy" social media websites. These open to a new tab upon click. These are consistent on every page

![Screen shot of the footer of "JapanEasy"](assets/images/footer.JPG) -->


### Background

- Background image - This is a full screen size image of a lots of Ema which will have been hung in a temple. Ema are praying or wishes written upon a piece of wood. This is the background image for all pages. There are two version of the image of different resolutions which will load depending on your screensize to optimize speed.

![Background image of "JapanEasy"](assets/images/backgroundimage2.webp)

### Introduction, explanation and choices

 - You are welcomed with a short and concise introduction and explanation of what to do followed by a couple of radio buttons. These are the options for the game. You can either have the questions in Hiragana and the answers in English or Vice versa. All questions and answers are completely randomised to ensure that the syllabary is learnt rather than the questions.

 The difficulty can be selected as easy, medium or hard. Easy gives 3 answers to choose from, medium gives 6 and hard gives 9.

![Screen shot of the first page of "JapanEasy"](assets/images/choices.JPG) -->

### Buttons

- All buttons on the site provide user feedback by taking on the red border when hovered over.

### Quiz page

- The layout of the quiz is a question, which is either English or Hiragana, followed by answer tiles; the number of which depends on the difficulty setting.
- Score counters runs along the bottom that displays the number of correct answers given as well as incorrect.
- All answer tiles provide feedback with the consistent red border on hover.
- When an answer is chosen, if it is correct, the background of the tile will turn green, and if incorrect, the background of the tile will turn red.
- The quiz will run through the whole syllabary, however you can choose to end the game at any time with the "End Game" button which will take you to the end game page.

![Screen shot of quiz from "JapanEasy"](assets/images/quiz.JPG)

### End Game page

- When you click to end the game or complete the syllabary to are taken to an end game screen which provided you with the number of answers correctly answered out of the number of questions.
- Feedback is provided dependent on the score.
- A "try again" button returns you to the home page where you can make your choices again and start the quiz again.

![Screen shot of contact us form from "It's Puppy Time"](assets/images/endgame.JPG) 

### Python functionality

## Features to implement in the future

- Add additional syllabaries such as Katakana and eventually Kanji

## Technologies Used

 ### Languages Used:

 1. [Python](https://en.wikipedia.org/wiki/Python) 
 - Programming language providing content and logic of project
 
 ### Frameworks, Libraries & Programs Used:

    
 1. [GitPod](https://gitpod.io/)
    - IDE (Integrated Development Environment), for writing, editing and saving code.

 2. [GitHub](https://github.com/) 
    - Remote hosting platform and code  repository.

10. [Google Developer Tools](https://developers.google.com/web/tools) - including Lighthouse
    - Used to constantly test the code and give feedback. 

11. [Responsinator](https://www.responsinator.com/) 
    - Used to check responsiveness across multiple screen sizes quickly.

## Testing

The testing process can be seen in the [TESTING.md](TESTING.md) document.

## Deployment

### Github Pages
The site is hosted using GitHub pages, deployed directly from the master branch of GitHub. The deployed site will update automatically as new commits are pushed to the master branch.

#### How I deployed my project to GitHub pages.
To host on GitHub pages you must follow these steps:

1. Go to [GitHub.com](https://github.com/)
2. Login to my account.
3. Click on 'Responsitories'
4. Click on 'JapanEasy'
5. Go to the 'Settings' tab
6. Scroll down to the 'GitHub Pages' section and set the source to 'main'. This turns on GitHub pages for the repository.
7. Reload the page. Scroll back to 'GitHub Pages' section, where the new URL for the deployed site can be found.

Additional information around these steps can be found on the [GitHub Pages Help Page](https://docs.github.com/en/github/working-with-github-pages/creating-a-github-pages-site).

#### Forking a GitHub Repository
1. Login to GitHub.
2. Locate your desired repository.
3. Locate the fork option in the top-right hand corner of the repository page.    
4. You will be asked where you want to fork it to.

## Credits

### Code

https://stackoverflow.com/questions/2084508/clear-terminal-in-python

### Content

- All content written is my own and based on my own experiences learning Hiragana and what I would have found more helpful. I took inspiration from all the main Hiragana websites such as 

### Thanks

- to tutor support at Code Institute. I have constantly found their positivity and genuine interest in helping resolve issues in my code a great help 
- to my mentor who reviewed my project and gave feedback.
- to my partner who travelled Japan with me and gave me the inspiration to make this project. 