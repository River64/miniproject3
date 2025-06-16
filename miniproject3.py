class person:
    def __init__(self, opinion):
        self.opinion = opinion
        # add other attributes a person can have?
        # these would probably be constants
    
    # Setter method for a person's belief
    def set_belief(self, opinion):
        self.opinion = opinion
    
    def generate_random_person():
        # returns a new person with randomly chosen attributes

class cell:
    # A constant: the maximum number of people a cell can hold
    max_occupancy = 20
    def __init__(self, people)
        # a cell has a number of people in it
        # generate [people] number of random people in the cell
        # put them all in an array
        # it may have other properties

class simulation:
    def __init__():
        # initialize fields (state variables)
        # cells, people in those cells

    def observe():
        # returns data representing the current state of the simulation
        # displays this data in an animation maybe?

    def update():
        # loop to update each person's state (opinion)
        # the people also move around between cells

    def run():
        # loops calling update() and observe()
        # collects and returns results

# create a new simulation
# call init function
# call run function
# print/display output of run function