# Quiz

Intellectual quiz-game

To play the game you need 2 teams. Each team chooses category and difficulty of question one by one.
The team that get more points after all questions have been answered - wins.

#### Screenshot example

![quiz.jpg](https://i.postimg.cc/7hWcxbhf/quiz.jpg)

## Requirements

You must have Python 3.7 or greater. You can download the latest Python release [here](https://www.python.org/downloads/).


## Install

Clone repository and install needed modules:

```
~$ git clone git@github.com:Komanok-dev/quiz-game.git
```
```
~$ pip3 install requests pygame
```

## Usage

You can change team names in settings.py

Here are 2 files with ready-made questions: 'question1.txt' and 'question2.txt'
Each file for 1 game. If you need more questions just create another file and specify it in settings.
Each line must consist of 4 elements separated by ';' and looks like:
```
Category;Points;Question;Answer
```

Run the program from the quiz folder:
```
> cd quiz
> python3 quiz.py
```

Alternatively you can just run this command file:
```
> quiz.exe
```