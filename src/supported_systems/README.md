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

Can use macros in templates as long as you put a ^ before the name. For instance ^con-mod is the constitution modifier in D&D 5e. And represents the stat constitution plust 10 divided by 2 rounded down. An example of this is below.

```
[macros]
str-mod=(%str-10)//2
dex-mod=(%dex-10)//2
con-mod=(%con-10)//2
int-mod=(%int-10)//2
wis-mod=(%wis-10)//2
cha-mod=(%cha-10)//2
```



### Header

The header section has one valid key. "template" which supports both stats and macros.

[header]
template=%name
 CR: ^cr
 AC: ^ac
 HP: ^hp
 STR: %str ^str-mod DEX: %dex ^dex-mod CON: %con ^con-mod 
 INT: %int ^int-mod WIS: %wis ^wis-mod CHA: %cha ^cha-mod


### Section Headings

For now these are very simple headings to each section. Not much to see here other then I am using "\n" which will later 
be read as a new-line character and add one line of spacing before and after the sections.

[sections]
template="\n====[ %section ]====\n"


### Footer

The last thing to be printed on a stat sheet. 

[footer]
template=\n
