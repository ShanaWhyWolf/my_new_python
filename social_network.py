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

User001 = User('Ann', 1989, 3, 1)
User002 = User('Masha', 1993, 12, 25)
User003 = User('Borya', 1989, 2, 21)

User001.add_friend(User002)
User001.add_friend(User003)
User002.add_friend(User001)
User002.add_friend(User003)
User003.add_friend(User001)
User003.add_friend(User002)

print(f'{User001.name}')
print(f'{User002.get_age()} years')
print(f'{len(User003.friends)}')