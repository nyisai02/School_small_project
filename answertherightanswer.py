#First pip install the tavulate for chart dispaly
#random will ask you a question random

import random
from tabulate import tabulate

class Flashcard:
    def __init__(self):
        self.fruits = {'apple': 'red',
                       'orange': 'orange',
                       'watermelon': 'green',
                       'banana': 'yellow'}
        self.results = []

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
            user_answer = input()
            
            if user_answer.lower() == color:
                print("Correct answer")
                result = ["Correct", fruit, color]
            else:
                print("Wrong answer")
                result = ["Wrong", fruit, user_answer]
                
            self.results.append(result)
            
            option = int(input("Enter 0 if you want to play again, otherwise enter any other number to quit: "))
            if option:
                break
        
        self.show_results()
        
    def show_results(self):
        table = tabulate(self.results, headers=["Result", "Fruit", "Your Answer"], tablefmt="grid")
        print(table)

print("Welcome to the fruit quiz!")
fc = Flashcard()
print(fc.fruits)
fc.quiz()
