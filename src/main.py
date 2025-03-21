import requests
import time
difficulties = {'easy', 'medium','hard'}
category_url = (requests.get('https://opentdb.com/api_category.php')).json()
categories = {}
def get_int(query):
    while True:
        try:
            var = int(input(query))
            break
        except ValueError: print('Please input a valid number. >')
    return var
def print_categories():
    i = 0
    while i <= 23:
        categories[i] = category_url['trivia_categories'][i]['name']
        print(f'{i + 1}: {categories[i]}')
        i += 1
def set_amount(amount):
    if amount > 50 or amount < 1:
        print('Invalid number. Please retry.')
        while True:
            var = get_int('How many questions do you want to be asked? > ')
            if var > 50 or var < 1: print('Invalid number. Please retry.')
            else: break
    else: return amount
class Questions:
    def __init__(self, difficulty, amount, category):
        self.difficulty = difficulty
        self.amount = amount
        self.category = category
    def get_difficulty(self): return self.difficulty
    def get_amount(self): return self.amount
    def get_category(self): return self.category
    def set_category(self, category):
        self.category = category + 8
        while self.category < 9 or self.category > 32: print('Invalid number. Please retry')
    def set_difficulty(self, difficulty): self.difficulty = difficulty
    def get_questions(self):
        while True:
            url = (requests.get(f'https://opentdb.com/api.php?amount={self.amount}&category={self.category}&difficulty={self.difficulty}')).json()
            if url['response_code'] == 0:
                print('Success!')
                return url
            elif url['response_code'] == 1:
                cat_question_amount = (requests.get(f'https://opentdb.com/api_count.php?category={self.category}')).json()
                print("Too many questions! Defaulting to maximum amount in category...")
                time.sleep(5)
                for i in difficulties:
                    if self.difficulty == i:
                        set_amount(cat_question_amount['category_question_count'][f'total_{i}_question_count'])
            elif url['response_code'] == 5:
                x = 0
                while url['response_code'] == 5:
                    x += 1
                    print(f'Rate Limited! Waiting 5 seconds. Retried {x} time(s)...')
                    time.sleep(5)
                    if x == 5:
                        print('API unreachable. Please restart the program.')
                        exit()

questions = Questions('easy', 0, 0)
set_amount(0)
print_categories()
questions.set_category(get_int('What number category would you like? > '))
questions.get_questions()