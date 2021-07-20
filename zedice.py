import random as rng
import discord

brain = "Brain :brain:"
feet = "Footsteps :footprints:"
shotgun = "BLAM! :exploding_head:"

#Game Classes

class Zedie:
    def __init__(self):
        self.faces = [brain, brain, brain, feet, feet, shotgun]
    
    def roll(self):
        return self.faces[(rng.randint(0,5))]
    
    def __repr__(self) -> str:
        return f"Green: {self.roll()}"

class Red_zedie(Zedie):
    def __init__(self):
        self.faces = [brain, feet, feet, shotgun, shotgun, shotgun]

    def __repr__(self) -> str:
        return f"Red: {self.roll()}"

class Yellow_zedie(Zedie):
    def __init__(self):
        self.faces = [brain, brain, feet, feet, shotgun, shotgun]

    def __repr__(self) -> str:
        return f"Yellow: {self.roll()}"

class Dice_bag:
    def __init__(self):
        self.contents = [Zedie(), Zedie(), Zedie(), Zedie(), Zedie(), Zedie(), Yellow_zedie(), Yellow_zedie(), Yellow_zedie(),
         Yellow_zedie(), Red_zedie(), Red_zedie(), Red_zedie()]

    def select_dice(self, amount):
        draw = []
        i = 0
        while i < amount:
            draw.append(self.contents.pop(rng.randint(0,len(self.contents) - 1)).roll())
            i += 1
        return draw

class Rolled_dice:
    def __init__(self, inital_roll) -> None:
        self.dice_pool = inital_roll
        self.feet_total = 0
        self.brain_total = 0
        self. blam_total = 0

#Discord classes

class Active_game:
    def __init__(self, server_id, channel_id, players = []) -> None:
        pass