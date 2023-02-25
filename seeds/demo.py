import datetime
import random

from apps.blog.models import Post
from apps.section10.models import Puppy
from apps.section12.models import User
from flask_seeder import Faker, Seeder, generator
from werkzeug.security import generate_password_hash

breeds = (
    "Golden Retrievers",
    "Boston Terriers",
    "Labrador Retrievers",
    "Poodles",
    "Border Collie",
    "Beagle",
    "Irish Setter",
    "Staffordshire Bull Terrier",
    "Cavalier King Charles Spaniel",
    "Cockapoo",
    "Boxer",
    "Shih Tzu",
    "French Bulldog",
    "Basset Hound",
    "Cocker Spaniel",
    "Greyhound",
    "Great Dane",
    "Samoyed",
    "West Highland Terriers",
    "Pembroke Welsh Corgi",
)


# class PuppySeeder(Seeder):
#     def run(self):
#         faker = Faker(
#             cls=Puppy,
#             init={
#                 "name": generator.Name(),
#                 "age": generator.Integer(start=1, end=10),
#                 "breed": "",
#             },
#         )
#
#         for puppy in faker.create(10):
#             print(f"Adding puppy: {puppy}")
#             puppy.breed = random.choice(breeds)
#             self.db.session.add(puppy)


class UserSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=User,
            init={
                "email": generator.Email(),
                "username": generator.Name(),
                "password": generator.String("1234"),
            },
        )

        for user in faker.create(100):
            print(f"Adding user: {user}")
            self.db.session.add(user)


class PostSeeder(Seeder):
    def run(self):
        faker = Faker(
            cls=Post,
            init={
                "title": "",
                "text": "",
                "user_id": 1,
            },
        )

        for post in faker.create(100):
            post.user_id = random.randrange(1, 10, 1)
            # post.date = datetime.datetime.now()
            post.title = f"dummy title: {post.user_id}"
            post.text = "a" * 101
            print(f"Adding post: {post}")
            self.db.session.add(post)
