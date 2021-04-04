#!/bin/env python
import re
import random


class dice:
#Never expose this class through a service. Its too insecure.
#But you can use it safely with known input values. Or as a part
#of a client application with known input values like in this case.
    def __init__(self, str_in=False):
        self.debug = False
        if str_in:
            self.string = str_in
        else:
            self.string = '1'

    def roll(self, str_in=False):
        if str_in:
            self.string = str_in
        #replace die rolls with generated numbers
        self.parse()
        if not re.search(r'[^0-9(*/)dD+-]', self.string):
            return eval(self.string)
        else:
            return 0

    def parse(self):
        #regex match each die and replace with this function
        self.string = re.sub(r'\d*d\d+',
                             lambda x: self.gen_die(x),self.string)
        if self.debug:
            print("|%s|"% self.string)

    def gen_die(self,die):
        # take first number and generate a list
        if self.debug:
            print("hi %s"%die.group(0))
        dice_info = re.search(r'(\d*)d(\d+)', die.group(0))
        if dice_info.group(1):
            num_die = int(dice_info.group(1))
        else:
            num_die = 1
        sides = int(dice_info.group(2))
        if self.debug:
            print("num_die:%s \nsides:%s" % (num_die, sides))
        return str(sum([random.randint(1,sides) for x in range(num_die)]))
