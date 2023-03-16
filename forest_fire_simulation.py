# import packages
import pygame
import random

# set up Pygame window with dimensions 500 x 500
pygame.init()

WINDOW_SIZE = (500, 500)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Forest Fire Simulation")
screen.fill((255, 255, 255))

# update the entire screen
pygame.display.flip()


# create a grid, which represents the forest
# each cell represents a plot of land in which exactly one tree can be planted
# hence, a cell can contain either no tree, a tree, or a burning tree
GRID_SIZE = (50, 50)
CELL_SIZE = (10, 10)

# create a forest with GRID_SIZE[0] x GRID_SIZE[1] cells
# initialize each cell to value 0 (no tree)
forest = [[0 for y in range(GRID_SIZE[1])] for x in range(GRID_SIZE[0])]
tree = 0.5 # the probability that a plot of land will contain a tree (each cell can contain at most 1 tree)

# position of the first tree to catch on fire
fire_x = random.randint(0, GRID_SIZE[0])
fire_y = random.randint(0, GRID_SIZE[1])

# draw forest
for x in range(GRID_SIZE[0]):
	for y in range(GRID_SIZE[1]):
		if x == fire_x and y == fire_y:
			# first tree to catch on fire
			forest[x][y] = 2
			pygame.draw.rect(screen, (255, 0, 0), (x*CELL_SIZE[0], y*CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))
		elif random.random() < tree:
			forest[x][y] = 1
			# update color of cell to green
			pygame.draw.rect(screen, (0, 255, 0), (x*CELL_SIZE[0], y*CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))
		else:
			# the value of forest[x][y] should already be set to 0
			# so all we need to do is change the color of the cell to white to represent bare land
			pygame.draw.rect(screen, (255, 255, 255), (x*CELL_SIZE[0], y*CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))

# update display
pygame.display.flip()

# now, we're going to set our forest on fire
paused = False

while not paused:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# exit simulation
			paused = True
		elif event.type == pygame.KEYDOWN:
			# user has pressed a key
			if event.key == pygame.K_SPACE:
				# user has pressed space bar
				paused = True

	if not paused:
		# user hasn't paused the simulation
		# update the forest
		for x in range(GRID_SIZE[0]):
			for y in range(GRID_SIZE[1]):
				if forest[x][y] == 1:
					# see if neighboring tree is burning
					# if neighbor tree is on fire, the current tree catches on fire
					for dx in range(-1, 2):
						for dy in range(-1, 2):
							if dx == 0 and dy == 0:
								# current tree
								continue
							# get position of neighbor tree
							nx = x + dx
							ny = y + dy 
							# ensure that position of neighbor tree is valid
							if nx < 0 or ny < 0 or nx >= GRID_SIZE[0] or ny >= GRID_SIZE[1]:
								# invalid tree position
								continue
							# see if neighbor tree is burning
							if forest[nx][ny] == 2:
								# if neighbor tree is burning, the tree catches on fire
								forest[x][y] = 2
								pygame.draw.rect(screen, (255, 0, 0), (x*CELL_SIZE[0], y*CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))
								pygame.display.flip()
								pygame.time.delay(5)
				elif forest[x][y] == 2:
					# burning tree
					forest[x][y] = 0 # tree is burnt and all that is left are ashes
					pygame.draw.rect(screen, (0, 0, 0), (x*CELL_SIZE[0], y*CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1]))
					pygame.display.flip()
					pygame.time.delay(5)

# exit simulation
pygame.quit()
