import random
import logging


def d(count=1, max_value=6, min_value=1, modifier=0, multiplier=1, drop_min=0, drop_max=0):
    dice = Dice(count, max_value, min_value, modifier)
    roll = list(dice.roll())
    roll.sort()
    return sum(roll[drop_min:drop_max]) * multiplier


class Dice:
    def __init__(
        self,
        count=1,
        max_value=6,
        min_value=1,
        modifier=0,
        multiplier=1,
        drop_min=0,
        drop_max=0,
        # throws=1,
        # characteristics=6,
        # group=1,
        # adjust=0.0,
        # points=0,
        # average_points=0,
        # keep_best=False,
        # max_characteristic=18,
    ):
        """
        Rolling dice
        :param count: number of dices
        :param max_value: max value of roll
        :param min_value: min value of roll
        :param modifier: roll modifier
        :param multiplier: roll multiplier
        :param drop_min: drop minimal dices
        :param drop_max: drop maximal dices
        """
        self.count = count
        self.min_value = min_value
        self.max_value = max_value
        self.modifier = modifier
        self.multiplier = multiplier
        self.drop_min = drop_min
        self.drop_max = drop_max

        self.value = None

    @property
    def name(self):
        """
        Dice name
        :return:
        """
        name = f"{self.count}d{self.max_value}"
        if self.modifier > 0:
            name = f"{name} + {self.modifier}"
        if self.multiplier > 1:
            name = f"({name}) * {self.multiplier}"
        return name

    def roll(self):
        """
        Roll next dice
        :return: roll result
        """
        for _ in range(self.count):
            self.value = random.randint(self.min_value, self.max_value)
            logging.debug("%s = %d", self.name, self.value)
            yield self.value

    def total(self):
        """
        Roll result
        :return:
        """
        rolls = list(self.roll())

        # Drop rolls
        rolls.sort()
        if self.drop_min:
            rolls = rolls[self.drop_min:]
        if self.drop_max:
            rolls = rolls[:-self.drop_max]

        # Apply modifier & multiplier
        self.value = (sum(rolls) + self.modifier) * self.multiplier
        logging.debug("%s = %d", self.name, self.value)
        return self.value

    def __str__(self):
        return "{} = {}".format(self.name, self.value)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value


class RollMethod:
    def __init__(
        self,
        method_id,
        name,
        *args,
        method_type=None,
        **kwargs,
    ):
        self.method_id = method_id
        self.name = name
        self.method_type = method_type
        self.dice = Dice(*args, **kwargs)
