from movie_world_2.project.customer import Customer
from movie_world_2.project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer_idx = self.customer_id(customer_id)
        dvd_idx = self.dvd_id(dvd_id)
        customer = self.customers[customer_idx]
        dvd = self.dvds[dvd_idx]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return 'DVD is already rented'
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        self.dvds[dvd_idx].is_rented = True
        self.customers[customer_idx].rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer_idx = self.customer_id(customer_id)
        dvd_idx = self.dvd_id(dvd_id)
        customer = self.customers[customer_idx]
        dvd = self.dvds[dvd_idx]
        if dvd in customer.rented_dvds:
            self.customers[customer_idx].rented_dvds.pop(self.customers[customer_idx].rented_dvds.index(dvd))
            self.dvds[dvd_idx].is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def customer_id(self, searched):
        for i in range(len(self.customers)):
            if self.customers[i].id == searched:
                return i

    def dvd_id(self, searched):
        for i in range(len(self.dvds)):
            if self.dvds[i].id == searched:
                return i

    def __repr__(self):
        string = []
        for i in self.customers:
            string.append(i)
        for i in self.dvds:
            string.append(i)
        return '\n'.join([str(i) for i in string])


# Test Code
c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))

print(movie_world)
