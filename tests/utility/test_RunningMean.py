from simpletextgenerator.utility.RunningMean import RunningMean


def test_3_average():
    running_mean = RunningMean(3)

    running_mean.add(1)
    running_mean.add(2)
    running_mean.add(3)

    assert running_mean.mean() == 2

def test_10_average():
    running_mean = RunningMean(10)

    running_mean.add(1)
    running_mean.add(2)
    running_mean.add(20)
    running_mean.add(-293)
    running_mean.add(192)
    running_mean.add(3.3)
    running_mean.add(30)
    running_mean.add(291)
    running_mean.add(322)
    running_mean.add(323)

    assert running_mean.mean() == 89.13


def test_round_to_3_places():
    running_mean = RunningMean()

    running_mean.add(1)
    running_mean.add(0)
    running_mean.add(0)

    assert running_mean.mean() == 0.333
