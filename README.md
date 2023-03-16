# Forest Fire Simulation

## Table of Contents
* Overview
* Software/Package Requirements
* Next Steps

## Overview
This program is a simple cellular automaton model of a forest fire. It first creates a grid, which represents the forest, containing square cells. Each cell represents a plot of land, in which one tree can be planted at most. A cell containing a healthy tree is represented with a green cell, a cell containing no trees is represented with a white cell, a cell containing a burning tree is represented with a red cell, and a cell containing a burnt tree is represented with a black cell. In other words, a cell can be in one of four states: no tree, healthy tree, burning tree, or burnt tree.

How populated the forest is can be altered by changing the *tree* variable. *tree* is a decimal value between 0 and 1 that represents the probability that a plot of land will contain a tree. A more populated forest will have a *tree* value close to 1; a less populated forest, on the other hand, has a *tree* value of close to 0. The starting point of the fire can be changed as well. Though set to a random position in the code, the user can change the *fire_x* and *fire_y* variables to start the fire at any cell in the grid. 

The rules of this simulation are as follows:
1. If two trees share an edge or a corner, they are neighbors. Hence, a tree can have a maximum of eight neighbor trees.
2. A tree catches on fire if and only if a neighbor tree is on fire.
3. A cell containing no trees at the beginning of the simulation remains in that state throughout the simulation.
4. A tree that is burning becomes burnt in the next round.
5. Once a tree is burnt, it cannot catch on fire again.

Pressing the spacebar ends the simulation.

## Software/Package Requirements
This code was written in Python. The forest is visualized using Pygame. Having Python and Pygame installed is sufficient to run the program.

## Next Steps
Some additional features that could be added to improve this simulation are...
### Firefighter
A firefighter feature could be added. This feature could slow down the spread of the forest fire in two ways:
1. Wet trees are harder to ignite that dry trees. Hence, the program could be altered such that a tree that has come into contact with a firefighter has < 1 chance of catching on fire (as opposed to the current code, where a tree is guaranteed to catch on fire if at least one of its neighbors is on fire)
2. A burning tree that comes into contact with a firefighter is extinguished, and therefore does not catch its neighbors on fire.

### Squirrel Escape
See if a squirrel would be able to successfully escape the burning forest under the following conditions:
1. The squirrel can only move horizontally and vertically in the grid.
2. The squirrel can only be on a cell if it contains no tree or if it contains a regular tree.
3. If a tree catches on fire whilst the squirrel is on it, the squirrel dies.
4. The squirrel has successfully escaped the forest if it reaches one of the four boundaries of the grid.
