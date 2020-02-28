
class Card():
    __SUITS = {0: '♥', 1: '♦', 2: '♣', 3: '♠'}  # hearts, clubs, diamonds, spades
    __RANK = {0: '6', 1: '7', 2: '8', 3: '9', 4: '10', 5: 'J', 6: 'Q', 7: 'K', 8: 'A'}  # старшинство карт
    def __init__(self, suit=0, rank=0):
        self.rank = rank  # Достоинство карты
        self.suit = suit
        self.istrump = False
    def __repr__(self):
        suit = str(self.__SUITS.get(self.suit))
        rank = str(self.__RANK.get(self.rank))
        return suit + rank

    def higher(self, other):  # Больше ли по достоинству карта другой
        return True if self.rank > other.rank else False
    def lower(self, other):  # Меньше ли по достоинству карта другой
        return True if self.rank < other.rank else False
    def equal(self, other):  # Равна ли по достоинству карта другой
        return True if self.rank == other.rank else False
    def insuit(self, other):  # Одинаковая масть карты с другой
        return True if self.suit == other.suit else False
    def beat(self, other):  # Бьёт ли карта другую
        if self.suit == other.suit:
            if self.rank > other.rank:
                return True
        else:
            if self.istrump == True:
                return True
            else:
                return False

