def probability(favorable, total):
    return favorable / total

favorable = int(input("Enter number of favorable outcomes: "))
total = int(input("Enter total number of outcomes: "))

print("Probability of event occurring:", probability(favorable, total))
