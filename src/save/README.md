# Pen And Paper System Construction

## Overview

Vualt Templates are a way to re-skin what appears by default for new items, monsters, traps, and NPC's. They also allow us to specify macros in the same place. These allow us to have special calculated values to use while building items, monsters, traps,and NPC's. This should give us some flexibility in defining different PNP rpg systems using the same application. But of coarse once in the encounter tracker anything from the vault will need an initiative and hp at a minimum.


### Format 

First lets talk about the format of the config file. It's in "ini" or config file format. This means there will be sections surrounded by [brackets] and simple key=value pairs one per line under a section. There wwill be only 4 valid sections. header, footer, stats, macros. 


### stats

Stats are basic values that are nessary for vault items. They are dynamicly loaded into the templating system and show up as values that can be modified by templates. Each key defined here is usable by calling it with a prepended % sign. For instance %str would be relpaced in templates with the value 10 if we defined it below like so:

```
[stats]
str=10
dex=10
con=10
int=10
wis=10
cha=10
```

### macros

A marco is a convienince tool to allow the templates to do basic math instead of writing it out multiple times in varous templates. Like before this is just a bunch of key=value pairs where the name is on the left and the math is on the right. In a macro you can use a stats as defined in your stats section of this document. 

Can use macros in templates as long as you put a % before the name. For instance %conmod is the constitution modifier in D&D 5e. And represents the stat constitution plust 10 divided by 2 rounded down. An example of this is below.

```
[macros]
strmod=(%str-10)//2
dexmod=(%dex-10)//2
conmod=(%con-10)//2
intmod=(%int-10)//2
wismod=(%wis-10)//2
chamod=(%cha-10)//2
```

### 5e.jinja

This file has a jinja template that broadly describes how the stat block should look. I use a compact(ish) template format because I have small laptop
screens but you do you. Any macros or stats defind in the 5e.ini file can be used in this template they should show up under the sc object. There should be some examples of that. As well as a few additional parameters being passed in through the data object. Feel free to experiment and try new things. Or 
make stat blocks that work for the ttrpg you prefer. 
