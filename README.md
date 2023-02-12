# Adventure Wrench
5E compatible
1. Initiative Tracker
2. A super useful Template builder
3. Template Randomizer, with automatic value adjustments.
4. A content vault that stores past creations.

Lets us build fast, reduces writing, and enhances what you get
out of what you create.

## Ethos:
- never ask anyone to save.
- Be easy to write and read
- Reuse and recycle as much as possible.

## Automaticly Adjusted Values
These special words will be replaced at the time your building something in "The Shop".
And generally allow you to write more flexible items and actions which adjust to
the difficulty your going for.

| Stand-in Values | What they are |
| %h| This is directly related to cr, but you likely will never use this |
| %h9| same as %h but divides by 9. Works with numbers 2-9 Great for making healing or poison effects. |
| %a| attack bonus calculated from strength mod plus profeciency bonus for cr |
| %d| damage calculated from "Challenge rating" divided by "Group of". You will need
to adjust this number down for things included in a multi-attack. %d is just a guess at damage
per round this entity should be doing for the challenge rating your looking for. |
| %e| elemental damage calculated as 1/4th of damager per round. (in addition to challenge rating) |
| %e9| same as %e only divides damage by number specified. can use numbers 2-9 |
| %s| Spell save DC for spell actions directly from cr|


## Examples
0.
| cr | "challenge rating" | "group of" |
|1/2| 1 | 2|
|1/4| 1 | 4|
|1/8| 1 | 8|
|1/16| 1 |16|
I guess the point here is double the "group of" field is aproximatly like lowering
the challenge rating by 1 level until you get to cr 1. Then it's more or less filling out
the space between CR 1 and CR 0. Remember if the HP seems high for a cr 1 thing,
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
the roll table is applied to something if A.W. rolls a 3 that thing will now have
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



## TODO:
@TheShop getting roll tables to work right.
@TheShop put in limiters for roll tables and templates so they can't be selected
twice. Preventing endless recussion problems.
@main add click-able window for items that came from the vault.
