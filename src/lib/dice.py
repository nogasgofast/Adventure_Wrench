#!/bin/env python
from __future__ import division
from pyparsing import (Literal, CaselessLiteral, Word, Combine, Group,
                       Optional, ZeroOrMore, Forward, nums, alphas, oneOf)
import math
import operator
import re
import random


class dice:
    # Never expose this class through a service. Its too insecure.
    # But you can use it safely with known input values. Or as a part
    # of a client application with known input values like in this case.
    def __init__(self, str_in=False):
        self.nsp = NumericStringParser()
        self.debug = False
        if str_in:
            self.string = str_in
        else:
            self.string = '1'

    def roll(self, str_in=False):
        if str_in:
            self.string = str_in
        # replace die rolls with generated numbers
        self.parse()
        if not re.search(r'[^0-9(*/)dD+-]', self.string):
            return int(self.nsp.eval(self.string))
        else:
            return 0

    def parse(self):
        # regex match each die and replace with this function
        self.string = re.sub(r'\d*d\d+',
                             lambda x: self.gen_die(x), self.string)
        if self.debug:
            print("|{}|".format(self.string))

    def gen_die(self, die):
        # take first number and generate a list
        if self.debug:
            print("hi {}".format(die.group(0)))
        dice_info = re.search(r'(\d*)d(\d+)', die.group(0))
        if dice_info.group(1):
            num_die = int(dice_info.group(1))
        else:
            num_die = 1
        sides = int(dice_info.group(2))
        if self.debug:
            print("num_die:%s \nsides:%s" % (num_die, sides))
        return str(sum([random.randint(1, sides) for x in range(num_die)]))

    def get_average(self, diceExpression):
        # breaks out the multiplier and die and averages
        # the die and multiplies the result.
        cleanExpression = re.sub('[de]{|}', '', diceExpression)
        # print("TEST1: {}".format(cleanExpression))
        m = re.match(r'(\d+)?d(\d+)([+-]\d+)?', cleanExpression)
        # print("TEST2: {} {} {}".format(m.group(1),
        #                                m.group(2),
        #                                m.group(3)))
        average = (int(m.group(1)) // 2) + 1
        if m.group(1):
            average = average * int(m.group(1))
        if m.group(3):
            average = average + int(m.group(3))
        return average

    def to_dice(self, Max=False):
        'use largest die possible, do not break into smaller die'
        if Max < 2:
            return Max
        dice = (100, 20, 12, 10, 8, 6, 4)
        out = None
        for die in dice:
            die_avg = (die // 2) + 1
            numDice = Max // die_avg
            if numDice >= 1:
                Max = Max - (die_avg * numDice)
                out = '{}d{}'.format(numDice, die)
                if Max <= 0:
                    return out
                else:
                    out = f"{out}+{Max}"
                    return out

# __author__ = 'Paul McGuire'
# __version__ = '$Revision: 0.0 $'
# __date__ = '$Date: 2009-03-20 $'
# __source__ = '''http://pyparsing.wikispaces.com/file/view/fourFn.py
# http://pyparsing.wikispaces.com/message/view/home/15549426
# '''
# __note__ = '''
# All I've done is rewrap Paul McGuire's fourFn.py as a class, so I can use it
# more easily in other places.
# '''


class NumericStringParser(object):
    '''
    Most of this code comes from the fourFn.py pyparsing example

    '''

    def pushFirst(self, strg, loc, toks):
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        if toks and toks[0] == '-':
            self.exprStack.append('unary -')

    def __init__(self):
        """
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        """
        point = Literal(".")
        e = CaselessLiteral("E")
        fnumber = Combine(Word("+-" + nums, nums) +
                          Optional(point + Optional(Word(nums))) +
                          Optional(e + Word("+-" + nums, nums)))
        ident = Word(alphas, alphas + nums + "_$")
        plus = Literal("+")
        minus = Literal("-")
        mult = Literal("*")
        div = Literal("/")
        lpar = Literal("(").suppress()
        rpar = Literal(")").suppress()
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        pi = CaselessLiteral("PI")
        expr = Forward()
        atom = ((Optional(oneOf("- +")) +
                 (ident + lpar + expr +
                  rpar | pi | e | fnumber).setParseAction(self.pushFirst))
                | Optional(oneOf("- +")) + Group(lpar + expr + rpar)
                ).setParseAction(self.pushUMinus)
        # by defining exponentiation as "atom [ ^ factor ]..." instead of
        # "atom [ ^ atom ]...", we get right-to-left exponents,
        # instead of left-to-right
        # that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor << atom + \
            ZeroOrMore((expop + factor).setParseAction(self.pushFirst))
        term = factor + \
            ZeroOrMore((multop + factor).setParseAction(self.pushFirst))
        expr << term + \
            ZeroOrMore((addop + term).setParseAction(self.pushFirst))
        # addop_term = ( addop + term ).setParseAction( self.pushFirst )
        # general_term = term + ZeroOrMore( addop_term ) |
        # OneOrMore( addop_term)
        # expr <<  general_term
        self.bnf = expr
        # map operator symbols to corresponding arithmetic operations
        epsilon = 1e-12
        self.opn = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "^": operator.pow}
        self.fn = {"sin": math.sin,
                   "cos": math.cos,
                   "tan": math.tan,
                   "exp": math.exp,
                   "abs": abs,
                   "trunc": lambda a: int(a),
                   "round": round,
                   "sgn": lambda a: abs(a) > epsilon and cmp(a, 0) or 0}

    def evaluateStack(self, s):
        op = s.pop()
        if op == 'unary -':
            return -self.evaluateStack(s)
        if op in "+-*/^":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        elif op == "PI":
            return math.pi  # 3.1415926535
        elif op == "E":
            return math.e  # 2.718281828
        elif op in self.fn:
            return self.fn[op](self.evaluateStack(s))
        elif op[0].isalpha():
            return 0
        else:
            return float(op)

    def eval(self, num_string, parseAll=True):
        self.exprStack = []
        results = self.bnf.parseString(num_string, parseAll)
        val = self.evaluateStack(self.exprStack[:])
        return val