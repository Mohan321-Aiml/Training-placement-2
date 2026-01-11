import random

def monte_carlo_coin_toss(n):
    heads_count = sum(1 for _ in range(n) if random.choice(["Heads", "Tails"]) == "Heads")
    return heads_count / n

n_simulations = int(input("Enter number of simulations: "))
print(f"Estimated probability of Heads: {monte_carlo_coin_toss(n_simulations):.2f}")
