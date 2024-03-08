import random

class RNA:
    def __init__(self, sequence):
        self.sequence = sequence
        self.fitness = evaluate_fitness(sequence)

def evaluate_fitness(sequence):
    # Örneğin, belirli bir dizinin belirli bir özelliği taşıması daha yüksek fitness değerini sağlasın
    if "AAA" in sequence:
        return len(sequence) * 2
    else:
        return len(sequence)

def mutate(rna):
    mutation_type = random.choice(["substitution", "deletion", "insertion"])
    mutation_point = random.randint(0, len(rna.sequence) - 1)

    if mutation_type == "substitution":
        mutated_base = random.choice("ACGU")
        mutated_sequence = list(rna.sequence)
        mutated_sequence[mutation_point] = mutated_base
        return RNA("".join(mutated_sequence))
    elif mutation_type == "deletion" and len(rna.sequence) > 1:
        mutated_sequence = list(rna.sequence)
        del mutated_sequence[mutation_point]
        return RNA("".join(mutated_sequence))
    elif mutation_type == "insertion":
        mutated_base = random.choice("ACGU")
        mutated_sequence = list(rna.sequence)
        mutated_sequence.insert(mutation_point, mutated_base)
        return RNA("".join(mutated_sequence))
    else:
        return rna

def compete(population):
    # Popülasyon içinde rekabeti simüle et
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[:len(population)//2]

def simulate_evolution(initial_sequence, population_size, generations):
    population = [RNA(initial_sequence) for _ in range(population_size)]

    for generation in range(generations):
        # Mutate RNA
        mutated_population = [mutate(rna) for rna in population]

        # Evaluate fitness
        for rna in mutated_population:
            rna.fitness = evaluate_fitness(rna.sequence)

        # Compete and select the fittest
        population = compete(population + mutated_population)

        # Print current state (optional)
        print(f"Generation {generation + 1}: {population[0].sequence} (Fitness: {population[0].fitness})")

if __name__ == "__main__":
    initial_sequence = "AAAAAA"
    population_size = 100
    generations = 100
    simulate_evolution(initial_sequence, population_size, generations)
