import random as rng
import discord

brain = "Brain :brain:"
feet = "Footsteps :footprints:"
shotgun = "BLAM! :exploding_head:"

class Zedie:
    def __init__(self):
        self.faces = [brain, brain, brain, feet, feet, shotgun]
    
    def roll(self):
        return self.faces[(rng.randint(0,5))]
    
    def __repr__(self) -> str:
        return "Green Die"

class Red_zedie(Zedie):
    def __init__(self):
        self.faces = [brain, feet, feet, shotgun, shotgun, shotgun]

    def __repr__(self) -> str:
        return "Red Die"

class Yellow_zedie(Zedie):
    def __init__(self):
        self.faces = [brain, brain, feet, feet, shotgun, shotgun]

    def __repr__(self) -> str:
        return "Yellow Die"

class Dice_bag:
    def __init__(self):
        self.contents = [Zedie, Zedie, Zedie, Zedie, Zedie, Zedie, Yellow_zedie, Yellow_zedie, Yellow_zedie, Yellow_zedie, Red_zedie, Red_zedie, Red_zedie]

    def select_dice(self, amount):
        draw = []
        i = 0
        while i < amount:
            draw.append(self.contents.pop(rng.randint(0,len(self.contents) - 1)))
            i += 1
        return draw

    