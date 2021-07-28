from simpletextgenerator.models.state import State


def test_state_creation():
    status = "status"
    iterations_run = "5"
    latest_model_saved = "some_model.hdf5"
    state = State(status, iterations_run, latest_model_saved)

    assert state.status == status
    assert state.iterations_run == iterations_run
    assert state.latest_model_saved == latest_model_saved


def test_state_render():
    status = "status"
    iterations_run = "5"
    latest_model_saved = "some_model.hdf5"
    state = State(status, iterations_run, latest_model_saved)

    with open("../templates/state.yml.mustache", "r") as f:
        assert state.render(f) == f"status: {status}\niterations_run: {iterations_run}\nlatest_model_saved: {latest_model_saved}\n"

