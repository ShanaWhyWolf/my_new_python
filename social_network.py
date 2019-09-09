class User:
    def __init__(self, name, date_of_birth_year, date_of_birth_month, date_of_birth_day):
        self.name = name
        from datetime import date
        self.date_of_birth = date(date_of_birth_year,date_of_birth_month,date_of_birth_day)
        self.friends = []

    def get_age(self):
        from datetime import date
        current_date = date.today()
        age = (current_date - self.date_of_birth).days
        return str (age/365)

    def add_friend(self, Friend):
        self.friends.append(Friend)

    def get_friends(self):
        for friend in self.friends:
            print(friend.name)


        # import datetime
        # current_date = datetime.date.today()
        # from datetime import date
        # current = date.today()
        # current.day
        # current.year

class SocialNetwork:
    def __init__(self):
        pass

    @classmethod
    def init_users(self, users):
        self.users = users

user = []
user.append(User('Ann', 1989, 3, 1))
user.append(User('Masha', 1993, 12, 25))
user.append(User('Borya', 1989, 2, 21))

user[0].add_friend(user[1])
user[0].add_friend(user[2])
user[1].add_friend(user[0])
user[1].add_friend(user[2])
user[2].add_friend(user[0])
user[2].add_friend(user[1])

print(f'{user[0].name}')
print(f'{user[1].get_age()} years')
print(f'{len(user[2].friends)}')

social_network = SocialNetwork()
social_network.init_users(user)