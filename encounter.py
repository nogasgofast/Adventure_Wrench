#!/usr/bin/python

import json

class Encounter():
    def __init__(self):
        self.data = {
            'abilities' : [],
            'ac' : 10,
            'atk_weapon': [],
            'atkBonus' : 0,
            'attacks' : [],
            'bs' : 0,
            'cond_immunity' : [],
            'DSF' : 0,
            'DSS' : 0,
            'dam_resistance' : [],
            'dam_vulnerable' : [],
            'dam_immunity' : [],
            'damPerRound' : 0,
            'dr' : 0,
            'exp' : 0,
            'groupOf' : 1,
            'groupHP' : [],
            'maxHP' : 1,
            'hp' : 1,
            'initiative' : 1,
            'locomotion' : [],
            'loot' : [],
            'misc_actions':[],
            'motivation' : [],
            'name' : '',
            'profBonus': 0,
            'saveDC' : 0,
            'senses' : [],
            'size' : [],
            'speed': 30,
            'STR':8,
            'DEX':8,
            'CON':8,
            'WIS':8,
            'INT':8,
            'CHA':8,
            'type' : 'creature',
            'ws':0}

    def copy(self):
        'copy is a value copy instead of a reference copy'
        XEncounter = Encounter()
        XEncounter.data = self.data.copy()
        return XEncounter

    def import_cr_dissabled(self,TargetCR):
        'import from a template main stats for this TargetCR'
        template = challengRating()
        stats = template.get(TargetCR)
        for stat in template.breakDown:
            self.data[stat] = stats[stat]

    def import_options_dissabled(self,options):
        'imports from lists of optional changes to this encounter'
        enc_type = self.data['type']
        attributes = preset_data().get_options(enc_type,'attribute')
        attacks = preset_data().get_options(enc_type,'weapon')
        misc  = preset_data().get_options(enc_type,'misc')
        for opt in options:
            for attribute in attributes:
                if opt in attribute[0]:
                    self.data['abilities'].append(attribute[0])
            pos_atk = opt[0:-8]
            for weapon in attacks:
                if pos_atk in weapon[2:]:
                    self.import_attacks(weapon)
            pos_misc = opt[0:-5]
            for action in misc:
                if pos_misc in action[2:]:
                    self.import_misc_actions(action)

    def print_self(self):
        print( json.dumps(self.data,sort_keys=True, indent=4, separators=(',', ': ')))

    def set_option(self,option,val):
        self.data[option] = val

    def get_option(self,option):
        return self.data[option]

    def import_attacks_dissabled(self,opt):
        if not opt in self.data['atk_weapon']:
            self.data['atk_weapon'].append(opt)

    def import_misc_actions_dissabled(self,misc):
        if not misc in self.data['misc_actions']:
            self.data['misc_actions'].append(misc)

    def import_stats_dissabled(self,STR,DEX,CON,WIS,INT,CHA):
        self.data['stats'] = {'STR':STR,
                          'DEX':DEX,
                          'CON':CON,
                          'WIS':WIS,
                          'INT':INT,
                          'CHA':CHA}

    def gen_actions(self):
        actions = []
        # attack bonus from cr
        size = 1
        if self.data['size'] == 'tiny':
            size = 0.25
        if self.data['size'] == 'small':
            size = 0.50
        if self.data['size'] == 'large':
            size = 2
        if self.data['size'] == 'gargantuan':
            size = 4
        attack = self.data['atkBonus']
        attacksPerRound = 1
        damage = self.data['damPerRound'] / self.data['groupOf']
        damage = damage / attacksPerRound
        damage = int(damage * size)
        damage = self.to_dice(damage)
        features = []
        # a list of weapons I can attack with
        for weapon in self.data['atk_weapon']:
            features = weapon[2:]
            damage_die = weapon[2]
            #TODO if damage_die == -1 : then don't have damage?
            actions.append('%s Attack: +%s damage: %s (%s)' % (weapon[0],
                                    attack,
                                    damage,
                                    ', '.join(features)
                                    ))
            features = []

        for spell_group in self.data['misc_actions']:
            for spell in spell_group:
                #remove ; from data before parsing.
                print(spell)
                spell_data = [s.replace(';','') for s in spell]
                name = spell_data.pop(0)
                spell_data.pop(0)
                target = spell_data.pop(0)
                damage_die = spell_data.pop(0)
                damage_type = spell_data.pop(0)
                success_type = spell_data.pop(0)
                actions.append('%s:\n'
                               '\tTarget: %s \n' \
                               '\tDamage: %s %s \n' \
                               '\t%s \n' \
                               '\t%s' % (name, target,
                                         damage_die, damage_type,
                                         success_type,
                                         ', \n\t'.join(spell_data)))
                features = []
        self.data['actions'] = actions
        #self.print_self()

    def sqrt(self,num):
        if (num / 2) > 1:
            return num / 2
        else:
            return 0

    def to_dice(self,Max=False):
        '%50 instability use largest die value possible.'
        # if this function is called with no arguments
        # we are asking for this items to_dice() string.
        if not Max:
            Max = self.get_option('maxHP')
        elif Max < 2:
            return Max
        Half = (Max // 2)
        myHalf = (Max // 2)
        dice = (100,20,12,10,8,6,4)
        rolls = []
        for die in dice:
            die_val = (die // 2) + 1
            numDice = myHalf // die_val
            if numDice >= 1:
                myHalf = myHalf - (die_val * numDice)
                rolls.append('%sd%s'%(numDice,die))
        rolls.append('%s'%(myHalf+Half))
        return '+'.join(rolls)


    def to_string(self):
        options = []
        loadData = [
            'damPerRound',
            'dr',
            'exp',
            'saveDC',
            'loot',
            'motivation',
            'senses']
        for catagory in loadData:
            # print self.data[catagory]
            if self.data[catagory]:
                options.append('%s: %s' % (
                    catagory,
                    self.data[catagory]))
        for ability in self.data['abilities']:
            options.append(ability)
        #print self.data['actions']
        if self.get_option('type') == 'creature':
            return (
                'Name: %s\n'
                'size: %s\n' \
                '====================\n' \
                'Armor Class: %s\n' \
                'MaxHP: %s(%s)\n' \
                'speed: %s %s\n' \
                '====================\n' \
                'STR       DEX       CON       WIS       INT       CHA\n' \
                '%s(%s)    %s(%s)    %s(%s)    %s(%s)    %s(%s)    %s(%s)\n' \
                '====================\n' \
                '%s\n' \
                '====================\n' \
                'Actions\n'
                '--------------------\n' \
                '%s\n' \
                '' % (
                self.data['name'],
                self.data['size'],
                self.data['ac'],
                self.data['maxHP'],
                self.to_dice(self.data['maxHP']),
                self.data['speed'],
                ', '.join(self.data['locomotion']),
                self.data['STR'],
                ((self.data['STR'] - 10) / 2),
                self.data['DEX'],
                ((self.data['DEX'] - 10) / 2),
                self.data['CON'],
                ((self.data['CON'] - 10) / 2),
                self.data['WIS'],
                ((self.data['WIS'] - 10) / 2),
                self.data['INT'],
                ((self.data['INT'] - 10) / 2),
                self.data['CHA'],
                ((self.data['CHA'] - 10) / 2),
                ' \n'.join(options),
                ' \n'.join(self.data['actions'])))
        elif self.get_option('type') == 'trap':
            return (
                'Name: %s (%s)\n'
                'size: %s\n' \
                '====================\n' \
                'Armor Class: %s\n' \
                'speed: %s %s\n' \
                '====================\n' \
                '%s\n' \
                '====================\n' \
                'Actions\n'
                '--------------------\n' \
                '%s\n' \
                '' % (
                self.data['name'],
                self.data['type'],
                self.data['size'],
                self.data['ac'],
                self.data['speed'],
                ', '.join(self.data['locomotion']),
                ' \n'.join(options),
                ' \n'.join(self.data['actions'])))
        elif self.get_option('type') == 'social':
            return (
                'Name: %s\n'
                'size: %s\n' \
                '====================\n' \
                'Armor Class: %s\n' \
                'MaxHP: %s(%s)\n' \
                'speed: %s %s\n' \
                '====================\n' \
                'STR       DEX       CON       WIS       INT       CHA\n' \
                '%s(%s)    %s(%s)    %s(%s)    %s(%s)    %s(%s)    %s(%s)\n' \
                '====================\n' \
                '%s\n' \
                '====================\n' \
                'Actions\n'
                '--------------------\n' \
                '%s\n' \
                '' % (
                self.data['name'],
                self.data['size'],
                self.data['ac'],
                self.data['maxHP'],
                self.to_dice(self.data['maxHP']),
                self.data['speed'],
                ', '.join(self.data['locomotion']),
                self.data['STR'],
                ((self.data['STR'] - 10) / 2),
                self.data['DEX'],
                ((self.data['DEX'] - 10) / 2),
                self.data['CON'],
                ((self.data['CON'] - 10) / 2),
                self.data['WIS'],
                ((self.data['WIS'] - 10) / 2),
                self.data['INT'],
                ((self.data['INT'] - 10) / 2),
                self.data['CHA'],
                ((self.data['CHA'] - 10) / 2),
                ' \n'.join(options),
                ' \n'.join(self.data['actions'])))
        else:
            return 'to_string() does not know what type this is.'


#class option_list():
class preset_data():
    def __init__(self):
        config_files = ['creature','trap','social']
        self.data = {}
        for config in config_files:
            self.data[config] = json.loads(open('config/%s.json'%config).read())
        self.cr = [
            (2,10,6,3,1,13,10),
            (2,13,85,3,14,13,200),
            (2,13,100,3,20,13,450),
            (2,13,115,4,26,13,700),
            (2,14,130,5,32,14,1100),
            (3,15,145,6,38,15,1800),
            (3,15,160,6,44,15,2300),
            (3,15,175,6,50,15,2900),
            (3,16,190,7,56,16,3900),
            (4,16,205,7,62,16,5000),
            (4,17,220,7,68,16,5900),
            (4,17,235,8,74,17,7200),
            (4,17,250,8,80,17,8400),
            (5,18,265,8,86,18,10000),
            (5,18,280,8,92,18,11500),
            (5,18,295,8,98,18,13000),
            (5,18,310,9,104,18,15000),
            (6,19,325,10,110,19,18000),
            (6,19,340,10,116,19,20000),
            (6,19,355,10,122,19,22000),
            (6,19,400,10,140,19,25000),
            (7,19,445,11,158,20,33000),
            (7,19,490,11,176,20,41000),
            (7,19,535,11,194,20,50000),
            (7,19,580,12,212,21,62000),
            (8,19,625,12,230,21,75000),
            (8,19,670,12,248,21,90000),
            (8,19,715,13,266,22,105000),
            (8,19,760,13,284,22,120000),
            (9,19,805,13,302,22,135000),
            (9,19,850,14,320,23,155000)]
        self.breakDown = (
                        'profBonus',
                        'ac',
                        'maxHP',
                        'atkBonus',
                        'damPerRound',
                        'saveDC',
                        'exp')

    def get(self,cr):
        stats = {}
        temp = self.cr[cr]
        i = 0
        for stat in self.breakDown:
            stats[stat] = temp[i]
            i += 1
        return stats

    def get_options(self,enc_type,option):
        ans = []
        for row in self.data[str(enc_type)]:
            if row[1] == option:
                ans.append(row)
        return ans
