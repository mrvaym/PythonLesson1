from random import shuffle
from Card import Card
from Deck import Deck

class Test_Deck:

    def setup(self):
        self.a = Deck(36)

    def tearsdown(self):
        print('Test complete!')

    def test_Deck(self):

        list_a=Deck()
        list_a.extend([self.a[0],self.a[1],self.a[2],self.a[3],self.a[4],self.a[5],self.a[6],self.a[7],self.a[8]])
        shuffle(list_a)
        min_card=list_a.min_in_list()
        max_card=list_a.max_in_list()
        assert Card(0,0).equal(min_card)
        assert Card(0,8).equal(max_card)
        list_b=Deck()
        list_b.extend([Card(1,4),Card(3,2),Card(2,7)])
        list_b.extend(list_a)
        assert list_b.insuit_in_list(Card(0,0))==list_a
