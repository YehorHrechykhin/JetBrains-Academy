import random

class Friends:
    def __init__(self):
        self.friends_list = []
        self.friends = {}
        self.number_friends = 0
        self.total_bill = 0
        self.bill = 0
        self.lucky = ''

    def get_number_friends(self):
        total = int(input('Enter the number of friends joining (including you):\n'))
        if total > 0:
            self.number_friends = total
        else:
            print('No one is joining for the party')
    
    def add_friends(self):
        print('Enter the name of every friend (including you), each on a new line:')
        for i in range(self.number_friends):
            self.friends_list.append(input())

    def get_bill(self):
        self.total_bill = int(input('Enter the total bill value:\n'))
        answer = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n")
        if answer == 'Yes':
            self.lucky = random.choice(self.friends_list)
            print(f'{self.lucky} is the lucky one!')
            self.number_friends -= 1
        else:
            print('No one is going to be lucky')
        self.bill = round(self.total_bill / self.number_friends, 2)

    def split_bill(self):
        if self.lucky == '':
            self.friends = dict.fromkeys(self.friends_list,self.bill)
        else:
            self.friends = dict.fromkeys(self.friends_list,self.bill)
            self.friends[self.lucky] = 0

    def main(self):
        self.get_number_friends()
        if self.number_friends:
            self.add_friends()
            self.get_bill()
            self.split_bill()
            print(self.friends)


get_friends = Friends()
get_friends.main()