#!/usr/bin/env python

import prompt


def greet(who):
    print('Hello, {}!'.format(who))

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    greet(name)


def main():
    welcome_user()


if __name__ == '__main__':
    main()
