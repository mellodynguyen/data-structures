"""Functions to parse a file containing villager data."""

# line order in the file 
# name -> species -> personality -> hobby -> motto

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()


    filename = open("villagers.csv")
    for line in filename:
        line = line.rstrip() 
        words = line.split("|")
        
        species.add(words[1])

    return species

# print(all_species("villagers.csv"))
# printing to make sure it's printing the species 

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    filename = open("villagers.csv")
    for line in filename:
        name, species = line.rstrip().split("|")[:2]
        # villager name and species = words [0] and [1] which is why we stop at [2]

        if search_string in ("All", species):
            villagers.append(name)

    return sorted(villagers)

# print(get_villagers_by_species("villagers.csv", search_string="All"))
# print(get_villagers_by_species("villagers.csv", search_string="Wolf"))
# checking if it works for the respective species

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # 6 hobbies: Fitness, Nature, Education, Music, Fashion, and Play
    # return value should be a list with six lists inside
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []



    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
