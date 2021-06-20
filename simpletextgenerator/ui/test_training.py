from unittest import TestCase

from simpletextgenerator.ui.training import TrainingWindow


class TestTrainingWindow(TestCase):
    def test_get_percentage_bar1(self):
        training_window = TrainingWindow(None, None, None)
        result = training_window.get_percentage_bar1("9 / 340[..............................] - ETA: 5s - loss: 1.6054")
        print(str(result))
        self.assertEqual(first=result, second=0, msg="fail")
        result = training_window.get_percentage_bar1("9 / 340[==>...........................] - ETA: 5s - loss: 1.6054")
        print(str(result))
        self.assertEqual(first=result, second=6, msg="fail")
