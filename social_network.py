from datetime import date
default_avatar = 'Default Avatar Url'
class AvatarMixin:
    Avatar = default_avatar

    def add_avatar(self, url):
        self.Avatar = url

class PremiumModeMixin:
    premium_mode_enabled = False

    def enable_premium_mode(self):
        self.premium_mode_enabled = True

class User(AvatarMixin, PremiumModeMixin):
    def __init__(self, name, date_of_birth_year, date_of_birth_month, date_of_birth_day):
        self.name = name
        self.date_of_birth = date(date_of_birth_year,date_of_birth_month,date_of_birth_day)
        self.friends = []

    def get_age(self):
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

class Author(User):
    posts = []

    def add_post(self, post_content: str):
        self.posts.append(post_content)

    def remove_post(self, post_id: int):
        self.posts.pop(post_id)


class SocialNetwork:
    def __init__(self):
        pass

    @classmethod
    def init_users(self, users):
        self.users = users

user = []
user.append(Author('Ann', 1989, 3, 1))
user.append(User('Masha', 1993, 12, 25))
user.append(User('Borya', 1989, 2, 21))

users_number = (len(user))
for i in range(users_number):
    for j in range(users_number):
        if i != j:
            user[i].add_friend(user[j])

print("First User's name")
print(f'{user[0].name}')
print("\n")

print("Second User's age")
print(f'{user[1].get_age()} years')
print("\n")

print("Number of Third User's friends")
print(f'{len(user[2].friends)}')
print("\n")

social_network = SocialNetwork()
social_network.init_users(user)

print("Author's posts")
user[0].add_post('Bla bla bla')
user[0].add_post('Bla bla bla (2)')
user[0].add_post('Bla bla bla (3)')
print(user[0].posts)
print("\n")

print("Author's posts after removal of one of them")
user[0].remove_post(0)
print(user[0].posts)
print("\n")

print("Users' avatars")
user[1].Avatar = "Second User's Avatar Url"
for i in range(users_number):
    print(user[i].Avatar)
print("\n")

print("Users' premium modes")
user[2].enable_premium_mode()
for i in range(users_number):
    print(user[i].premium_mode_enabled)