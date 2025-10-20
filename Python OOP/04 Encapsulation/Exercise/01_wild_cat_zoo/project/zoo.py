from project.animals.animal import Animal
from project import Worker


class Zoo:
    def __init__(self, name:str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list = []
        self.workers: list = []
        self.__current_animal_capacity = 0
        self.__current_worker_capacity = 0


    def add_animal(self, animal:Animal, price: int) -> str:
        if self.__animal_capacity > self.__current_animal_capacity and price <= self.__budget:
            self.animals.append(animal)
            self.__budget -= price
            self.__current_animal_capacity += 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > self.__current_animal_capacity and price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > self.__current_worker_capacity:
            self.workers.append(worker)
            self.__current_worker_capacity += 1
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [el for el in self.workers if el.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum(w.salary for w in self.workers)
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        sum_for_animals = sum(a.money_for_care for a in self.animals)
        if self.__budget >= sum_for_animals:
            self.__budget -= sum_for_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self):
        # lions = [repr(el) for el in self.animals if el.__class__.__name__ == "Lion"]
        # tigers = [repr(el) for el in self.animals if el.__class__.__name__ == "Tiger"]
        # cheetah = [repr(el) for el in self.animals if el.__class__.__name__ == "Cheetah"]
        #
        # result = [f"You have {len(self.animals)} animals"]
        # result.append(f"----- {len(lions)} Lions:")
        # result.extend(lions)
        # result.append(f"----- {len(tigers)} Tigers:")
        # result.extend(tigers)
        # result.append(f"----- {len(cheetah)} Cheetahs:")
        # result.extend(cheetah)
        # return "\n".join(result)
        return self.__print_status(self.animals,"Lion", "Tiger", "Cheetah")

    def workers_status(self) -> str:
        # keepers = [repr(el) for el in self.workers if el.__class__.__name__ == "Keeper"]
        # caretaker = [repr(el) for el in self.workers if el.__class__.__name__ == "Caretaker"]
        # vet = [repr(el) for el in self.workers if el.__class__.__name__ == "Vet"]
        #
        # result = [f"You have {len(self.workers)} workers"]
        # result.append(f"----- {len(keepers)} Keepers:")
        # result.extend(keepers)
        # result.append(f"----- {len(caretaker)} Caretakers:")
        # result.extend(caretaker)
        # result.append(f"----- {len(vet)} Vets:")
        # result.extend(vet)
        # return "\n".join(result)
        return self.__print_status(self.workers,"Keeper", "Caretaker", "Vet")

    @staticmethod
    def __print_status(obj_list: list[Animal | Worker], *class_names: str):
        elements = {name: [] for name in class_names}
        for obj in obj_list:
            elements[obj.__class__.__name__].append(repr(obj))
        result = [f"You have {len(obj_list)} {str(obj_list[0].__class__.__bases__[0].__name__).lower()}s"]
        for key, value in elements.items():
            result.append(f"----- {len(value)} {key}s")
            result.extend(value)

        return "\n".join(result)
