#!/usr/bin/python


from lib.dice import dice
import random
import configparser
import json
import os
import re


class Encounter():
    def __init__(self):
        self.data = {
            'abilities': [],
            'actions': [],
            'ac': 10,
            'atk_weapon': [],
            'atkBonus': 0,
            'attacks': [],
            'attributes': [],
            'bs': 0,
            # such as Construct, Beast, or other.
            'class': '',
            'cr': 0,
            'cond_immunity': [],
            'DSF': 0,
            'DSS': 0,
            'dam_resistance': [],
            'dam_vulnerable': [],
            'dam_immunity': [],
            'damPerRound': 0,
            'dr': 0,
            'exp': 0,
            'groupOf': 1,
            'groupHP': [],
            'maxHP': 1,
            'hp': 1,
            'initiative': 1,
            'items': [],
            'locomotion': [],
            'loot': [],
            'misc_actions': [],
            'motivation': [],
            'name': '',
            'profBonus': 0,
            'saveDC': 0,
            'senses': [],
            'size': [],
            'speed': 30,
            'spells': [],
            'STR': 8,
            'DEX': 8,
            'CON': 8,
            'WIS': 8,
            'INT': 8,
            'CHA': 8,
            'type': 'creature',
            'ws': 0}

    def copy(self):
        'copy is a value copy instead of a reference copy'
        XEncounter = Encounter()
        XEncounter.data = self.data.copy()
        return XEncounter

    # def import_cr_dissabled(self,TargetCR):
    #     'import from a template main stats for this TargetCR'
    #     template = challengRating()
    #     stats = template.get(TargetCR)
    #     for stat in template.breakDown:
    #         self.data[stat] = stats[stat]
    #
    # def import_options_dissabled(self,options):
    #     'imports from lists of optional changes to this encounter'
    #     enc_type = self.data['type']
    #     attributes = preset_data().get_options(enc_type,'attribute')
    #     attacks = preset_data().get_options(enc_type,'weapon')
    #     misc  = preset_data().get_options(enc_type,'misc')
    #     for opt in options:
    #         for attribute in attributes:
    #             if opt in attribute[0]:
    #                 self.data['abilities'].append(attribute[0])
    #         pos_atk = opt[0:-8]
    #         for weapon in attacks:
    #             if pos_atk in weapon[2:]:
    #                 self.import_attacks(weapon)
    #         pos_misc = opt[0:-5]
    #         for action in misc:
    #             if pos_misc in action[2:]:
    #                 self.import_misc_actions(action)

    def print_self(self):
        print(json.dumps(self.data, sort_keys=True,
                         indent=4, separators=(',', ': ')))

    def set_option(self, option, val):
        self.data[option] = val

    def append_option(self, option, val):
        self.data[option].append(val)

    def get_option(self, option):
        return self.data[option]

    # def import_attacks_dissabled(self,opt):
    #     if not opt in self.data['atk_weapon']:
    #         self.data['atk_weapon'].append(opt)
    #
    # def import_misc_actions_dissabled(self,misc):
    #     if not misc in self.data['misc_actions']:
    #         self.data['misc_actions'].append(misc)
    #
    # def import_stats_dissabled(self,STR,DEX,CON,WIS,INT,CHA):
    #     self.data['stats'] = {'STR':STR,
    #                       'DEX':DEX,
    #                       'CON':CON,
    #                       'WIS':WIS,
    #                       'INT':INT,
    #                       'CHA':CHA}

    def sqrt(self, num):
        if (num // 2) > 1:
            return num // 2
        else:
            return 0

    def to_string(self):
        dice_caddy = dice()
        options = []
        loadData = [
            'class',
            'damPerRound',
            'dr',
            'exp',
            'saveDC',
            'loot',
            'motivation',
            'senses']
        for catagory in loadData:
            # print(self.data[catagory])
            if self.data[catagory]:
                options.append('%s: %s' % (
                    catagory,
                    self.data[catagory]))

        name_size_type = (
            '{}\n'
            '{} {}\n'.format(
                self.data['name'],
                self.data['size'],
                self.data['class']))
        header = (
            'Armor Class: {}\n'
            'Max HP: {}({})\n'
            'Speed: {}\n'
            'CR: {}\n'
            'Exp: {}\n'
            '{}\n'.format(
                self.data['ac'],
                self.data['maxHP'],
                dice_caddy.to_dice(self.data['maxHP']),
                ', '.join([sp for sp in self.data['locomotion'] if sp != 0]),
                self.data['cr'],
                self.data['exp'],
                ''.join(self.data['attributes'])))
        stats = (
            '  STR       DEX       CON      WIS       INT       CHA\n'
            '{}({})    {}({})    {}({})    '
            '{}({})    {}({})    {}({})\n'.format(
                self.data['STR'],
                ((self.data['STR'] - 10) // 2),
                self.data['DEX'],
                ((self.data['DEX'] - 10) // 2),
                self.data['CON'],
                ((self.data['CON'] - 10) // 2),
                self.data['WIS'],
                ((self.data['WIS'] - 10) // 2),
                self.data['INT'],
                ((self.data['INT'] - 10) // 2),
                self.data['CHA'],
                ((self.data['CHA'] - 10) // 2)))
        inventory = (
            'Inventory:\n'
            '\t{}\n'.format('\n\t'.join(self.data['items'])))

        actions = (
            'Actions:\n'
            '\t{}\n'.format('\n\t'.join(self.data['actions'])))

        spells = (
            'SpellCasting:\n'
            '{}\n'.format('\n\n'.join(self.data['spells'])))
        output = '\n'.join([name_size_type, header, stats,
                            inventory, actions, spells])
        return output


class Preset_data():
    def __init__(self):
        config_files = os.listdir('config/')
        # print(config_files)
        self.data = {}
        self.template_names = []
        for config in config_files:
            self.template_names.append(config)
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
                        'maxHP',
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

    def templates_that_have(self, type, section):
        'reads config meta data and provides lists'
        ans = []
        for config in self.template_names:
            tmp = configparser.ConfigParser(allow_no_value=True,
                                            interpolation=None)
            tmp.read('config/{}'.format(config))
            if not tmp['template'].get('type') or \
                    type in tmp['template']['type']:
                if tmp.has_section(section):
                    ans.append((config, tmp['template']['name']))
        return ans


class Template_factory():
    def __init__(self, encounter):
        'save encounter to be minipulated'
        self.presets = Preset_data()
        self.dice_caddy = dice()
        self.encounter = encounter
        self.raw_templates = list()
        self.pattern_attack_mod = re.compile(r'a{}')
        self.pattern_stat_mod = re.compile(r'(\w{3})([+-])(\d+)')
        self.pattern_dice_table_option = re.compile(r'^(\d+)(-(\d+))?\s+')
        self.pattern_import_template = re.compile(r'import (\w+\.tmp)')
        self.pattern_random_table_option = re.compile(r'^r\s+')
        self.pattern_dc_replacement = re.compile(r'dc{(d*)}')
        self.pattern_dmg_die = re.compile(r'd{(\d?d\d+)}')
        self.pattern_elem_dmg_die = re.compile(r'e{(\d?d\d+)}')
        self.pattern_die_sides = re.compile(r'(?<=d)(\d+)')

    def read(self, name):
        # we must never add a config that's already been added once.
        # this ensures we have no config loops, or dependency loops.
        for tmp in self.raw_templates:
            if name in tmp['template']['name']:
                print("templates can only be imported once!"
                      "Ignoring: {}".format(name))
                return None
        self.raw_templates.append(
            configparser.ConfigParser(allow_no_value=True,
                                      interpolation=None))
        # print('config/{}'.format(name))
        self.raw_templates[-1].read('config/{}'.format(name))
        # print(self.raw_templates[-1].sections())

    def read_list(self, name):
        with open('./config/{}.lst'.format(name)) as f:
            return f.read().splitlines()

    def apply(self, dmg_calc_method, level=0):
        rt = self.raw_templates[-1]
        # print('start application')
        sections = rt.sections()

        live_sections = ['attributes', 'items', 'actions', 'spells']
        for sect in live_sections:
            if sect in sections:
                all_keys = list(rt[sect].keys())
                # print('start ak: {}'.format(all_keys))
                # check for template includes
                all_keys_itr = all_keys
                for key in all_keys_itr:
                    is_import = self.pattern_import_template.match(key)
                    if is_import:
                        self.read(is_import.group(1))
                        self.apply(dmg_calc_method, level + 1)
                        all_keys.remove(key)
                # print('after tmp includes ak: {}'.format(all_keys))
                # check for random table
                if 'random' in all_keys:
                    all_keys.remove('random')
                    all_keys = self._read_random_table(all_keys)
                # print('after random table ak: {}'.format(all_keys))
                # check for a roll table.
                if 'roll' in all_keys:
                    # check for a dice table
                    all_keys = self._read_dice_table(rt, sect, all_keys)
                # print('after roll table ak: {}'.format(all_keys))
                # just save the keys in the right sections as they were written
                for option in all_keys:
                    if rt[sect][option] is None:
                        self.encounter.append_option(
                            sect,
                            "{}".format(option))
                    else:
                        self.encounter.append_option(
                            sect,
                            "{}: {}".format(option,
                                            rt[sect][option]))
        # this is designed to only run after all recursions have
        # been considered.
        if level == 0:
            # print('starting consideration ')
            size = self.encounter.get_option('size')
            # print(f"my size is: {size}")
            for sect in live_sections:
                self._stat_commands_apply(sect)
                maValue = self._calc_maValue(sect)
                # print(f"damage_calc_method={dmg_calc_method}")
                if dmg_calc_method:
                    self._CR_adjustment_for_damage(sect, maValue)
                else:
                    self._damage_size_upgrades(sect, size)

                self._spell_save_dc_replace(sect)
                # do some value clean up to remove the last bits of
                # left over syntax from the display
                remove = list()
                replace = list()
                for option in self.encounter.get_option(sect):
                    if self.pattern_stat_mod.match(option):
                        remove.append(option)
                    option = self.pattern_random_table_option.sub('', option)
                    option = self.pattern_dice_table_option.sub('', option)
                    option = self._update_action_attack_mod(option)
                    replace.append(option)
                # print("value cleanup: {}".format(replace))
                self.encounter.set_option(sect, replace)
                for item in remove:
                    self.encounter.get_option(sect).remove(item)

    def _spell_save_dc_replace(self, sect):
        replace = list()
        # spell save dc replacement for target cr
        for option in self.encounter.get_option(sect):
            # print("books: {}".format(option))
            m = self.pattern_dc_replacement.search(option)
            if m:
                option = self.pattern_dc_replacement.sub(
                    'dc {}'.format(str(
                        self.encounter.get_option('saveDC'))),
                    option)
                replace.append(option)
            else:
                replace.append(option)
        # print("after spell save cd replacement: {}".format(replace))
        self.encounter.set_option(sect, replace)

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

    def _stat_commands_apply(self, sect):
        # checks for the existance of stat commands and applies them.
        # print('section {}'.format(sect))
        for option in self.encounter.get_option(sect):
            # print('considering: {}'.format(option))
            if self._read_stat_command(option):
                # print(option)
                self.encounter.get_option(sect).remove(option)

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

    def _read_stat_command(self, text):
        stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        stat_mod = self.pattern_stat_mod.match(text)
        if stat_mod:
            stat_name = stat_mod.group(1).upper()
            # print('stat name: {}'.format(stat_name))
            if stat_name in stats:
                stat_value = self.encounter.get_option(stat_name)
                stat_value = (int(stat_value) +
                              int(stat_mod.group(2) +
                              stat_mod.group(3)))
                self.encounter.set_option(stat_name, stat_value)
                return True
        return None

    # TODO: One of my attacks dissappeared and I don't know why
    def _read_random_table(self, items):
        r_table = list()
        not_r_table = list()
        for i in items:
            if self.pattern_random_table_option.match(i):
                r_table.append(i)
            else:
                not_r_table.append(i)
        answer = list()
        length = len(r_table)
        if length:
            last = length - 1
        tries = random.randrange(1, last)
        while tries >= 0:
            index = random.randrange(0, length)
            answer.append(r_table.pop(index))
            length = length - 1
            tries = tries - 1
        return answer.append(not_r_table)

    def _read_dice_table(self, raw_templates, sect, item_list):
        'reads roll tables and selects correct items from a template or list'
        roll = self.dice_caddy.roll(raw_templates[sect]['roll'])
        # print('dice roll for table: {}'.format(roll))
        item_list.remove('roll')
        selected_from_table = list()
        not_dice_table = list()
        # search all section items for options
        for key in item_list:
            # print(key)
            option = self.pattern_dice_table_option.match(key)
            # when you find them select and return those options.
            if option:
                # if this matches the option is of the type #-#
                if option.group(2):
                    # print("found range {} {}".format(option.group(1),
                    #                                  option.group(3)))
                    if roll in range(int(option.group(1)),
                                     int(option.group(3)) + 1):
                        selected_from_table.append(key)
                elif roll == int(option.group(1)):
                    # print("found single number {}".format(option.group(1)))
                    selected_from_table.append(key)
            else:
                not_dice_table.append(key)
        return selected_from_table + not_dice_table
