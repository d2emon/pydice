import random
from .dice import Dice


class RollMethod:
    title = "Roll"

    dices = 1
    min_value = 1
    max_value = 6
    modifier = 0

    drop_lowest = 0
    drop_upper = 0
    throws = 1
    keep_best = False
    characteristics = 6
    max_characteristics = 18  # !!!

    points = None  # ???

    def __init__(self):
        self.dice = Dice(
            count=self.dices,
            min_value=self.min_value,
            max_value=self.max_value,
            modifier=self.modifier,
        )

        self.group = 0  # ???
        self.glbrndfact = .0  # ???

        self.average_points = 0  # ???
        self.keep_best = False  # ???
        self.mtdtype = 0  # ???

        self.rolls = []

    def throw(self, throws_count=None):
        def make_throw():
            dices = list(self.dice.roll())
            dices.sort()
            dices = dices[self.drop_lowest:-self.drop_upper]
            return sum(dices)

        throws_count = throws_count or self.throws
        throws = [make_throw() for _ in range(throws_count)]
        throws.sort()
        return throws

    def roll(self):
        if self.keep_best:
            throws = self.throw()[:self.characteristics]
            random.shuffle(throws)
            return throws
        return [self.throw()[0] for _ in range(self.characteristics)]
