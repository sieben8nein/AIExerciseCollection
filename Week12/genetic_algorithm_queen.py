import random
import math

from Week12.queens_fitness import fitness_fn_negative, fitness_fn_positive

p_mutation = 0.2
num_of_generations = 30


def genetic_algorithm(population, fitness_fn, minimal_fitness):
    for generation in range(num_of_generations):
        print("Generation {}:".format(generation))
        #print_population(population, fitness_fn)

        new_population = set()

        for i in range(len(population)):
            mother, father = random_selection(population, fitness_fn)
            child = reproduce(mother, father)

            if random.uniform(0, 1) < p_mutation:
                child = mutate(child)

            new_population.add(child)

        # Add new population to population, use union to disregard
        # duplicate individuals
        population = population.union(new_population)
        fittest_individual = get_fittest_individual(population, fitness_fn)
        if minimal_fitness <= fitness_fn(fittest_individual):
            break

    print("Final generation {}:".format(generation))
    print_population(population, fitness_fn)

    return fittest_individual


def print_population(population, fitness_fn):
    for individual in population:
        fitness = fitness_fn(individual)
        print("{} - fitness: {}".format(individual, fitness))


def reproduce(mother, father):
    '''
    Reproduce two individuals with single-point crossover
    Return the child individual
    '''
    random_crossover = random.randint(0, min(len(mother), len(father)))
    child = mother[:random_crossover] + father[random_crossover:]
    # print("random crossover", random_crossover)
    # print("mother", mother, "father", father)
    # print("child", child)
    return child


def mutate(individual):
    '''
    Mutate an individual by randomly assigning one of its bits
    Return the mutated individual
    '''
    random_position = random.randint(0, len(individual) - 1)
    mutated_individual = list(individual)
    random_bit = random.randint(1, 8)
    mutated_individual[random_position] = random_bit
    # print("individual:", individual, "mutation", mutated_individual)
    return tuple(mutated_individual)


def random_selection(population, fitness_fn):
    """
    Compute fitness of each in population according to fitness_fn and add up
    the total. Then choose 2 from sequence based on percentage contribution to
    total fitness of population
    Return selected variable which holds two individuals that were chosen as
    the mother and the father
    """

    # Python sets are randomly ordered. Since we traverse the set twice, we
    # want to do it in the same order. So let's convert it temporarily to a
    # list.
    ordered_population = list(population)
    total_fittness = 0
    for individual in ordered_population:
        total_fittness += fitness_fn(individual)

    normalized_population = []
    for individual in ordered_population:
        normalized_population.append([individual, fitness_fn(individual) / total_fittness])

    normalized_population.sort(key=lambda x: x[1])

    for i in range(1, len(normalized_population)):
        current_ind_fittness = (normalized_population[i])[1]
        previous_ind_fittness = (normalized_population[i - 1])[1]
        normalized_population[i][1] = current_ind_fittness + previous_ind_fittness

    # print("random selection", normalized_population)

    parents = []
    for i in range(0, 2):
        rand_value = random.uniform(0, 1)
        # print("random value:", rand_value)
        for j in normalized_population:
            if (j[1] >= rand_value):
                parents.append(j[0])
                break
    # print("parents:", parents)
    return parents


def fitness_function(individual):
    '''
    Computes the decimal value of the individual
    Return the fitness level of the individual

    Explanation:
    enumerate(list) returns a list of pairs (position, element):

    enumerate((4, 6, 2, 8)) -> [(0, 4), (1, 6), (2, 2), (3, 8)]

    enumerate(reversed((1, 1, 0))) -> [(0, 0), (1, 1), (2, 1)]
    '''
    if (individual == None):
        return 0
    enu = list(enumerate(reversed(individual)))
    total_fittness = 0
    for value in enu:
        if value[1] != 0:
            total_fittness += math.pow(2, value[0])

    return total_fittness


def get_fittest_individual(iterable, func):
    return max(iterable, key=func)


def get_initial_population(n, count):
    '''
    Randomly generate count individuals of length n
    Note since its a set it disregards duplicate elements.
    '''
    return set([
        tuple(random.randint(0, 1) for _ in range(n))
        for _ in range(count)
    ])


def queen_main():
    #(5, 3, 1, 7, 2, 8, 6, 4) final solution
    minimal_fitness = 0
    initial_population = {
        (2, 4, 7, 4, 8, 5, 5, 2),
        (3, 2, 7, 5, 2, 4, 1, 1),
        (2, 4, 4, 1, 5, 1, 2, 4),
        (5, 3, 1, 7, 2, 8, 6, 5),
    }
    fittest = genetic_algorithm(initial_population, fitness_fn_negative, minimal_fitness)
    print('Fittest Individual: ' + str(fittest))


def main():
    queen_main()


if __name__ == '__main__':
    pass
    main()
