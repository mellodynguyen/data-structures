"""Functions to parse a file containing villager data."""

# line order in the file 
# name -> species -> personality -> hobby -> motto
# [0]     [1]        [2]            [3]      [4]

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()


    file = open(filename)
    for line in file:
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

    file = open("filename")
    for line in file:
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
    # main_list = [fitness[(villagers with fitness)], nature[], educaiton[], music[], fashion[], play[]]
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    # main list the hobbies will go into 
    main_list = []

    # line order in the file 
    # name -> species -> personality -> hobby -> motto
    # [0]     [1]        [2]            [3]      [4]
    file = open(filename)
    for line in file: 
        name = line.rstrip().split("|")[0]
        hobby = line.rstrip().split("|")[3]
        # name, hobby = line.rstrip().split("|")
        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
        elif hobby == "Play":
            play.append(name)
    
    # main_list.append(fitness)
    # main_list.append(nature)
    # main_list.append(education)
    # main_list.append(music)
    # main_list.append(fashion)
    # main_list.append(play)

    main_list = [fitness, nature, education, music, fashion, play]
    return main_list
    
    # print statement to see if it is appending the whole fitness list to main list 
    # print(main_list)

    # testing if list are appending every name to their respective list

    # print(f"Fitness: {fitness}")
    # print(f"Nature: {nature}")
    # print(f"Education {education}")
    # print(music)
    # print(fashion)
    # print(play)

# all_names_by_hobby("villagers.csv")

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

    # sentence/line structure 
    # Cyrano|Anteater|Cranky|Education|Don't punch your nose to spite your face.

    # what the tuple should look like:
    # ('cyrano', 'anteater', 'cranky', 'education', 'Don't punch your nose to spite your face')

    file= open(filename)
    for line in file:
        name, species, personality, hobby, motto = line.rstrip().split("|")[0:]
        
        all_info = tuple(line.rstrip().split("|")[0:])
        # cant use -> tuple(name, species, personality, hobby, motto) // tuples take 1 argument at a time 
        all_data.append(all_info)

    
    # all_data being the list that contains the tuples -> all_data = (insert tupes)
    
    return all_data
# print(all_data("villagers.csv"))

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

    filename = open("villagers.csv")
    for line in filename:
        name = line.rstrip().split("|")[0]
        motto = line.rstrip().split("|")[4]
        if name == villager_name:
            #print to see if it works
            # print(motto)
            return motto


# find_motto("villagers.csv", "Pinky")


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
    likeminded_villagers = set()
    same_personality = None

    # file = open(filename)
    for villager_data in all_data(filename):
        name, _, personality = villager_data[:3]
        if villager_name == name:
            # print(personality)
            same_personality = personality
            break
    
    if same_personality:
        for villager_data in all_data(filename):
            name, _, personality = villager_data[:3]
            if personality == same_personality:
                likeminded_villagers.add(name)
        
    return likeminded_villagers

# print(find_likeminded_villagers("villagers.csv", "Olaf"))
