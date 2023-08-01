import matplotlib.pyplot as plt
import streamlit as st

from src.parameters import Parameters


def sir_model(parameters: Parameters):
    st.write(parameters)
    initial_population = parameters.initial_susceptible + parameters.initial_infected + parameters.initial_recovered
    S = parameters.initial_susceptible
    I = parameters.initial_infected
    R = parameters.initial_recovered
    susceptible = [S]
    infected = [I]
    recovered = [R]

    for day in range(parameters.days_simulation):
        new_infected = parameters.transmission_rate * S * I / initial_population
        new_recovered = parameters.recovery_rate * I

        S -= new_infected
        I += new_infected - new_recovered
        R += new_recovered

        S = max(0, S)
        S = min(S, initial_population)
        I = max(0, I)
        I = min(I, initial_population)
        R = max(0, R)
        R = min(R, initial_population)

        S, I, R = round(S), round(I), round(R)

        susceptible.append(S)
        infected.append(I)
        recovered.append(R)

    return susceptible, infected, recovered


def plot(parameters: Parameters):
    S, I, R = sir_model(parameters)
    days_simulation = parameters.days_simulation
    plt.figure(figsize=(10, 6))
    plt.plot(range(days_simulation + 1), S, label="Susceptible")
    plt.plot(range(days_simulation + 1), I, label="Infected")
    plt.plot(range(days_simulation + 1), R, label="Recovered")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.title("Transmission Dynamics of Typhoid Fever (SIR Model)")
    plt.legend()
    plt.grid()
    st.pyplot(plt.gcf(), True)
