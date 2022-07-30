from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Sergio Gonzalo Mejia Ramos'

doc = """

Double Auction Market with 2 Assets to trade

"""

class Constants(BaseConstants):
    name_in_url = 'auction'
    players_per_group = None
    num_rounds = 1
    
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    highest_bidder = models.IntegerField()
    highest_bid = models.CurrencyField(initial=0)

class Player(BasePlayer):
    
    def live_auction(self, data):
        print("Mandando..: ",data)
