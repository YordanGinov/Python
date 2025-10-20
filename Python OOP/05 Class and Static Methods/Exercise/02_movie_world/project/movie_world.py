from project import Customer
from project import DVD


class MovieWorld:
    MOVIE_CAPACITY = 15
    CUSTOMER_CAPACITY = 10
    def __init__(self, name: str):
        self.name = name
        self.customers: Customer(list) = []
        self.dvds: DVD(list) = []

    @staticmethod
    def dvd_capacity() -> int:
        return MovieWorld.MOVIE_CAPACITY

    @staticmethod
    def customer_capacity() -> int:
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if self.CUSTOMER_CAPACITY > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if self.MOVIE_CAPACITY > len(self.dvds):
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = [c for c in self.customers if c.id == customer_id][0]
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += customer.__repr__() + "\n"
        for dvd in self.dvds:
            result += dvd.__repr__() + "\n"
        return result