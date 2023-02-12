#!/usr/bin/python

from lib.dice import Dice_factory
import random
import re


class Preset_data():
    def __init__(self):
        self.cr = [
            (2, 10, 6, 3, 1, 13, 10),
            (2, 13, 85, 3, 14, 13, 200),
            (2, 13, 100, 3, 20, 13, 450),
            (2, 13, 115, 4, 26, 13, 700),
            (2, 14, 130, 5, 32, 14, 1100),
            (3, 15, 145, 6, 38, 15, 1800),
            (3, 15, 160, 6, 44, 15, 2300),
            (3, 15, 175, 6, 50, 15, 2900),
            (3, 16, 190, 7, 56, 16, 3900),
            (4, 16, 205, 7, 62, 16, 5000),
            (4, 17, 220, 7, 68, 16, 5900),
            (4, 17, 235, 8, 74, 17, 7200),
            (4, 17, 250, 8, 80, 17, 8400),
            (5, 18, 265, 8, 86, 18, 10000),
            (5, 18, 280, 8, 92, 18, 11500),
            (5, 18, 295, 8, 98, 18, 13000),
            (5, 18, 310, 9, 104, 18, 15000),
            (6, 19, 325, 10, 110, 19, 18000),
            (6, 19, 340, 10, 116, 19, 20000),
            (6, 19, 355, 10, 122, 19, 22000),
            (6, 19, 400, 10, 140, 19, 25000),
            (7, 19, 445, 11, 158, 20, 33000),
            (7, 19, 490, 11, 176, 20, 41000),
            (7, 19, 535, 11, 194, 20, 50000),
            (7, 19, 580, 12, 212, 21, 62000),
            (8, 19, 625, 12, 230, 21, 75000),
            (8, 19, 670, 12, 248, 21, 90000),
            (8, 19, 715, 13, 266, 22, 105000),
            (8, 19, 760, 13, 284, 22, 120000),
            (9, 19, 805, 13, 302, 22, 135000),
            (9, 19, 850, 14, 320, 23, 155000)]
        self.breakDown = (
                        'profBonus',
                        'ac',
                        'hp',
                        'atkBonus',
                        'damPerRound',
                        'saveDC',
                        'exp')

    def get(self, cr):
        stats = {}
        temp = self.cr[cr]
        i = 0
        for stat in self.breakDown:
            stats[stat] = temp[i]
            i += 1
        return stats


