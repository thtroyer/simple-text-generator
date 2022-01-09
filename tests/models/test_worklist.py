from simpletextgenerator.models.worklist import WorkItem, WorkList, TrainingWorkItem, GeneratingWorkItem


def test_trainingWorkItem():
    training_work_item = TrainingWorkItem(50)
    assert (training_work_item.get_time_estimate(training_rate=50)) == 1
    assert (training_work_item.get_time_estimate(training_rate=1.0)) == 50
    assert (training_work_item.get_time_estimate(training_rate=1.2)) == 50 / 1.2


def test_generatingWorkItem():
    generating_work_item = GeneratingWorkItem(50)
    assert (generating_work_item.get_time_estimate(generation_rate=50)) == 1
    assert (generating_work_item.get_time_estimate(generation_rate=1.0)) == 50
    assert (generating_work_item.get_time_estimate(generation_rate=1.2)) == 50 / 1.2


def test_Worklist_get_time_estimate():
    workList = WorkList(
        (
            GeneratingWorkItem(50), TrainingWorkItem(200)
        )
    )
    workList.set_training_rate(2)
    workList.set_generating_rate(1)

    assert workList.get_time_estimate() == 150


def test_Worklist_get_time_estimate_progress():
    workList = WorkList(
        (
            TrainingWorkItem(200),
            GeneratingWorkItem(50)
        )
    )
    workList.set_training_rate(2)
    workList.set_generating_rate(1)

    assert workList.get_time_estimate() == 150

    workList.set_progress_on_current_work_item(0.5)

    assert workList.get_time_estimate() == 100

    workList.set_progress_on_current_work_item(0.75)

    assert workList.get_time_estimate() == 75


def test_Worklist_advance_index():
    workList = WorkList(
        (
            GeneratingWorkItem(50),
            GeneratingWorkItem(50),
            TrainingWorkItem(100),
            TrainingWorkItem(100)
        )
    )

    workList.set_training_rate(1)
    workList.set_generating_rate(1)

    assert workList.get_time_estimate() == 300
    workList.advance_index()
    assert workList.get_time_estimate() == 250
    workList.advance_index()
    assert workList.get_time_estimate() == 200
    workList.advance_index()
    assert workList.get_time_estimate() == 100
    workList.advance_index()
    assert workList.get_time_estimate() == 0

    # make sure advancing too far doesn't cause problem
    workList.advance_index()
    assert workList.get_time_estimate() == 0
