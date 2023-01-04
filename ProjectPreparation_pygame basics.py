
# Project Preparation (pygame basics)

# Installing pygame :pip install pygame
# Creating a pygame window

"""Right at the top we import pygame and then we call the init function located in the pygame package.
This function does a lot of setup work for us, but we don't need to worry too much about what is going on behind
the scenes here.

On the next line we tell pygame how big we want our application window to be. We do this using the set_mode
function located in the display module.

Like our own programs, pygame is split up into several different files, and different parts of the library
are located in these different files. Things to do with the main display window can be found in the display
module. We'll be using it quite a lot.

The set_mode function is what actually creates the display window, and we can call it without any arguments if
we want to. If we pass in no arguments, we get a window that fills our entire screen. If we want to limit the
window to some specific size, we can instead pass in a two element sequence, like a list a list or a tuple.
The values inside must be integers, where the first represents the width of the window in pixels, and the
second represents the height of the window in pixels.

The rest of the application is concerned with keeping the window around, and ensuring that the user can close
the program using the window controls"""

import pygame
from collections import namedtuple

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
CIRCLE_COLOUR = Colour(red=255, green=253, blue=65)
RECTANGLE_COLOUR = Colour(red=255, green=255, blue=255)

pygame.init()

# If we want to set a custom title for the window, we can do that using the display.set_caption function
pygame.display.set_caption(("My Game!"))

screen = pygame.display.set_mode([640, 480])
screen.fill(BACKGROUND_COLOUR)

pygame.draw.rect(screen, RECTANGLE_COLOUR, [0, 0, 100, 50])
pygame.draw.circle(screen, CIRCLE_COLOUR, [320, 240], 40)

pygame.display.update()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

main()

print(screen.get_width())
print(screen.get_height())

"""The draw module
The draw module contains several functions for drawing simple shapes onto a surface.

Let's start by drawing a rectangle using the rect function. rect takes a few different arguments.

First, it takes a surface to draw on, which can be any Surface object.

The second argument is color, which expects a colour in the same format as we discussed for fill.

The final required parameter is rect, which expects either a Rect object, or a sequence of values 
containing the information that a Rect object would usually hold.

Rect objects are really just containers for four important values: the x and y position of the 
rectangle's top left corner, expressed as coordinates; the width of the rectangle; and the height 
of the rectangle. This means we can replace them with a four element list or tuple that contains 
the same information.

With that in mind, let's try to draw a white circle on the screen surface, positioned in the top 
left corner.


Drawing text
Drawing text onto a surface is a little more complicated. We first have to create a Font object 
from the pygame.font module like so:

font = pygame.font.Font(None, 28)

The first argument here a file name , but we can just write None here. The second argument is a
 font size.

Once we have a Font object, we can call the render method to give us something we can actually 
draw onto a surface.

The render method takes a string, which will form the text content, a Boolean, and a colour. 
The Boolean represents whether or not you want to use anti-aliasing.

font = pygame.font.Font(None, 28)
text = font.render("Woo! This is some text!", True, (0, 0, 0))

Finally, we can draw the text onto a surface by calling the blit method on the surface we want 
to draw onto.

font = pygame.font.Font(None, 28)
text = font.render("Woo! This is some text!", True, (0, 0, 0))
screen.blit(text, (50, 50))

blit really just means draw, but it's a funny word you're going to have to get used to.

The blit method takes in the thing you want to blit, and then a position."""

# We're also going to need one more thing, which is a Clock object
# he Clock is going to let us limit how often the window gets painted, by setting a maximum frame rate.
# We do this by providing a frames per second value to the tick method from inside our loop.

import pygame
from collections import namedtuple

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
CIRCLE_COLOUR = Colour(red=255, green=253, blue=65)

pygame.init()

pygame.display.set_caption("My game!")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

def main():
    circle_position = [320, 240]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, CIRCLE_COLOUR, circle_position, 40)
        pygame.display.update()

        circle_position[0] += 5

        clock.tick(60)

main()


"""Events
Events are how pygame communicates that something has happened in the application. This 
might be something like the user moving their mouse, or pressing a key, or clicking the 
little cross to close the application.

Since the very first example, we've had some code in our main function which is checking 
for a pygame.QUIT event.

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return

Here we're checking through some set of events that pygame has logged, and we're looking 
to see if any of those events are pygame.QUIT events. This event is what gets triggered 
when a user presses the button to close the application.

Clicking this button doesn't actually close the window: we have to do something to cause 
that to happen. In our case, we return from the main function, which leaves Python with 
no more code to run. This causes the application to terminate.

pygame has a lot of different events types, and we can check for those events in the same 
way that we're checking for pygame.QUIT. For example, we can check for mouse movement 
using pygame.MOUSEMOTION
"""

