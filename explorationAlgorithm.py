import random
import traversable
import copy


class Direction:
    def __init__(self, deltaX, deltaY, name):
        self.x = deltaX
        self.y = deltaY
        self.name = name


LEFT = Direction(-1, 0, "LEFT")
RIGHT = Direction(1, 0, 'RIGHT')
UP = Direction(0, -1, "UP")
DOWN = Direction(0, 1, 'DOWN')

directionsDict = {1: LEFT, 2: RIGHT, 3: UP, 4: DOWN}
directionsList = [LEFT, RIGHT, UP, DOWN]


class Coordinates:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    # find out if a point is within the dimensions of the labyrinth
    def isWithinRange(self, direction):
        if self.x + direction.x >= self.height or self.x + direction.x < 0 or self.y + direction.y >= self.width or self.y + direction.y < 0:
            return False
        else:
            return True


def exploreRandom(knownLabyrinth, coordinates):
    # random direction
    validDirectionFound = False
    while not validDirectionFound:
        r = random.randint(1, 4)
        # print(r)
        direction = directionsDict[r]

        # if the direction picked is legit
        if (coordinates.isWithinRange(direction) and
                # the tile we want to go to isn't a wall
                knownLabyrinth[coordinates.x + direction.x][coordinates.y + direction.y] != "#"):
            # move 1 in the picked direction
            coordinates.x += direction.x
            coordinates.y += direction.y

            return direction.name


class Edge:
    def __init__(self, originNode, destinationNode):
        self.originNode = originNode
        self.destinationNode = destinationNode


class Node:
    def __init__(self, coordinates):
        self.Coordinates = coordinates
        self.ingoingEdges = []
        self.outgoingEdges = []

    def connectNeighbors(self, knownLabyrinth, nodes):
        # find adjacent nodes that are also traversable
        for direction in directionsList:
            # if the direction is out of bounds, skip it
            if not self.Coordinates.isWithinRange(direction):
                continue

            coordinatesClone = copy.deepcopy(self.Coordinates)
            # move the point in the desired direction
            coordinatesClone.x += direction.x
            coordinatesClone.y += direction.y

            if knownLabyrinth[coordinatesClone.y][coordinatesClone.x] in traversable.traversable:
                destinationNode = nodes[coordinatesClone.y][coordinatesClone.x]

                # add the outgoing edge to the list
                edge = Edge(self, destinationNode)

                self.outgoingEdges += [edge]
                destinationNode.ingoingEdges += [edge]


def constructGraph(knownLabyrinth, HEIGHT, WIDTH):
    nodes = []
    for row in range(HEIGHT):
        r = []
        for column in range(WIDTH):
            r += [None]
        nodes += [r]

    # First start by filling the nodes that exist
    for row in range(HEIGHT):
        for column in range(WIDTH):
            # if the point is traversable, create a node that corresponds to it
            if knownLabyrinth[row][column] in traversable.traversable:
                nodes[row][column] = Node(Coordinates(column, row, HEIGHT, WIDTH))

    nodeArray = []
    # Then connectNeighbors for each existing node
    for row in range(HEIGHT):
        for column in range(WIDTH):
            if nodes[row][column]:
                nodes[row][column].connectNeighbors(knownLabyrinth, nodes)
                nodeArray += [nodes[row][column]]
    return nodeArray


def exploreBreadthFirst(knownLabyrinth, coordinates, HEIGHT, WIDTH):
    # make a graph of all the points in the labyrinth using constructGraph()


    # make a graph of the points in the labyrinth within 2 range of a ? mark

    # how to create nodes in a graph without repeating a location?

    pass
