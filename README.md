

# Adventure Wrench
A no internet necessary, 5e compatible, intiative tracker and encounter builder. It focuses on fast reactions to current events. And allows Encounters to be built quickly from modular pieces. Or to help my ADHD friends keep consistant when making stat blocks.

## Game Tracker
The Main window for this program is the game tracker. It keeps tabs on important information, notes and marks about the current encounter. It's clean and easy to see what is going on at a glance.
Full stat blocks are hidden by default but can be seen on mouse roll-over. You can pull them up in seperate window by double-clicking them.


## The Vault
The vault is a repository of all unique things that can be copied into the current game when needed. Think varients of a monster, trap, npc, or boss. Or even pre-generated lists of information like lore, background, or geography.


# Under Construction for v2

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

### Tips
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
