
# Project Dice Roller

"""The brief

Now that we've learnt a little bit about argparse we can get to the meat of the project. For this project we're going
to be creating a dice roller for n-sided dice.

The user is going to be able to specify a selection of dice using the following syntax, where the number before the
d represents the number of dice, and the number after the d represents how many sides those dice have.

python main.py 3d6

In this case, the user has requested three six-sided dice.

Using the random module, we're going to simulate the dice rolls the user requested, and we're going to output some
results in the console, like this:

Rolls: 1, 2, 4
Total: 7
Average: 2.33

Here we have the numbers rolled, the sum of the values, and the average of the rolls.

In addition to printing this result to the console, we're also going to keep a permanent log of the rolls in a file
called roll_log.txt. The user can specify a different log file if they wish with an option argument called --log.

python main.py 2d10 --log rolls.txt

In addition to specifying a custom log file, the user can specify a number of times to roll the dice set using
a --repeat flag.

python main.py 6d4 --repeat 2

Both --repeat and --log should have appropriate documentation, and the user should be able to use -r and -l as short
versions of the flags. The user can also use both the --repeat and --log flags if they want to."""