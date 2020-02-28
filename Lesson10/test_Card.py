from Card import Card

class Test_Card:
    def setup(self):
        self.a = Card(1, 8)
        self.b = Card(1, 4)
        self.c = Card(2, 8)

    def tearsdown(self):
        print('Test complete!')

    def test___init__(self):
        assert self.a.suit==1
        assert self.a.rank == 8
        assert self.a.istrump == False
    def test___repr__(self):
        assert str(self.a) == '♦A'
    def test_higher(self):
        assert self.a.higher(self.b)==True
        assert self.b.higher(self.a) == False
    def test_lower(self):
        assert self.b.lower(self.a)==True
        assert self.a.lower(self.b) == False
    def test_beat(self):
        assert self.a.beat(self.b) == True
        assert self.c.beat(self.a) == False
        self.c.istrump = True
        assert self.c.beat(self.a) == True

    def test_insuit(self):
        assert self.a.insuit(self.b) == True
        assert self.a.insuit(self.c) == False




