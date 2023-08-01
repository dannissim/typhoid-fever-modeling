import pydantic


class Parameters(pydantic.BaseModel):
    initial_infected: int
    initial_susceptible: int
    initial_recovered: int
    transmission_rate: float
    recovery_rate: float
    days_simulation: int
