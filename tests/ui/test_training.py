from unittest.mock import MagicMock, patch
import sys

# Mock tkinter before importing anything
sys.modules['tkinter'] = MagicMock()
sys.modules['tkinter.scrolledtext'] = MagicMock()
sys.modules['tkinter.ttk'] = MagicMock()

# Import base module so we can monkeypatch BaseWindow
import simpletextgenerator.ui.base

class MockBaseWindow:
    def __init__(self, parent, title):
        pass
    def destroy(self):
        pass

# Monkeypatch BaseWindow
simpletextgenerator.ui.base.BaseWindow = MockBaseWindow

# Now import TrainingWindow
from simpletextgenerator.ui.training import TrainingWindow

def test_get_percentage_bar1():
    # We mock _init_ui and periodic_callback
    with patch.object(TrainingWindow, '_init_ui', return_value=None), \
         patch.object(TrainingWindow, 'periodic_callback', return_value=None):
        training_window = TrainingWindow(None, None, None)

        result = training_window.get_percentage_bar1("9 / 340[..............................] - ETA: 5s - loss: 1.6054")
        assert result == 0

        result = training_window.get_percentage_bar1("9 / 340[==>...........................] - ETA: 5s - loss: 1.6054")
        assert result == 6


def test_get_percentage_bar2():
    with patch.object(TrainingWindow, '_init_ui', return_value=None), \
         patch.object(TrainingWindow, 'periodic_callback', return_value=None):
        training_window = TrainingWindow(None, None, None)

        result = training_window.get_percentage_bar2("20%|██        | 1/5 [00:04<00:19,  4.85s/it]")
        assert result == "20"

        training_window = TrainingWindow(None, None, None)
        result = training_window.get_percentage_bar2("80%|████████  | 4/5 [00:13<00:03,  3.12it/s]")
        assert result == "80"