"""Let's create a new application where we just print out the position of the mouse to the console. 
We can find the position of the mouse from a pygame.MOUSEMOTION event by accessing an attribute 
on the event called __dict__.

This gives us a dictionary with a key called "pos" which contains coordinates for the mouse 
position when that event was triggered"""

import pygame

pygame.init()

pygame.display.set_caption("Mousetracker")
screen = pygame.display.set_mode([640,480])

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                position = event.__dict__["pos"]
                print(position)

main()


# Let's upgrade this little app so that a ball follows the cursor around the screen

import pygame
from collections import namedtuple

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
CIRCLE_COLOUR = Colour(red=255, green=253, blue=65)

pygame.init()

pygame.display.set_caption("Mousetracker")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640,480])

def main():
    circle_position = (screen.get_width() // 2), (screen.get_height() // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                circle_position = event.__dict__["pos"]

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, CIRCLE_COLOUR, circle_position, 20)
        pygame.display.update()

        clock.tick(60)

main()


"""A bouncing ball
Let's look at one more example.

I want to return to the ball which moves on its own, but now I'd like it to bounce off 
the sides, rather than flying out of view.

In order to do this, we're going to keep track of the ball's velocity, which is going to 
describe how far the ball will move in a given direction for each tick of our clock. 
To keep things interesting, we can randomise the starting values for this velocity"""

import pygame
from collections import namedtuple
from random import randint

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
BALL_COLOUR = Colour(red=255, green=253, blue=65)

BALL_RADIUS = 20

pygame.init()

pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

def main():
    ball_position = [(screen.get_width() // 2), (screen.get_height() // 2)]
    ball_velocity = [randint(-5, 5), randint(-5, 5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, BALL_COLOUR, ball_position, BALL_RADIUS)
        pygame.display.update()

        clock.tick(60)

main()


# The next step is checking that the ball hasn't exceeded any of the "walls" of our window.
# If it has, we need to redirect the ball, preventing it from continuing on its current trajectory.
# In order to do this, we're going to modify the ball's velocity.

import pygame
from collections import namedtuple
from random import randint

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
BALL_COLOUR = Colour(red=255, green=253, blue=65)

BALL_RADIUS = 20

pygame.init()

pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

def main():
    ball_position = [(screen.get_width() // 2), (screen.get_height() // 2)]
    ball_velocity = [randint(-5, 5), randint(-5, 5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, BALL_COLOUR, ball_position, BALL_RADIUS)
        pygame.display.update()

        # Check for left and right collisions
        if ball_position[0] - BALL_RADIUS < 0:
            ball_velocity[0] = -ball_velocity[0]
        elif ball_position[0] + BALL_RADIUS > screen.get_width():
            ball_velocity[0] = -ball_velocity[0]

        # Check for top and bottom collisions
        if ball_position[1] - BALL_RADIUS < 0:
            ball_velocity[1] = -ball_velocity[1]
        elif ball_position[1] + BALL_RADIUS > screen.get_height():
            ball_velocity[1] = -ball_velocity[1]

        clock.tick(60)

main()

# Finally, we just need to move the ball for each tick, adding the current velocity to the ball's position.
import pygame
from collections import namedtuple
from random import randint

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=168)
BALL_COLOUR = Colour(red=255, green=253, blue=65)

BALL_RADIUS = 20

pygame.init()

pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])

def main():
    ball_position = [(screen.get_width() // 2), (screen.get_height() // 2)]
    ball_velocity = [randint(-5, 5), randint(-5, 5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, BALL_COLOUR, ball_position, BALL_RADIUS)
        pygame.display.update()

        # Check for left and right collisions
        if ball_position[0] - BALL_RADIUS < 0:
            ball_velocity[0] = -ball_velocity[0]
        elif ball_position[0] + BALL_RADIUS > screen.get_width():
            ball_velocity[0] = -ball_velocity[0]

        # Check for top and bottom collisions
        if ball_position[1] - BALL_RADIUS < 0:
            ball_velocity[1] = -ball_velocity[1]
        elif ball_position[1] + BALL_RADIUS > screen.get_height():
            ball_velocity[1] = -ball_velocity[1]

        ball_position[0] += ball_velocity[0]
        ball_position[1] += ball_velocity[1]

        clock.tick(60)

main()

