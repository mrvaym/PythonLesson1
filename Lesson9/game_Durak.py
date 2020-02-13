from random import shuffle, choice


class Durak():
    def __init__(self, players={}, cards_in_deck=36):
        self.players = self.set_players(players)  # Список игроков
        self.deck = Deck(cards_in_deck)
        self.trump = ''  # Козырь
        self.cards_on_table = Deck()
        self.turn_num = 0
        self.attack_player = ''
        self.defense_player = ''

    def set_players(self, players):
        num = 1
        players_list = []
        for n in players.keys():  # создание колоды
            if players.get(n) == 0:
                i = Human(n)
            else:
                i = Computer(f'Компьютер {num}')
                num += 1
            players_list.append(i)
        return players_list

    def set_trump(self):  # определить козырную масть и переложить карту вниз
        trump_card = self.deck.pop()
        self.deck.insert(0, trump_card)
        self.trump = trump_card.suit
        for i in self.deck:  # Установка козырности для карт в колоде
            if i.suit == self.trump:
                i.istrump = True

    def deal(self):  # Раздача в начале игры
        for i in range(6):
            for n in self.players:
                n.set_hand(self.deck[len(self.deck) - 1])
                self.deck.pop()

    def whose_attack(self):
        card = Card(self.trump, 8)  # козырный туз
        if self.turn_num == 1:  # Если ход первый
            # Ходит у кого меньший козырь
            for n in self.players:
                trumps = n.hand_trumps()
                print(n, trumps)
                if trumps != []:
                    x = trumps.min_in_list()
                    if x.lower(card):
                        card = x
                        self.attack_player = n
            # все без козырей - жребий
            if self.attack_player == '':
                self.attack_player = choice(self.players)
                print('Жребий')
        # else:
        #     ''' Если ход не первый'''
        #     if self.players.index(self.attack_player) == len(self.players) - 1:
        #         self.attack_player = self.players[0]
        #     else:
        #         self.attack_player = self.players[self.players.index(self.attack_player) + 1]
        if self.players.index(self.attack_player) == len(self.players) - 1:
            self.defense_player = self.players[0]
        else:
            self.defense_player = self.players[self.players.index(self.attack_player) + 1]
        print(f'ходит {self.attack_player}')
        return True

    def play_card(self,card):
        if card:
            self.cards_on_table.append(card)
            defense_card = self.defense_player.defense(card)
            if defense_card:
                self.cards_on_table.append(defense_card)
                print(f'{self.defense_player} защищается {defense_card}')
            else:
                print('нечем бить')
                self.defense_player.abandon_defense(self.cards_on_table)
                print(f'{self.defense_player} взял, на руках {self.defense_player.get_hand()}')
                self.cards_on_table.clear()
        pass

    def play_game(self):

        shuffle(self.deck)
        # print(f'Перетасовали{self.deck}')
        self.set_trump()
        # print(f'Установили козыря{self.deck}')
        self.deal()
        for i in self.players:
            print(i, i.get_hand())

        for i in self.players:
            without_trumps = i.get_hand() - i.hand_trumps()

        print(f'Козырь {self.deck[0]} в колоде {len(self.deck)}')

        self.turn_num = 1
        self.whose_attack()

        attack_card = self.attack_player.attack()
        print(f'{self.attack_player} ходит {attack_card}')
        self.play_card(attack_card)

        # print(self.cards_on_table)
        pitch_player=self.attack_player
        if self.defense_player.get_hand() != [] or self.cards_on_table / 2 < 6:
            pitch_card = pitch_player.pitch(self.cards_on_table)
            self.play_card(pitch_card)
            pass
        # print(self.cards_on_table)
        pass


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

    def __str__(self):
        return self.__repr__()

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


class Player:
    def __init__(self, name):
        self.__hand = Deck()  # Карты на руках
        self.__name = name  # Имя игрока

    # def __repr__(self):
    #     return self.get_name()

    def __str__(self):
        return self.get_name()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_hand(self):
        return self.__hand

    def set_hand(self, card):
        self.__hand.append(card)

    def remove_hand(self, card):
        self.__hand.remove(card)

    def hand_trumps(self):  # Козыри на руках
        trumps = Deck()
        for i in self.__hand:
            if i.istrump:
                trumps.append(i)
        return trumps

    def attack(self):  # Ходим
        pass

    def deffense(self):  # Отбиваемся
        pass

    def pitch(self):  # Подкидываем
        pass

    def abandon_defense(self, card_on_table):
        self.__hand.extend(card_on_table)


class Human(Player):
    def __init__(self, name=''):
        super(Human, self).__init__(name)

    def attack(self):  # Ходим
        pass

    def deffense(self):  # Отбиваемся
        pass

    def pitch(self):  # Подкидываем
        pass


class Computer(Player):
    def __init__(self, name=''):
        super(Computer, self).__init__(name)

    def attack(self):  # Ходим

        without_trumps = self.get_hand() - self.hand_trumps()
        # print(without_trumps)
        if without_trumps != []:
            attack_card = without_trumps.min_in_list()  # Ходим наименьшей картой
        else:
            attack_card = self.hand_trumps().min_in_list()
        self.remove_hand(attack_card)
        return attack_card

    def defense(self, attack_card):  # Отбиваемся
        defense_card = ''
        insuit_cards = self.get_hand().insuit_in_list(attack_card)
        higher_cards = insuit_cards.higher_in_list(attack_card)
        trumps = self.hand_trumps()
        if higher_cards != []:
            defense_card = higher_cards.min_in_list()
        elif trumps != []:
            defense_card = trumps.min_in_list()
        else:
            return False  # нечем бить
        self.remove_hand(defense_card)
        return defense_card

    def pitch(self, cards_on_table):  # Подкидываем

        equal_cards = Deck()
        without_trumps = Deck()
        for i in cards_on_table:
            x = self.get_hand().equal_in_list(i)
            if x != []:
                equal_cards.extend(x)
        if equal_cards!=[]:
            without_trumps=equal_cards-self.hand_trumps()
            if without_trumps != []:
                pitch_card = without_trumps.min_in_list()
            else:
                pitch_card = equal_cards.min_in_list()
            print(pitch_card)
            return pitch_card
        else:
            return False

if __name__ == "__main__":
    game = Durak({'a': 1, 'b': 1, 'c': 1, 'd': 1})
    game.play_game()
