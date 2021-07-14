#!/usr/bin/env python

import prompt
import sys

sys.path.append('brain_games/games')


from random import randint
import games


def greet(who):
    print('Hello, {}!'.format(who))


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greet(name)
    return name


def calc_game(login):
    print('What is the result of the expression?')
    points = 0
    signs = {1: '+',
             2: '-',
             3: '*'}
    while points != 3:
        key = randint(1, 3)
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        if key == 1:
            correct_answer = number1 + number2
        elif key == 2:
            correct_answer = number1 - number2
        else:
            correct_answer = number1 * number2

        print(f'Question: {number1} {signs[key]} {number2}')
        answer = int(prompt.string('Your answer: '))

        if answer == correct_answer:
            points += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'")
            print(f"Let's try again, {login}!")
            break
        if points == 3:
            print(f"Congratulations, {login}!")


def main():
    # calc_game(welcome_user())
    print(games.uga_ga())


if __name__ == '__main__':
    main()
