import explorationAlgorithm


class LabyrinthTestcase:
    def __init__(self, labyrinth, HEIGHT, WIDTH, SIGHTRANGE, playerCoordinates, goalCoordinates):
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH

        self.SIGHTRANGE = SIGHTRANGE
        self.controlRoomFound = False

        self.playerCoordinates = playerCoordinates
        self.goalCoordinates = goalCoordinates

        self.labyrinth = []
        self.initializeLabyrinth()

        self.knownLabyrinth = []
        self.initializeKnownLabyrinth()

    def printLabyrinth(self):
        labyrinth2 = self.knownLabyrinth.copy()
        labyrinth2[self.playerCoordinates.y][self.playerCoordinates.x] = "X"
        for row in labyrinth2:
            print(*row)

    def initializeLabyrinth(self):
        for row in range(self.HEIGHT):
            r = []
            for column in range(self.WIDTH):
                r += ["."]
            self.labyrinth += [r]
        # also testcase dependent
        self.labyrinth[self.goalCoordinates.y][self.goalCoordinates.x] = "C"

    def initializeKnownLabyrinth(self):
        # initialize known labyrinth
        for row in range(self.HEIGHT):
            r = []
            for column in range(self.WIDTH):
                r += ["?"]
            self.knownLabyrinth += [r]
        # testcase dependent
        self.knownLabyrinth[self.playerCoordinates.y][self.playerCoordinates.x] = "T"

    def explore(self):
        movementcount = 0
        while not self.controlRoomFound:
            movementcount += 1
            # define the range of tiles to reveal
            minX = max(self.playerCoordinates.x - self.SIGHTRANGE, 0)
            maxX = min(self.playerCoordinates.x + self.SIGHTRANGE + 1, self.WIDTH)  # must add 1 because range(b, e) is exclusive at the end

            minY = max(self.playerCoordinates.y - self.SIGHTRANGE, 0)
            maxY = min(self.playerCoordinates.y + self.SIGHTRANGE + 1, self.HEIGHT) # must add 1 because range(b, e) is exclusive at the end

            # add the new tiles to the knownLabyrinth
            for row in range(minY, maxY):
                for column in range(minX, maxX):
                    self.knownLabyrinth[row][column] = self.labyrinth[row][column]
                    if self.labyrinth[row][column] == "C":
                        self.controlRoomFound = True

            # self.printLabyrinth()
            #
            # print("minX: ", minX)
            # print("maxX: ", maxX)
            # print("minY: ", minY)
            # print("maxY: ", maxY)
            #
            # print("_________________________________________")

            if not self.controlRoomFound:
                # time.sleep(0.2)
                movement = explorationAlgorithm.exploreRandom(self.knownLabyrinth, self.playerCoordinates)
                # print(movement)


        #self.printLabyrinth()  # otherwise we're missing a print
        print(movementcount)
