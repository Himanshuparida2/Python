import random
from card import Card
class Deck:
                NUMBER_OF_CARDS=52
                def __init__(self):
                                self.current_card=0
                                self._deck=[]
                                for i in range(self.NUMBER_OF_CARDS):
                                                face=Card.FACES[i%13]
                                                suit=Card.SUITS[i//13]
                                                self._deck.append(Card(face,suit))
                @property




                def deck(self):
                                return self._deck
                def deal_card(self):
                                try:
                                                card=self.deck[self.current_card]
                                                self.current_card+=1
                                                return card
                                except IndexError:
                                                return None
                def shuffle(self):
                                return random.shuffle(self.deck)
                def __str__(self):
                                s=''
                                for i,card in enumerate(self.deck):
                                                s+=f'{str(card):<20}'
                                                if(i+1)%4==0:
                                                                s+='\n'
                                return s
