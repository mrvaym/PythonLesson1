
from Card import Card

class Test_Card:
    def setup(self):
        a = Card(1, 8)
        b = Card(1, 4)
        c = Card(2, 8)


    def tearsdown(self):
        print('Test complete!')


    def test_Card(self):
        a = Card(1, 8)
        b = Card(1, 4)
        c = Card(2, 8)
        assert a.suit==1
        assert a.rank==8
        assert a.istrump==False
        assert str(a) == '♦A'
        assert a.higher(b)==True
        assert b.higher(a) == False
        assert b.lower(a)==True
        assert a.lower(b) == False
        assert a.beat(b) == True
        assert a.insuit(b) == True
        assert a.insuit(c) == False
        assert c.beat(a) == False
        c.istrump = True
        assert c.beat(a) == True

