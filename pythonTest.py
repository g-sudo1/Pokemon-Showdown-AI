#!/usr/bin/env python3
import asyncio

from poke_env import Player
from poke_env import RandomPlayer
from poke_env.data import GenData
import sys

sys.path.append("../src")
class YourFirstAgent(Player):
    def choose_move(self, battle):
        for move in battle.available_moves:
            if move.base_power > 90:
                # A powerful move! Let's use it
                return self.create_order(move)

        # No available move? Let's switch then!
        for switch in battle.available_switches:
            if switch.current_hp_fraction > battle.active_pokemon.current_hp_fraction:
                # This other pokemon has more HP left... Let's switch it in?
                return self.create_order(switch)

        # Not sure what to do?
        return self.choose_random_move(battle)
    
firstAgent = YourFirstAgent()
second_player = RandomPlayer()
async def battle():
    await firstAgent.battle_against(second_player, n_battles=1)
asyncio.run(battle())
print(
    f"Player {firstAgent.username} won {firstAgent.n_won_battles} out of {firstAgent.n_finished_battles} played"
)
print(
    f"Player {second_player.username} won {second_player.n_won_battles} out of {second_player.n_finished_battles} played"
)

# Looping over battles

for battle_tag, battle in firstAgent.battles.items():
    print(battle_tag, battle.won)


