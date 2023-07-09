# Adventure Wrench
5E compatible
1. Initiative Tracker
2. A super useful Template builder
3. Template Randomizer, with automatic value adjustments.
4. A content vault that stores past creations.

Lets us build fast, reduces writing, and enhances what you get
out of what you create.


## Automaticly Adjusted Values
These special words will be replaced at the time you are building something in "The Shop".
And generally allow you to write more flexible items and actions which adjust to
the difficulty you are going for.


| Stand-in Values | What they are |
| --------------- | ------------- |
| %str            | Strength mod after templates are compiled |
| %dex            | Dexterity mod after templates are compiled |
| %con            | Constitution mod after templates are compiled |
| %wis            | Wisdom mod after templates are compiled |
| %int            | Intelligence mod after templates are compiled |
| %cha            | Charisma mod after templates are compiled |
| %h              | This is current health value directly related to challenge rating, but should not be used often.  |
| %h9             | Same as %h but divides it by 9. Works with numbers 2-9 Great for making healing or poison effects. |
| %a              | Attack bonus calculated from challenge rating directly   |
| %d              | Damage per round, calculated from "Challenge rating" divided by "Group of" on the shop page of the app. You will need to adjust this number down for things included in a multi-attack. I am still working on a way to enforce damage per round by  |
| %d9             | Same as %d only divides damage per round number specified. can use numbers 2-9 |
| %s              | Spell save DC for spell actions calculated directly from challange rating     |
| %{ }            | Takes any dice notation in the {} and caluculates it. ie: ${ 1d1 + 1} would be replaced with 2. supports simple dice notation 1d20 or 4d6. supports simple addition and subtraction 5 - 3. supports top function 2d20T1 or 4d6t3. support bottom function 6d10B2 6d10b2 |


## Examples
0. Fractional Challenge Ratings

| cr  | "challenge rating" | "group of" |
| --- | ------------------ | ---------- |
|1/2  | 1                  | 2          |
|1/4  | 1                  | 4          |
|1/8  | 1                  | 8          |
|1/16 | 1                  |16          |

I guess the point here is double the "group of" field is aproximatly like lowering
the challenge rating by 1 level until you get to cr 1. Then it's more or less filling out
the space between CR 1 and CR 0. Remember if the HP seems high for a cr of 1,
that's because it's built to be a challenging 4 on 1 fight. That goes for the damage
as well. The Challenge Rating data is sampled from the SRD but may not be exact.

1. damage, elemental damange, and health auto-values
Building a weapon with auto-values. You can create a "Action" for this:
Name: flame sprite mace
Cost: 1 Attack action
Limitations: range 5ft, 1 target
Result:
  Attack: +%a to hit
  on hit: %d bludgeoning damage, and %e fire damage. Small sparks and flames
  splash the target, ignighting flamable meterials.


2. Roll tables and selecting from lists randomly.
Roll tables are extreamly powerful in this application. Not only allowing for a
random selection, or a classic roll table from dnd. But also allowing roll tables
to select multiple items from one roll. By over-lapping the match values:

roll: 1d6
1: a stick
2-3: a pudding
3-5: a spoon
6: a golden ticket

Here we can see this is like a regular roll table except 3 is on here twice. When
the roll table is applied to something if Adventure Wrench rolls a 3 that thing will now have
a pudding and a spoon. A better outcome then even a golden ticket some might say.

Random roll? yes.
roll: 1d6
a stick
a pudding
a spoon
a golden ticket

In this case we are rolling 1d6 and picking randomly from the list that many times.

roll: 1d6
1: template: water bender
2: template: earth bender
3: template: air bender
4: template: fire bender
5: template: multi-dicepline bender
6: template: cabage vender

In this case we are not selecting items but other templates. In fact we can choose
to have roll tables which select other roll tables, templates that use other templates
and so on. When applied to something this roll table will apply another template so
long as that template or roll table has not been applied already.


## Making A Game to distribute
### I have the game all written up, what now?
1. close the application.
2. go into the "save" folder in the program directory and rename default.sqlite to anything else, keep the .sqlite end.
3. Share that renamed file to a friend, tell them to drop it into the "save" folder and use the "switch game" button.
4. Starting up the appication will start a new empty game named default.sqlite in the save folder.
5. If you want to switch back to the campaign you can use the "swtich game" button.

### I have a different game started already!
1. close the application
2. open the "save" folder and rename default.sqlite to anything else, keep the .sqlite end.
3. re-open the application and write your campaign.
4. Follow the instructions above for "I have the game all written up, what now?"
5. If you want to switch back to your old game at any time use the "switch game" button.

### 1337 hack3rs only
The awconfig.ini file should have the name of the currently used database file in it.
The change game button just edits this file and forces the user to restart the application.
that is all.

## Install instructions

If you are running 64bit windows or linux, likely all you need
is to look up the latest [Release]https://github.com/nogasgofast/Adventure_Wrench/releases)
for your platform.

Then you can simply unzip and move the folder to where you want the files to be kept, and
if you are so inclined you can make a shortcut at that time.

The application and all of it's dependencies will be in a self-contained folder the executable
file is "adventure_wrench".


## Python install instructions

If a binary does not work or does not work on your platform you can try building
the application for your system.

This application requires at least python 3.10, all versions before that are untested.

On a local command line interface:
git clone the project to a local folder.

optionally create a virtual enviornment and make sure it's activated.

cd src/
pip install -r requirements.txt

Then to run the application:
python main.py


## creating binary distrobutions

First you have to build the application as stated in python install instructions.
Then you can do the following:
pip install cx_Freeze
Make sure to read how cx_Freeze works and is used. Might be important info.

cd src/

Then do one of the following or make a new setup.py for your distrobution.

python linux-setup.py build
or
python windows-setup.py build

The distibution will be in a build/ folder.


## Questions
If you have any questions please pop them into the [Issues tracker on github](https://github.com/nogasgofast/Adventure_Wrench/issues)
