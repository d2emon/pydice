#! /usr/bin/env python
# -*- coding:utf-8 -*-


import random
import logging


def byPercent(cases=dict()):
    percents = list(cases.keys())
    percents.sort()

    p = random.randrange(100)
    logging.debug("%d%%", p)
    for i in percents:
        if p < i:
            return cases[i]
