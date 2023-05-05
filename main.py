import Labyrinth
from explorationAlgorithm import Coordinates as Coordinates
import explorationAlgorithm

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    labyrinthTestcase = Labyrinth.LabyrinthTestcase([],  # labyrinth
                                                    20,  # Height
                                                    20,  # Width
                                                    2,  # sight range
                                                    Coordinates(0, 0, 20, 20),  # Player Coordinates
                                                    Coordinates(19, 19, 20, 20)  # Goal Coordinates
                                                    )
    labyrinthTestcase.explore()
    knownLabyrinth = labyrinthTestcase.knownLabyrinth
    nodeArray = explorationAlgorithm.constructGraph(knownLabyrinth, labyrinthTestcase.HEIGHT, labyrinthTestcase.WIDTH)

