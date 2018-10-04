import random
import logging


def d(count=1, max_value=6, min_value=1, modifier=0, drop_min=0, drop_max=0):
    dice = Dice(count, max_value, min_value, modifier)
    roll = list(dice.roll())
    roll.sort()
    return sum(roll[drop_min:drop_max])


class Dice:
    def __init__(self, count=1, max_value=6, min_value=1, modifier=0):
        self.count = count
        self.min_value = min_value
        self.max_value = max_value
        self.modifier = modifier

        self.value = None

    @property
    def name(self):
        return "{}d{} + {}".format(
            self.count,
            self.max_value,
            self.modifier
        )

    def roll(self):
        for _ in range(self.count):
            self.value = random.randint(self.min_value, self.max_value) + self.modifier
            logging.debug("%s = %d", self.name, self.value)
            yield self.value

    def __str__(self):
        return "{} = {}".format(self.name, self.value)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value
