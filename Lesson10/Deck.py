from Card import Card

class Deck(list):

    def __init__(self, cards_num=0):
        super(Deck, self).__init__()
        self.cards_num = cards_num
        if cards_num == 36:
            for n in range(4):  # создание колоды
                for i in range(9):
                    self.append(Card(n, i))
                    self.cards_num += 1

    def __add__(self, other):
        pass

    def __sub__(self, other):
        result = Deck()
        x = list(set(self) - set(other))
        result.extend(x)
        return result

    def min_in_list(self):
        ''' min значение в списке'''
        y = self[0]
        if self != []:
            for x in self:
                if x.lower(y):
                    y = x
            return y
        else:
            return []

    def max_in_list(self):
        ''' max значение в списке'''
        y = self[0]
        if self != []:
            for x in self:
                if x.higher(y):
                    y = x
                else:
                    continue
            return y
        else:
            return []

    def insuit_in_list(self, card):
        y = Deck()
        for x in self:
            if x.insuit(card):
                y.append(x)
        return y

    def higher_in_list(self, card):
        y = Deck()
        for x in self:
            if x.higher(card):
                y.append(x)
        return y

    def lower_in_list(self, card):
        y = Deck()
        for x in self:
            if x.lower(card):
                y.append(x)
        return y

    def equal_in_list(self, card):
        y = Deck()
        for x in self:
            if x.equal(card):
                y.append(x)
        return y