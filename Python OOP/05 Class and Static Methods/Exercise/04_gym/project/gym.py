from project import Customer
from project import Equipment
from project import ExercisePlan
from project import Subscription
from project import Trainer


class Gym:
    def __init__(self) -> None:
        self.customers: Customer(list) = []
        self.trainers: Trainer(list) = []
        self.equipment: Equipment(list) = []
        self.plans: ExercisePlan(list) = []
        self.subscriptions: Subscription(list) = []

    def add_customer(self, customer: Customer) -> None:
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer) -> None:
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment) -> None:
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plans: ExercisePlan) -> None:
        if plans not in self.plans:
            self.plans.append(plans)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int) -> str:
        subscription = self.subscriptions[subscription_id - 1]
        customer_id = subscription.customer_id
        trainer_id = subscription.trainer_id
        plan_id = subscription.exercise_id
        customer = self.customers[customer_id - 1]
        trainer = self.trainers[trainer_id - 1]
        plan = self.plans[plan_id - 1]
        equipment_id = plan.equipment_id
        equipment = self.equipment[equipment_id - 1]
        result = subscription.__repr__() + '\n' + customer.__repr__() + '\n' + trainer.__repr__() + '\n' + equipment.__repr__() + '\n' + plan.__repr__()
        return result