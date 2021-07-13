#!/usr/bin/env python

import prompt

from random import randint


def greet(who):
    print('Hello, {}!'.format(who))


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greet(name)
    return name


# def even_game(login):
#     print('Answer "yes" if the number is even, otherwise answer "no".')
#     points = 0
#
#     while points != 3:
#         number = randint(1, 500)
#         is_even_tumbler = 'yes' if number % 2 == 0 else 'no'
#         print(f'Question: {number}')
#         answer = prompt.string('Your answer ').lower()
#         if answer == is_even_tumbler:
#             points += 1
#             print('Correct!')
#         else:
#             correct_answer = 'yes' if answer == 'no' else 'no'
#             print(f"'{answer}' is wrong answer ;(."
#                   f" Correct answer was '{correct_answer}'")
#             print(f"Let's try again, {login}!")
#             break
#         if points == 3:
#             print(f"Congratulations, {login}!")


def calc_game(login):
    pass


def main():
    even_game(welcome_user())


if __name__ == '__main__':
    main()
