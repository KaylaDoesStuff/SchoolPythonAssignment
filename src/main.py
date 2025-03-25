import requests
import time
import json
difficulties = ['Easy', 'Medium','Hard']
difficultiesLow = ['easy', 'medium', 'hard']
category_url = json.loads(requests.get('https://opentdb.com/api_category.php').text)
categories = {}
players = {}
def get_int(query):
    while True:
        try: var = int(input(query)); break
        except ValueError: print('Please input a valid number. >')
    return var
def print_categories():
    i = 0
    while i <= 23:
        categories[i] = category_url['trivia_categories'][i]['name']
        print(f'{i + 1}: {categories[i]}')
        i += 1
    time.sleep(5)
def set_amount(amount):
    if amount > 50 or amount < 1:
        while True:
            var = get_int('How many questions do you want to be asked? > ')
            if var > 50 or var < 1: print('Invalid number. Please retry.')
            else: return var
    else: return amount
def set_category(category):
    if category > 24 or category < 1:
        while True:
            var = get_int('What number category would you like? > ')
            if var > 24 or var < 1: print('Invalid number. Please retry.')
            else: return var
    else: return category

def playerCountAndName():
    player_amount = get_int('How many people are playing today? > ')
    i = 0
    while i < player_amount:
        players[i]['Name'] = input(f"Player {i+1}'s Name > ")
        players[i]['Score'] = 0

class Leaderboard:
    def __init__(self, topName, topScore):
        self.topName = topName
        self.topScore = topScore

class Player:
    def __init__(self, name, score, order):
        self.name = name
        self.score = score
        self.order = order

    def get_order(self): return self.order
    def get_name(self): return self.name
    def get_score(self): return self.score

    def set_name(self, name): self.name = name
    def set_order(self, order): self.order = order
    def set_score(self, score): self.score = score

class Questions:
    def __init__(self, difficulty, amount, category):
        self.difficulty = difficulty
        self.amount = amount
        self.category = category
    def get_difficulty(self): return self.difficulty
    def get_amount(self): return self.amount
    def get_category(self): return self.category
    def set_difficulty(self):
        i = 0
        while i <= 2:
            print(f'{i + 1}: {difficulties[i]}')
            i += 1
        var = get_int('What difficulty would you like to play? > ')
        while var < 1 or var > 3: print('Invalid option. Please repeat...'); self.set_difficulty()
        self.difficulty = difficultiesLow[var-1]
    def get_questions(self):
        x = 0
        while True:
            url = json.loads(requests.get(f'https://opentdb.com/api.php?amount={self.amount}&category={self.category}&difficulty={self.difficulty}&type=multiple-choice').text)
            if url['response_code'] == 1:
                cat_question_amount = json.loads(requests.get(f'https://opentdb.com/api_count.php?category={self.category}').text)
                print("Too many questions! Defaulting to maximum amount in category...")
                time.sleep(5)
                for i in difficultiesLow:
                    if self.difficulty == i:
                        self.amount = set_amount(cat_question_amount['category_question_count'][f'total_{i}_question_count'])
            elif url['response_code'] == 5:
                x += 1
                print(f'Rate Limited! Waiting 5 seconds. Retried {x} time(s)...')
                time.sleep(5)
                if x == 5: exit('API unreachable. Please restart the program.')
            else: break

questions = Questions('easy', 0, 0)
questions.amount = set_amount(0)
print_categories()
questions.category = set_category(0)
questions.set_difficulty()
questions.get_questions()