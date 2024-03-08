import random

class DNA:
    def __init__(self, sequence):
        self.sequence = sequence
        self.fitness = evaluate_fitness(sequence)

def evaluate_fitness(sequence):
    # Örneğin, belirli bir dizinin belirli bir özelliği taşıması daha yüksek fitness değerini sağlasın
    if "AAA" in sequence:
        return len(sequence) * 2
    else:
        return len(sequence)

def mutate(dna):
    mutation_type = random.choice(["substitution", "deletion", "insertion"])
    mutation_point = random.randint(0, len(dna.sequence) - 1)

    if mutation_type == "substitution":
        mutated_base = random.choice("ACTG")
        mutated_sequence = list(dna.sequence)
        mutated_sequence[mutation_point] = mutated_base
        return DNA("".join(mutated_sequence))
    elif mutation_type == "deletion" and len(dna.sequence) > 1:
        mutated_sequence = list(dna.sequence)
        del mutated_sequence[mutation_point]
        return DNA("".join(mutated_sequence))
    elif mutation_type == "insertion":
        mutated_base = random.choice("ACTG")
        mutated_sequence = list(dna.sequence)
        mutated_sequence.insert(mutation_point, mutated_base)
        return DNA("".join(mutated_sequence))
    else:
        return dna

def compete(population):
    # Popülasyon içinde rekabeti simüle et
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[:len(population)//2]

def simulate_evolution(initial_sequence, population_size, generations):
    population = [DNA(initial_sequence) for _ in range(population_size)]

    for generation in range(generations):
        # Mutate DNA
        mutated_population = [mutate(dna) for dna in population]

        # Evaluate fitness
        for dna in mutated_population:
            dna.fitness = evaluate_fitness(dna.sequence)

        # Compete and select the fittest
        population = compete(population + mutated_population)

        # Print current state (optional)
        print(f"Generation {generation + 1}: {population[0].sequence} (Fitness: {population[0].fitness})")

if __name__ == "__main__":
    initial_sequence = "AAAAAA"
    population_size = 100
    generations = 100
    simulate_evolution(initial_sequence, population_size, generations)
