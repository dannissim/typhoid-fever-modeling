import pathlib
import sys

import streamlit as st

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))
from src import sir
from src.parameters import Parameters

DEFAULT_PARAMETERS = Parameters(initial_infected=10,
                                initial_susceptible=10000,
                                initial_recovered=0,
                                transmission_rate=0.63,
                                recovery_rate=0.25,
                                weeks_simulation=50,
                                chronic_rate=0.05,
                                sanitation_improvement_rate=0.01,
                                relative_transmission_rate_of_chronic=0.01)

MARKDOWN_FILE_PATH_1 = pathlib.Path('src/static/typhoid1.md')
MARKDOWN_FILE_PATH_2 = pathlib.Path('src/static/typhoid2.md')
MARKDOWN_FILE_PATH_3 = pathlib.Path('src/static/typhoid3.md')
MARKDOWN_FILE_PATH_4 = pathlib.Path('src/static/typhoid4.md')
MARKDOWN_FILE_PATH_5 = pathlib.Path('src/static/typhoid5.md')
MARKDOWN_FILE_PATH_6 = pathlib.Path('src/static/typhoid6.md')


def parameters_inputs() -> Parameters:
    col1, col2 = st.columns(2)
    with col1:
        initial_susceptible = st.slider('S Initial Susceptible',
                                        1,
                                        10**5,
                                        value=DEFAULT_PARAMETERS.initial_susceptible,
                                        step=1000)

        initial_infected = st.slider('I Initial Infected',
                                     0,
                                     100,
                                     value=DEFAULT_PARAMETERS.initial_infected,
                                     step=1)
        initial_recovered = st.slider('R Initial Recovered',
                                      0,
                                      10**5,
                                      value=DEFAULT_PARAMETERS.initial_recovered,
                                      step=1000)
        relative_transmission_rate_of_chronic = st.slider(
            'Relative Transmission Rate of Chronic Carriers',
            0.0,
            1.0,
            value=DEFAULT_PARAMETERS.chronic_rate,
            step=0.01)
        sanitation_improvement_rate = st.slider(
            'λ Sanitation Improvement Rate',
            0.0,
            0.1,
            value=DEFAULT_PARAMETERS.sanitation_improvement_rate,
            step=0.001,
            format='%f')

    with col2:
        transmission_rate = st.slider('β Transmission Rate',
                                      0.0,
                                      3.0,
                                      value=DEFAULT_PARAMETERS.transmission_rate,
                                      step=0.01)
        recovery_rate = st.slider('γ Recovery Rate',
                                  0.0,
                                  1.0,
                                  value=DEFAULT_PARAMETERS.recovery_rate,
                                  step=0.01)
        weeks_simulation = st.slider('Number of Weeks to Simulate',
                                     10,
                                     200,
                                     value=DEFAULT_PARAMETERS.weeks_simulation,
                                     step=5)
        chronic_rate = st.slider('θ New Chronic Carriers Rate',
                                 0.0,
                                 1.0,
                                 value=DEFAULT_PARAMETERS.chronic_rate,
                                 step=0.01)

    return Parameters(initial_infected=initial_infected,
                      initial_susceptible=initial_susceptible,
                      initial_recovered=initial_recovered,
                      transmission_rate=transmission_rate,
                      recovery_rate=recovery_rate,
                      weeks_simulation=weeks_simulation,
                      chronic_rate=chronic_rate,
                      sanitation_improvement_rate=sanitation_improvement_rate,
                      relative_transmission_rate_of_chronic=relative_transmission_rate_of_chronic)


def background():
    st.markdown(MARKDOWN_FILE_PATH_1.read_text(encoding='utf-8'), unsafe_allow_html=True)
    st.image('src/static/map1.png')
    st.image('src/static/map2.png', caption='Maps of global outbreaks')
    st.markdown(MARKDOWN_FILE_PATH_2.read_text(encoding='utf-8'), unsafe_allow_html=True)
    st.image('src/static/graph1.png', caption='Open defecation levels in India over time')
    st.markdown(MARKDOWN_FILE_PATH_3.read_text(encoding='utf-8'), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image(
            'src/static/gram_vikas1.png',
            caption='Laxmi, in the yellow and pink dress with other trainees in the mason training.'
        )
    with col2:
        st.image('src/static/gram_vikas2.png',
                 caption='A local woman enjoying newly available running water.')
    st.image(
        'src/static/gram_vikas3.png',
        caption='A community meeting in progress in Satapatia village, Nayagarh district, Odisha')
    st.markdown(MARKDOWN_FILE_PATH_4.read_text(encoding='utf-8'), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image(
            'src/static/model_graph1.png',
            caption=
            '(Top) Weekly incidence of observed (blue line) and model-predicted (thick red line)'
            ' typhoid inpatients at Christian Medical College hospital in Vellore, India. '
            'The thin red line represents a simulated incidence time-series for the best-fit '
            'model assuming the number of cases each week is Poisson distributed with a mean '
            'equal to the model-predicted incidence.\n(Bottom) Age distribution of observed (blue) '
            'and model-predicted (red) typhoid cases.')
    with col2:
        st.image('src/static/model_graph2.png',
                 caption='A diagram of the paper\'s model structure.')
    st.markdown(MARKDOWN_FILE_PATH_5.read_text(encoding='utf-8'), unsafe_allow_html=True)


def title():
    st.title('Typhoid Fever Modeling')
    st.markdown(
        'Below is my analysis of Typhoid Fever transmission in India, using a dynamic mathematical '
        'model. Enjoy!<br/>'
        'The app was developed by Dan Nissim in July, 2023, as a part of the submission requirements'
        ' for the course "Mathematical Modeling of Epidemics" at Tel Aviv University. '
        'Feel free to <a href="mailto:nissim.dan@gmail.com">contact me</a>.',
        unsafe_allow_html=True)


def conclusion():
    st.markdown(MARKDOWN_FILE_PATH_6.read_text(encoding='utf-8'), unsafe_allow_html=True)


def main():
    title()
    background()
    parameters = parameters_inputs()
    sir.plot(parameters)
    conclusion()


if __name__ == '__main__':
    main()
