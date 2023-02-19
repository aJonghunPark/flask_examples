from apps.section10.models import Puppy
from flask_seeder import Faker, Seeder, generator


class PuppySeeder(Seeder):

    def run(self):
        faker = Faker(cls=Puppy,
                      init={
                          "name": generator.Name(),
                          "age": generator.Integer(start=1, end=10),
                      })

        for puppy in faker.create(10):
            print(f"Adding puppy: {puppy}")
            self.db.session.add(puppy)
