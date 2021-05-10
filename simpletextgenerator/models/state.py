from dataclasses import dataclass


@dataclass
class State:
    status: str
    iterations_run: str
    latest_model_saved: str


def create_state(state_data) -> State:
    status = state_data['status']
    iterations_run = state_data['iterations_run']
    latest_model_saved = state_data['latest_model_saved']

    return State(status, iterations_run, latest_model_saved)