class Template_factory():
    def _calc_maValue(self, sect):
        maValue = []
        for option in self.encounter.get_option(sect):
            # print(option)
            if 'multiattack' in option:
                print('multiattack activated')
                maValue = option.split(':')[1].strip().split(',')
                print(f'maValue is: {maValue}')
                for i in maValue:
                    i = i.strip()
        return maValue

    def _CR_adjustment_for_damage(self, sect, maValue):
        high_dpr = self._calc_high_dpr(sect, maValue)
        # force template actions and damage rolls to more closely
        # match the requested Challenge Rating
        current_cr = 0
        for row in self.presets.cr:
            if row[4] < high_dpr:
                current_cr += 1
        # this recprents the direction current dpr must travel in
        # in order to match target challenge rating.
        # reduce the target by maValue divisor to normalize multiAttack.
        ma_dmg_diff = ((self.presets.cr[self.encounter.get_option('cr')][4] //
                        (len(maValue) or 1)) -
                       self.presets.cr[current_cr][4])

        dmg_diff = ((self.presets.cr[self.encounter.get_option('cr')][4] //
                     (len(maValue) or 1)) -
                    self.presets.cr[current_cr][4])

        # regular attack adjustment dpr
        replace = list()
        for option in self.encounter.get_option(sect):
            maFlag = False
            for act in maValue:
                if act in option:
                    maFlag = True
            if maFlag:
                option = self._update_damage(ma_dmg_diff, option)
            else:
                option = self._update_damage(dmg_diff, option)
            # print(f"after update {option}")
            replace.append(option)
        # print("cows: {}".format(replace))
        self.encounter.set_option(sect, replace)

    def _calc_high_dpr(self, sect, maValue):
        high_dpr = 0
        # print("_calc_high_dpr reports: {}".format(maValue))
        for option in self.encounter.get_option(sect):
            test_dpr = self._find_damage(option)
            if test_dpr:
                dpr = self.dice_caddy.get_average(test_dpr)
                if dpr > high_dpr:
                    high_dpr = dpr
        high_dpr = high_dpr // (len(maValue) or 1)
        return high_dpr

    def _calculate_dpa(self, sect, maValue):
        # search all options for multiattack
        dpr = self.encounter.get_option('damPerRound')
        # damage per action
        if maValue:
            dpa = dpr / len(maValue)
        else:
            dpa = dpr
        return dpa, maValue

    def _update_action_attack_mod(self, text):
        attack_mod = self.presets.get(
            self.encounter.get_option('cr'))['atkBonus']
        return self.pattern_attack_mod.sub('+'+str(attack_mod), text)

    def _update_damage(self, damage_diff, text):
        'take damage_diff and applies it'
        dice_caddy = dice()
        m1 = self.pattern_dmg_die.search(text)
        m2 = self.pattern_elem_dmg_die.search(text)
        dam1, dam2 = None, None
        # print("ud_7 {},{}".format(m1, m2))
        # TODO check the idea behind damage_diff
        # should be a range of numbers between -1000 and 1000
        # and reprepsent the direction to skew the dice to match
        # the target CR
        # if the damage needs to move higher
        if damage_diff > 0 and m1:
            # And there is elemental damage to account for
            # print(m1)
            dam1 = self.dice_caddy.get_average(m1.group(0))
            if m2:
                # print(m2)
                dam2 = self.dice_caddy.get_average(m2.group(0))
                # elemental damage and regular damage are seperate
                # but both contribute to this weapon
                dam1 = dam1 + (damage_diff // 2)
                dam2 = dam2 + (damage_diff // 2)

                dam1 = dice_caddy.to_dice(dam1)
                dam2 = dice_caddy.to_dice(dam2)
                text = self.pattern_dmg_die.sub(str(dam1), text)
                # print("positive elemental damage: {}".format(text))
                return self.pattern_elem_dmg_die.sub(str(dam2), text)
            else:
                dam1 = dam1 + damage_diff
                dam1 = dice_caddy.to_dice(dam1)
                # print("positive damage {}".format(text))
                return self.pattern_dmg_die.sub(str(dam1), text)
        # if the damage needs to move lower
        elif damage_diff < 0 and m1:
            dam1 = self.dice_caddy.get_average(m1.group(0))
            # if there was elemental damage on this weapon as well.
            if m2:
                if (dam1 + (damage_diff // 2)) > 0:
                    dam1 = dam1 + (damage_diff // 2)
                dam2 = self.dice_caddy.get_average(m2.group(0))
                if (dam2 + (damage_diff // 2)) > 0:
                    dam2 = dam2 - (damage_diff // 2)
                dam1 = dice_caddy.to_dice(dam1)
                dam2 = dice_caddy.to_dice(dam2)
                text = self.pattern_dmg_die.sub(str(dam1), text)
                return self.pattern_elem_dmg_die.sub(str(dam2), text)
            else:
                if (dam1 + damage_diff) > 0:
                    dam1 = dam1 + damage_diff
                dam1 = dice_caddy.to_dice(dam1)
                return self.pattern_dmg_die.sub(str(dam1), text)
        else:
            return text

    def _find_damage(self, text):
        # print("_find_damage reports: {}".format(text))
        m1 = self.pattern_dmg_die.search(text)
        m2 = self.pattern_elem_dmg_die.search(text)
        dam1, dam2 = None, None
        if m1:
            dam1 = re.sub('d{|}', '', ''.join(m1.group()))
        if m2:
            dam2 = re.sub('e{|}', '', ''.join(m2.group()))
        if m1 and m2:
            # print('damage add')
            # print(dam1 + dam2)
            return dam1 + dam2
        if not m2 and m1:
            # print('only dam1')
            # print(dam1)
            return dam1
        if not m1 and m2:
            # print('only elemental damage')
            # print(dam2)
            return dam2
        # print('fall out')
        return None

    def _damage_size_upgrades(self, sect, size):
        size = size.strip()
        newSection = list()
        for text in self.encounter.get_option(sect):
            dice = [2, 4, 6, 8, 10, 12, 20, 100]
            m = self.pattern_dmg_die.search(text)
            if m:
                sizeMod = 0
                # print(f"inner size: {size}")
                if size == 'large':
                    # print("large active")
                    sizeMod = 1
                if size == 'huge':
                    # print("huge active")
                    sizeMod = 2
                if size in 'gargantuan':
                    # print("gargantuan active")
                    sizeMod = 3
                # find the sides of the die being used.
                # print("in: {}".format(m.group(1)))
                sides = self.pattern_die_sides.search(m.group(1))
                # print(f"out: {sides.group(1)}")
                index = dice.index(int(sides.group(1))) + sizeMod
                # print(f"Index {index}")
                # upgrade the sides of the die based on the size of the monster
                # if calculated index does not over-shoot the length of dice
                if index < len(dice) - 1:
                    sides = dice[index]
                # print(m.group(1), sides)
                # put the upgraded die back in the damage calculation.
                new_damage_die = self.pattern_die_sides.sub(str(sides),
                                                            text,
                                                            count=1)
                # print(f"new dmg die {new_damage_die}")
                # print(f"text: {text}")
                newSection.append(new_damage_die)
            else:
                newSection.append(text)
        # print(newSection)
        self.encounter.set_option(sect, newSection)
