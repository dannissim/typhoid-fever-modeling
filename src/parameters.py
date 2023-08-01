import pydantic


class Parameters(pydantic.BaseModel):
    initial_infected: int
    initial_susceptible: int
    initial_recovered: int
    transmission_rate: float
    recovery_rate: float
    weeks_simulation: int
    chronic_rate: float
    sanitation_improvement_rate: float
    relative_transmission_rate_of_chronic: float
