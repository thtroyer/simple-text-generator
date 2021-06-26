from dataclasses import dataclass
from typing import IO
import chevron
import logging
logger = logging.getLogger("ui")


@dataclass
class State:
    status: str
    iterations_run: str
    latest_model_saved: str

    def render(self, mustache_file: IO) -> str:
        return (chevron.render(mustache_file, {
            'status': self.status,
            'iterations_run': self.iterations_run,
            'latest_model_saved': self.latest_model_saved
        }))


def create_state(state_data) -> State:
    status = state_data['status']
    iterations_run = state_data['iterations_run']
    latest_model_saved = state_data['latest_model_saved']

    return State(status, iterations_run, latest_model_saved)
