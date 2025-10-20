from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    MIN_BUDGET_REQUIRED = 1000000
    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def team_data(self):
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.MIN_BUDGET_REQUIRED:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self,race_pos: int) -> str:
        expenses, sponsors = self.team_data
        revenue = 0

        for sponsor in sponsors.values():
            for position, investment in sponsor.items():
                if race_pos <= position:
                    revenue += investment
                    break
        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
