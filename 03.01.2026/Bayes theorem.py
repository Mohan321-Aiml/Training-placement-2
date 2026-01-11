def bayes_theorem(prior_A, likelihood_B_given_A, probability_B):
    posterior_A_given_B = (likelihood_B_given_A * prior_A) / probability_B
    return posterior_A_given_B

prior_A = float(input("Enter prior probability P(A): "))
likelihood_B_given_A = float(input("Enter likelihood P(B|A): "))
probability_B = float(input("Enter total probability P(B): "))

posterior = bayes_theorem(prior_A, likelihood_B_given_A, probability_B)
print(f"Posterior Probability P(A|B): {posterior:.4f}")
