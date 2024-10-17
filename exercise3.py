#write the program that has the following:
#1.generate 100 random integers between 1 and 50 and store them in list.
#2.compute the mean, median, mode and standard duration of the members in the list.
#my program code
import random
import statistics

def generate_random_integers(n, lower_bound, upper_bound):
    """Generate a list of n random integers between lower_bound and upper_bound."""
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]

def main():
    random_integers = generate_random_integers(100, 1, 50)
    mean = statistics.mean(random_integers)
    median = statistics.median(random_integers)
    mode = statistics.mode(random_integers)
    std_dev = statistics.stdev(random_integers)

    # Print results
    print("Random Integers:", random_integers)
    print(f"Mean: {mean:.2f}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_dev:.2f}")


