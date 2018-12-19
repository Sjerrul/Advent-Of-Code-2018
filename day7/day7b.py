import re

from common import input_parser
from day7.logic.Step import Step


def find_next_possible_task(executed_steps):
    for step in steps:
        if (step.step_id in list(executed_steps)):
            continue

        all_requirements_done = True
        for requirement in step.requirements:
            if requirement not in list(executed_steps):
                all_requirements_done = False
        if all_requirements_done:
            return step

    return None

class Worker:
    id_ = None
    assigned_task = None
    seconds_performing_task = None

    def __init__(self, id_):
        self.id_ = id_

    def assign_task(self, task):
        self.assigned_task = task
        self.seconds_performing_task = 1  # first second counts

    def work(self):
        if self.assigned_task is not None:
            self.seconds_performing_task += 1

    def is_finished_with_task(self):
        if self.assigned_task is None:
            return True

        return self.get_task_length() - self.seconds_performing_task < 0

    def get_task_length(self):
        if self.assigned_task is not None:
            return 60 + ord(self.assigned_task.lower()) - 96  # TODO: Factor out the base step length

        return None

    def __repr__(self):
        return "Worker %s - assigned_task: %s, seconds_performing_task: %s" % (self.id_, self.assigned_task, self.seconds_performing_task)


if __name__ == '__main__':
    puzzle_input = input_parser.read_file_lines("input.txt")
    # puzzle_input = input_parser.read_file_lines("input-ex.txt")

    steps = []
    for line in puzzle_input:
        parts = re.search('Step (.*) must be finished before step (.*) can begin.', line)
        requirement = parts[1]
        actual_step = parts[2]

        if len([x for x in steps if x.step_id == actual_step]) is 0:
            step = Step(actual_step)
            step.add_requirement(requirement)
            steps.append(step)
        else:
            [x for x in steps if x.step_id == actual_step][0].add_requirement(requirement)

        if len([x for x in steps if x.step_id == requirement]) is 0:
            step = Step(requirement)
            steps.append(step)

    steps.sort(key=lambda x: x.step_id)
    for step in steps:
        step.requirements.sort()

    total_number_of_steps = len(steps)

    for s in steps:
        print(s)

    workers = []
    for i in range(0, 5):
        workers.append(Worker(i))

    second = 0
    executed_steps = ""
    while len(executed_steps) < total_number_of_steps: # todo: change this to something dynamic
        print("second", second)
        for worker in workers:
            worker.work()
            if worker.is_finished_with_task():
                if worker.assigned_task is not None:
                    executed_steps += worker.assigned_task

                next_step = find_next_possible_task(executed_steps)
                #print(next_step)
                if next_step is not None:
                    worker.assign_task(next_step.step_id)
                    steps.remove(next_step)
                else:
                    worker.assign_task(None)

            print(worker)
        # foreach worker
            # Check if current task its doing is finished
            # Mark that task (if any) as finished

            # assign a new task to the worker
            # mark that task as being done

        second += 1

    for worker in workers:
        print(worker)

    print(executed_steps, len(executed_steps))
    print(second - 1)

    ## TODO: Fix to get CORRECT ANSWER: 1105
