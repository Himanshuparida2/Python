class Card:
                FACES=['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']
                SUITS=['HEARTS','SPADES','DIAMONDS','CLUBS']
                def __init__(self,face,suit):
                                self.face=face
                                self.suit=suit
                def __str__(self):
                                return f'{self.face} of {self.suit}'
                @property
                def image_name(self):
                                return str(self).replace(' ','_')+'.png'
