from project import Player


class Guild:
    def __init__(self, name: str) -> None:
        self.name = name
        self.players: list[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            current_player = [el for el in self.players if el.name == player_name][0]
            self.players.remove(current_player)
            current_player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        except IndexError:
            return f"Player {player_name} is not in the guild."

    def guild_info(self) -> str:
        result = f"Guild: {self.name}\n"
        for player in self.players:
            result += f"{player.player_info()}\n"
        return result