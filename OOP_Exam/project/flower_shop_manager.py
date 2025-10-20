from project.clients.base_client import BaseClient
from project.clients.business_client import BusinessClient
from project.clients.regular_client import RegularClient
from project.plants.base_plant import BasePlant
from project.plants.flower import Flower
from project.plants.leaf_plant import LeafPlant


class FlowerShopManager:
    def __init__(self):
        self.income = 0
        self.plants: list[BasePlant|Flower|LeafPlant] = []
        self.clients: list[BaseClient|RegularClient|BusinessClient] = []
        self.valid_plant_type= {
            "Flower": Flower,
            "LeafPlant": LeafPlant
        }
        self.valid_client_type = {
            "RegularClient": RegularClient,
            "BusinessClient": BusinessClient
        }

    def add_plant(self, plant_type: str, plant_name: str, plant_price: float, plant_water_needed: int, plant_extra_data: str):
        if plant_type not in self.valid_plant_type:
            raise ValueError("Unknown plant type!")
        plant = self.valid_plant_type[plant_type](plant_name, plant_price, plant_water_needed, plant_extra_data)
        self.plants.append(plant)
        return f"{plant_name} is added to the shop as {plant_type}."

    def add_client(self, client_type: str, client_name: str, client_phone_number: str):
        if client_type not in self.valid_client_type:
            raise ValueError("Unknown client type!")
        client = [c for c in self.clients if c.phone_number == client_phone_number]
        if client:
            raise ValueError("This phone number has been used!")
        client = self.valid_client_type[client_type](client_name, client_phone_number)
        self.clients.append(client)
        return f"{client_name} is successfully added as a {client_type}."

    def sell_plants(self, client_phone_number: str, plant_name: str, plant_quantity: int):
        try:
            client = [c for c in self.clients if c.phone_number == client_phone_number][0]
        except IndexError:
            raise ValueError("Client not found!")
        plants = [p for p in self.plants if p.name == plant_name]
        if not plants:
            raise ValueError("No plants found!")
        if plant_quantity > len(plants):
            return "Not enough plant quantity."
        order_amount = 0
        for _ in range(plant_quantity):
            current_plant = plants.pop(0)
            self.plants.remove(current_plant)
            order_amount += current_plant.price - (current_plant.price * client.discount / 100)
        self.income += order_amount
        client.update_total_orders()
        client.update_discount()
        return f"{plant_quantity}pcs. of {plant_name} plant sold for {order_amount:.2f}"



    def remove_plant(self, plant_name: str):
        plant = [p for p in self.plants if p.name == plant_name]
        if not plant:
            return "No such plant name."
        remove_plant = plant[0]
        self.plants.remove(remove_plant)
        return f"Removed {remove_plant.plant_details()}"

    def remove_clients(self):
        clients = [c for c in self.clients if c.total_orders == 0]
        count = len(clients)
        if count != 0:
            for client in clients:
                self.clients.remove(client)
        return f"{count} client/s removed."

    def shop_report(self):
        unsold_plants = {}
        for plant in self.plants:
            if plant.name not in unsold_plants:
                unsold_plants[plant.name] = 0
            unsold_plants[plant.name] += 1
        unsold_plants = dict(sorted(unsold_plants.items(), key=lambda x: (-x[1], x[0])))
        #TODO check if the sorting is correct

        clients = sorted(self.clients, key=lambda x: (-x.total_orders, x.phone_number))

        result = "~Flower Shop Report~\n"
        result += f"Income: {self.income:.2f}\n"
        count_all_orders= 0
        for client in clients:
            count_all_orders += client.total_orders
        result += f"Count of orders: {count_all_orders}\n"
        unsold_plants_count = 0
        for plant in unsold_plants:
            unsold_plants_count += unsold_plants[plant]
        result += f"~~Unsold plants: {unsold_plants_count}~~\n"
        for plant_name, count in unsold_plants.items():
            result += f"{plant_name}: {count}\n"
        result += f"~~Clients number: {len(clients)}~~\n"
        result += "\n".join([client.client_details() for client in clients])

        return result

