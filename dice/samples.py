from .dice import Dice
from .method import RollMethod


class Roll3d6Twice(RollMethod):
    title = "3D6 Twice"

    dices = 3
    max_value = 6

    throws = 2


class Roll4d6TwiceDropLowest(RollMethod):
    title = "4D6 Twice drop lowest"

    dices = 4
    max_value = 6

    drop_lowest = 1
    drop_upper = 0
    throws = 2


class AverageCharacOfClass(RollMethod):
    title = "Average charac of class with 30% adjust + or -"

    dices = 1
    max_value = 8

    drop_lowest = 0
    drop_upper = 0


class Roll3d6TenTimesKeepBest6(RollMethod):
    title = "3D6 Ten times keep best 6"

    dices = 3
    max_value = 6

    throws = 10
    keep_best = True


class Roll3d6TwelveTimesKeepBest6(RollMethod):
    title = "3D6 Twelve times keep best 6"

    dices = 3
    max_value = 6

    drop_lowest = 0
    drop_upper = 0
    throws = 12
    keep_best = True


class Roll5D6OnceDropLowests(RollMethod):
    title = "5D6 Once drop lowests"

    dices = 5
    max_value = 6

    drop_lowest = 2


class Roll5D6TwiceDropLowests(RollMethod):
    title = "5D6 Twice drop lowests"

    dices = 5
    max_value = 6

    drop_lowest = 2
    throws = 2


class RollDarksun(RollMethod):
    title = "4D4+4 (Darksun)"

    dices = 4
    max_value = 4
    modifier = 1


class RollDarksunNPC(RollMethod):
    title = "5D4 (Darksun NPC)"

    dices = 5
    max_value = 4
    max_characteristics = 20


class Roll6D4DropLowestDarksunNPC(RollMethod):
    title = "6D4 Drop Lowest (Darksun NPC)"

    dices = 6
    max_value = 4

    drop_lowest = 1
    max_characteristics = 20

# Alternity

class RollMin4Max14TwoThrows(RollMethod):
    title = "Min 4 max 14, two throws"

    dices = 2
    max_value = 6

    throws = 2
    max_characteristics = 14
    modifier = 2


class Roll60PointsToDistribute(RollMethod):
    title = "60 points to distribute"

    min_value = 4
    max_value = 14

    max_characteristics = 14
    points = 60


class Roll64PointsToDistribute(RollMethod):
    title = "64 points to distribute"

    min_value = 4
    max_value = 14

    max_characteristics = 14
    points = 64


"""


"""