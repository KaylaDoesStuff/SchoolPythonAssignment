import requests
import time
import json

difficulties = {'easy', 'medium','hard'}

class Questions:
    def __init__(self, difficulty, amount, category):
        self.difficulty = difficulty
        self.amount = amount
        self.category = category

    def get_difficulty(self):
        return self.difficulty

    def get_amount(self):
        return self.amount

    def get_category(self):
        return self.category

    def set_amount(self, Iinput):
        self.amount = Iinput

    def get_questions(self):
        while True:
            url = (requests.get(f'https://opentdb.com/api.php?amount={self.amount}&category={self.category}&difficulty={self.difficulty}')).json()
            if url['response_code'] == 0:
                print('Success!')
                break
            elif url['response_code'] == 1:
                cat_question_amount = (requests.get(f'https://opentdb.com/api_count.php?category={self.category}')).json()
                print("Too many questions! Defaulting to maximum amount in category...")
                time.sleep(5)
                for i in difficulties:
                    if self.difficulty == i:
                        self.set_amount(cat_question_amount['category_question_count'][f'total_{i}_question_count'])
            elif url['response_code'] == 5:
                print('Rate Limited! Waiting 5 seconds...')
                time.sleep(5)

questions = Questions('easy', 30, 20)
Questions.get_questions(questions)