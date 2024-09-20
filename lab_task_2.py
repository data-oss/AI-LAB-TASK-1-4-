#question # 1
# fizz buzz

import random
class fizz_buzz:
    def __init__(self,x):
        self.x=x
    def game(self):
        for i in range (1,100):
            if i%3==0 and 1%5==0:
                print("fizz buzz : ")
            elif i%3==0:
                print("fizz: ")
            elif i%5==0:
                print("buzz: ")
            else:
                print(i)
    def play(self):
        self.game()
        print("Do you want to play again? (yes/no)")
        answer = input()
        if answer.lower() == "yes":
            self.play()
        else:
            print("Thank you for playing!")
fizz_buzz = fizz_buzz(10)
fizz_buzz.play()


# Task 2 -- Movie Budgets
movies = [
    ("Eternal Sunshine of the Spotless Mind", 80000000),
    ("Memento", 12000000),
    ("Requiem for a Dream", 5500000),
    ("Pirates of the Caribbean: On Stranger Tides", 479000000),
    ("Avengers: Age of Ultron", 465000000),
    ("Avengers: Endgame", 456000000),
    ("Incredibles 2", 300000000)
]
movies_add = int(input("How many movies would you like to add? "))
for i in range(movies_add):
    name = input("Enter the movie name: ")
    budget = int(input("Enter the movie budget: "))
    movies.append((name, budget))
total_budget = sum(budget for i, budget in movies)
average_budget = total_budget / len(movies)
high_budget = []
for movie, budget in movies:
    if budget > average_budget:
        difference = budget - average_budget
        high_budget.append((movie, budget, difference))
print(f"The average movie budget is: ${average_budget:,.2f}")
print("Movies with a budget higher than the average:")
for movie, budget, difference in high_budget:
    print(f"{movie}: ${budget:,.2f} (which is ${difference:,.2f} higher than the average)")
print(f"Number of movies with a budget higher than the average: {len(high_budget)}")
