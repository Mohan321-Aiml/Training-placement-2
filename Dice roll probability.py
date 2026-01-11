from itertools import product

def probability_of_sum(target_sum):
    outcomes = list(product(range(1, 7), repeat=2))
    favorable = sum(1 for outcome in outcomes if sum(outcome) == target_sum)
    return favorable / len(outcomes)

target = int(input("Enter desired sum: "))
print(f"Probability of getting sum {target}: {probability_of_sum(target):.2f}")
