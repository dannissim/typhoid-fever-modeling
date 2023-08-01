import matplotlib.pyplot as plt
import streamlit as st

from .parameters import Parameters


def sir_model(parameters: Parameters):
    # st.write(parameters)
    initial_population = parameters.initial_susceptible + parameters.initial_infected + parameters.initial_recovered
    transmission_rate = parameters.transmission_rate
    S = parameters.initial_susceptible
    I = parameters.initial_infected
    R = parameters.initial_recovered
    C = 0
    susceptible = [S]
    infected = [I]
    recovered = [R]
    chronic_carriers = [C]

    for week in range(parameters.weeks_simulation):
        new_infected = transmission_rate * S * I / initial_population + (
            parameters.relative_transmission_rate_of_chronic * transmission_rate * S * C /
            initial_population)
        new_recovered = parameters.recovery_rate * I
        new_chronic_carriers = parameters.chronic_rate * I

        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered
        C += new_chronic_carriers

        transmission_rate *= (1 - parameters.sanitation_improvement_rate)

        S = max(0, S)
        S = min(S, initial_population)
        I = max(0, I)
        I = min(I, initial_population)
        R = max(0, R)
        R = min(R, initial_population)
        C = max(0, C)
        C = min(C, initial_population)

        S, I, R, C = round(S), round(I), round(R), round(C)

        susceptible.append(S)
        infected.append(I)
        recovered.append(R)
        chronic_carriers.append(C)

    return susceptible, infected, recovered, chronic_carriers


def plot(parameters: Parameters):
    S, I, R, C = sir_model(parameters)
    weeks_simulation = parameters.weeks_simulation
    plt.figure(figsize=(10, 6))
    plt.plot(range(weeks_simulation + 1), S, label="Susceptible")
    plt.plot(range(weeks_simulation + 1), I, label="Infected")
    plt.plot(range(weeks_simulation + 1), R, label="Recovered")
    plt.plot(range(weeks_simulation + 1), C, label="Chronic Carriers")
    plt.xlabel("Weeks")
    plt.ylabel("Population")
    plt.title("Transmission Dynamics of Typhoid Fever (SIRC Model)")
    plt.legend()
    plt.grid()
    st.pyplot(plt.gcf(), True)
