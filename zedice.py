import random as rng
import discord

# "Constants" for the output in Discord.
brain = "Brain :brain:"
feet = "Footsteps :footprints:"
shotgun = "BLAM! :exploding_head:"

#Game Classes

#A standard green die, six-sided, weighted with brains, you can roll it and get a random side and it's icon.
class Zedie:
    def __init__(self):
        """Initialized as a die with specified possible sides to roll"""
        self.faces = [brain, brain, brain, feet, feet, shotgun]
        self.roll()
        self.color = "Green"
    
    def roll(self): # TODO Need to set the die face as active, not just return the text of the side.
        """Sets a random side of the die"""
        self.active_side = self.faces[(rng.randint(0,5))]
    
    def __repr__(self) -> str:
        return f"{self.color}: {self.active_side}"

#Red die, weighted with shotguns (more dangerous)
class Red_zedie(Zedie):
    def __init__(self):
        super().__init__() 
        self.faces = [brain, feet, feet, shotgun, shotgun, shotgun]
        self.color = "Red"


#Yellow die, equal sides.
class Yellow_zedie(Zedie):
    def __init__(self):
        super().__init__() 
        self.faces = [brain, brain, feet, feet, shotgun, shotgun]
        self.color = "Yellow"


#The game has 13 dice. You can draw any amount of dice, but typically it's 1 to 3. When a die is rolled, it's removed from the bag.
#Each active game needs it's own dice bag.
class Dice_bag:
    def __init__(self):
        """Bag starts with 13 dice, 3 reds, 4 yellow, nad 5 green"""
        self.contents = [Zedie(), Zedie(), Zedie(), Zedie(), Zedie(), Zedie(), Yellow_zedie(), Yellow_zedie(), Yellow_zedie(),
         Yellow_zedie(), Red_zedie(), Red_zedie(), Red_zedie()]

    def select_dice(self, amount):
        """Draw any amount of dice from the bag and remove them"""
        draw = []
        i = 0
        while i < amount:
            draw.append(self.contents.pop(rng.randint(0,len(self.contents) - 1)))
            i += 1
        return draw
    
    def return_dice(self, dice = []):
        """Once a player's turn is done, the dice from the game's Rolled_dice.dice_pool need returned."""
        for die in dice:
            self.contents.append(die)

#Which dice have been rolled for an active game. The initial roll is 3 dice from the dice bag. Once turn is done, put dive_pool back into the
#the game's dice bag and replace the instance of rolled dice with a new one. (maybe new dice bag too?)
class Rolled_dice:
    """Whichever rolled dice for a player's current turn. If shotgun_total >= 3, they gain no points and return all dice back into the bag."""
    def __init__(self, inital_roll = []) -> None:
        self.dice_pool = inital_roll
        self.feet_total = 0
        self.brain_total = 0
        self.shotgun_total = 0
        self.update_totals(self.dice_pool)
    
    def access_dice_pool(self):
        return self.dice_pool
    
    def add_dice(self, dice):
        self.dice_pool.append(dice)

    def update_totals(self, dice_pool):
        #This will have to change, I need to put die instances in roll, not just results, then each die for it's roll.
        self.feet_total = [die.active_side for die in self.dice_pool()].count(feet) 
        self.brain_total = [die.active_side for die in self.dice_pool()].count(brain) 
        self.shotgun_total = [die.active_side for die in self.dice_pool()].count(shotgun) 
    


#Discord classes

#Any given server can have one active game in any given channel. If a non-player or player who'd turn it isn't, tries to run a command,
#it will check versus current player and return an error. 
#Will need to allow admins or perhaps a time out so a stalled game doesn't prevent play forever.
class Active_game:
    def __init__(self, server_id, channel_id, players = []) -> None:
        self.location = (server_id, channel_id)
        self.players = rng.shuffle(players)
        self.current_player = self.players[0]
        self.start_player = self.players[0]
        self.dice_bag = Dice_bag()
        self.rolled_dice = Rolled_dice(self.dice_bag.select_dice(3))
        self.scores = {} #player: score
        self.endgame = False #each player gets a turn until current_player == start_player
        for player in self.players:
            self.scores[player] = 0

    def _end_turn(self):
        self.players.append(self.players.pop(0))
    
    def _set_current_player(self):
        self.current_player = self.players[0]
    
    def _update_score(self, player, score_plus):
        self.scores[player] += score_plus
        if self.scores[player] >= 13:
            return "Endgame"
        else:
            return "Continue"

    def update_game(self, player, score_plus):
        #Add new score
        #Check for endgame
        #Pass game to next player unless Endgame and next player is Start Player (replace dice bag and rolled dice with fresh instances.)
        #If Game Over announce winner and scores.
        pass