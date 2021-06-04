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

class Red_zedie(Zedie):
    def __init__(self):
        self.faces = [brain, feet, feet, shotgun, shotgun, shotgun]

class Yellow_zedie(Zedie):
    def __init__(self):
        self.faces = [brain, brain, feet, feet, shotgun, shotgun]