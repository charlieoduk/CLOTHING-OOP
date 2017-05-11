class Clothes(object):

    def __init__(self):
       pass

    def sale(self, pieces):
        self.stock -= pieces
        return self.stock

class Tees(Clothes):
    def __init__(self):
        Clothes.__init__(self)
        self.stock = 47

    def sale(self, pieces):
        if pieces > self.stock:
            return "Sorry We don't have enough stock"
        elif pieces < 0:
            return "Invalid sale"
        Clothes.sale(self, pieces)
        print('You sold {} Tee(s) and you have {} left in stock'.format(pieces, self.stock))
        return self.stock

class Polos(Clothes):
    def __init__(self):
        Clothes.__init__(self)
        self.stock = 100

    def sale(self, pieces):
        if pieces > self.stock:
            return "Sorry We don't have enough stock"
        elif pieces < 0:
            return "Invalid sale"
        Clothes.sale(self, pieces)
        print('You sold {} polo(s) and you have {} left in stock'.format(pieces,self.stock))
        return self.stock
