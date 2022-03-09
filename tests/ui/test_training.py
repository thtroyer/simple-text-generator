from simpletextgenerator.ui.training import TrainingWindow


def test_get_percentage_bar1():
    training_window = TrainingWindow(None, None, None)

    result = training_window.get_percentage_bar1("9 / 340[..............................] - ETA: 5s - loss: 1.6054")
    assert result == 0

    result = training_window.get_percentage_bar1("9 / 340[==>...........................] - ETA: 5s - loss: 1.6054")
    assert result == 6


def test_get_percentage_bar2():
    training_window = TrainingWindow(None, None, None)

    result = training_window.get_percentage_bar2("20%|██        | 1/5 [00:04<00:19,  4.85s/it]")
    assert result == "20"

    training_window = TrainingWindow(None, None, None)
    result = training_window.get_percentage_bar2("80%|████████  | 4/5 [00:13<00:03,  3.12it/s]")
    assert result == "80"
