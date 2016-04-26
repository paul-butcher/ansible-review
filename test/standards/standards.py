from ansiblereview import Standard, Result, Error, lintcheck


def check_fail(candidate, settings):
    return Result(candidate,[Error(1, "test failed")])


def check_success(candidate, settings):
    return Result(candidate)


test_play_ansiblelint_success = Standard(dict(
    check = lintcheck('TEST0004'),
    name = "Test play lint success",
    version = "0.1",
    types = "playbook"
))

test_play_ansiblelint_failure = Standard(dict(
    check = lintcheck('TEST0003'),
    name = "Test play lint failure",
    version = "0.3",
    types = "playbook"
))

test_task_ansiblelint_success = Standard(dict(
    check = lintcheck('TEST0002'),
    name = "Test task lint success",
    version = "0.2",
    types = "playbook,tasks"
))

test_task_ansiblelint_failure = Standard(dict(
    check = lintcheck('TEST0001'),
    name = "Test task lint failure",
    version = "0.4",
    types = "playbook,tasks"
))

test_failure = Standard(dict(
    check = check_fail,
    name = "Test general failure",
    version = "0.5",
    types = "playbook,tasks,vars"
))

test_success = Standard(dict(
    check = check_success,
    name = "Test general success",
    version = "0.2",
    types = "playbook,tasks,vars"
))


standards = [
        test_play_ansiblelint_success,
        test_play_ansiblelint_failure,
        test_task_ansiblelint_success,
        test_task_ansiblelint_failure,
        test_success,
        test_failure,
]
