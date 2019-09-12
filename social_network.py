#Vpythone :)
import csv
from datetime import date
import networkx as nx
import matplotlib.pyplot as plt

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

    # def add_friend(self, Friend):
    #     self.friends.append(Friend)

    def get_friends(self):
        for friend in self.friends:
            print(friend.name)

    def __str__(self):
        return f'Name: {self.name} \nDate of Birth: {self.date_of_birth} \nNumber of Friends: {len(self.friends)}'

    # def __len__(self):
    #     return len(self.friends)
    #
    # def __gt__(self, other):
    #     return len(self.friends) > len(other.friends)
    #
    # def __lt__(self, other):
    #     return len(self.friends) < len(other.friends)
    #
    # def __ge__(self, other):
    #     return len(self.friends) >= len(other.friends)
    #
    # def __le__(self, other):
    #     return len(self.friends) <= len(other.friends)

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
    users = nx.Graph()

    def add_user(self, user: Author):
        self.users.add_node(f'{user.name}', data={'name': f'{user.name}', 'date_of_birth': f'{user.date_of_birth}'})

    def init_users(self, users):
        self.users = users

    def add_friends(self, user1, user2):
        self.users.add_edge(f'{user1}', f'{user2}')

    def recommend_friends(self, user):
        friends_of_friends = set()
        neighbours = set(nx.neighbors(self.users, f'{user}'))
        #найдем друзей, чтобы потом найти друзей друзей
        for neighbour_i in neighbours:
            neighbours_neighbour = set(nx.neighbors(self.users, neighbour_i))  #находим друзей друга
            neighbours_neighbour_sorted = neighbours_neighbour.difference(neighbours)
            friends_of_friends.update(neighbours_neighbour_sorted)
        friends_of_friends.remove(user)
        return friends_of_friends

    def __getitem__(self, name):
        users_list = list(filter(lambda x: x.name == name, self.users))
        return users_list

#Метод для экспорта пользователей в CSV файл
    def load_users_to_csv(self):
        with open('users.csv', 'wt') as f:
            writer = csv.DictWriter(f, ['name', 'dateofbirth', 'friendsnumber'])
            writer.writeheader()
            for item in self.users:
                somedict = dict(name=f'{item.name}', dateofbirth=f'{item.date_of_birth}',
                                friendsnumber=f'{len(item.friends)}')
                writer.writerow(somedict)


 # user = []
 # user.append(Author('Ann', 1989, 3, 1))
 # user.append(User('Masha', 1993, 12, 25))
 # user.append(User('Borya', 1989, 2, 21))
 # user.append(Author('Ann', 1989, 4, 12))

social_network = SocialNetwork()
social_network.add_user(Author('Ann', 1989, 3, 1))
social_network.add_user(Author('Masha', 1993, 12, 25))
social_network.add_user(Author('Borya', 1989, 2, 21))
social_network.add_user(Author('Vladislav', 1781, 12, 25))
social_network.add_user(Author('Yiura', 1991, 12, 12))
social_network.add_user(Author('Nikolai', 1988, 2, 22))


social_network.add_friends('Ann', 'Masha')
social_network.add_friends('Borya', 'Masha')
social_network.add_friends('Yiura', 'Masha')
social_network.add_friends('Nikolai', 'Masha')
social_network.add_friends('Ann', 'Vladislav')

print(social_network.recommend_friends('Ann'))

nx.draw_networkx(social_network.users)
plt.show()

# users_number = (len(user))
# for i in range(users_number):
#     for j in range(users_number):
#         if i != j:
#             user[i].add_friend(user[j])

# print("First User's name")
# print(f'{user[0].name}')
# print("\n")
#
# print("Second User's age")
# print(f'{user[1].get_age()} years')
# print("\n")
#
# print("Number of Third User's friends")
# print(f'{len(user[2].friends)}')
# print("\n")
#
#
#
# print("Author's posts")
# user[0].add_post('Bla bla bla')
# user[0].add_post('Bla bla bla (2)')
# user[0].add_post('Bla bla bla (3)')
# print(user[0].posts)
# print("\n")
#
# print("Author's posts after removal of one of them")
# user[0].remove_post(0)
# print(user[0].posts)
# print("\n")
#
# print("Users' avatars")
# user[1].Avatar = "Second User's Avatar Url"
# for i in range(users_number):
#     print(user[i].Avatar)
# print("\n")
#
# print("Users' premium modes")
# user[2].enable_premium_mode()
# for i in range(users_number):
#     print(user[i].premium_mode_enabled)
# print("\n")
#
# user.append(Author('Alex', 1990, 12, 31))
#
# print("Users' parameters")
# for i in range(len(user)):
#     print(f'{user[i]} \n')
#
# print("Number of User's friends")
# for i in range(len(user)):
#     print(f'{len(user[i])} \n')
#
# print("Friends list comparison")
# print(user[0] > user[4])
# print(user[0] < user[4])
# print(user[0] >= user[4])
# print(user[0] <= user[4])
# print("\n")
#
# print("Users' with name Ann in Vpythone")
# name_to_find = 'Ann'
# for i in range(len(social_network[name_to_find])):
#     print(f'{social_network[name_to_find][i]}\n')

#social_network.load_users_to_csv()

