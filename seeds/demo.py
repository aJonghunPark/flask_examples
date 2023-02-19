import random

from apps.section10.models import Puppy
from flask_seeder import Faker, Seeder, generator

breeds = ("Golden Retrievers", "Boston Terriers", "Labrador Retrievers",
          "Poodles", "Border Collie", "Beagle", "Irish Setter",
          "Staffordshire Bull Terrier", "Cavalier King Charles Spaniel",
          "Cockapoo", "Boxer", "Shih Tzu", "French Bulldog", "Basset Hound",
          "Cocker Spaniel", "Greyhound", "Great Dane", "Samoyed",
          "West Highland Terriers", "Pembroke Welsh Corgi")


class PuppySeeder(Seeder):

    def run(self):
        faker = Faker(cls=Puppy,
                      init={
                          "name": generator.Name(),
                          "age": generator.Integer(start=1, end=10),
                          "breed": '',
                      })

        for puppy in faker.create(10):
            print(f"Adding puppy: {puppy}")
            puppy.breed = random.choice(breeds)
            self.db.session.add(puppy)
