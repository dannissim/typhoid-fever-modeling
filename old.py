import matplotlib.pyplot as plt
import numpy as np

# Real-life data (number of infectious individuals per community over time)
real_data = np.array([[10, 15, 20, 25, 20, 15, 10, 5], [5, 10, 15, 20, 25, 20, 15, 10],
                      [8, 12, 15, 18, 20, 18, 15, 12], [3, 6, 9, 12, 15, 18, 15, 12],
                      [15, 20, 25, 30, 35, 30, 25, 20]])

# Parameters
num_communities = 5  # Number of communities
population_per_community = 2000  # Population per community
transmission_rate = 0.8  # Probability of transmission
recovery_rate = 0.1  # Probability of recovery
movement_rate = 0.05  # Probability of movement between communities
intervention_start = 50  # Time step at which intervention starts
intervention_effectiveness = 0.5  # Effectiveness of intervention (reduction in transmission rate)

# Calculate total population size
population_size = num_communities * population_per_community

# Initialize compartments using real data
infectious = real_data[:, 0]
susceptible = np.full((num_communities, ), population_per_community) - infectious
recovered = np.zeros((num_communities, ))

# Lists to store population counts over time
susceptible_counts = [susceptible.copy()]
infectious_counts = [infectious.copy()]
recovered_counts = [recovered.copy()]

# Simulation time steps
num_steps = len(real_data[0]) - 1

# Run simulation
for t in range(num_steps):
    # Calculate new infections and recoveries
    new_infections = np.random.binomial(susceptible,
                                        transmission_rate * infectious / population_per_community)
    new_recoveries = np.random.binomial(infectious, recovery_rate)

    # Apply intervention measures
    if t >= intervention_start:
        transmission_rate *= (1 - intervention_effectiveness)

    # Update compartment counts
    susceptible -= new_infections
    infectious += new_infections - new_recoveries
    recovered += new_recoveries

    # Update movement between communities
    for i in range(num_communities):
        movement = np.random.binomial(susceptible[i], movement_rate)
        susceptible[i] -= movement
        susceptible[(i + 1) % num_communities] += movement

    # Update infectious counts using real data
    infectious = real_data[:, t + 1]

    # Store compartment counts
    susceptible_counts.append(susceptible.copy())
    infectious_counts.append(infectious.copy())
    recovered_counts.append(recovered.copy())

# Convert compartment counts to numpy arrays
susceptible_counts = np.array(susceptible_counts)
infectious_counts = np.array(infectious_counts)
recovered_counts = np.array(recovered_counts)

# Plotting the results
time = np.arange(num_steps + 1)
plt.figure(figsize=(10, 6))
plt.plot(time, susceptible_counts.sum(axis=1), label='Susceptible')
plt.plot(time, infectious_counts.sum(axis=1), label='Infectious')
plt.plot(time, recovered_counts.sum(axis=1), label='Recovered')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Cholera Spread in Poor Indian Communities (Robust SIR Model)')
plt.legend()
plt.show()
