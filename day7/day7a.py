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


if __name__ == '__main__':
    puzzle_input = input_parser.read_file_lines("input.txt")

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


    for s in steps:
        print(s)

    executed_steps = ""

   # first_step_to_do = next(filter(lambda x: x.requirements in list(executed_steps), steps))

    while True:
        next_step = find_next_possible_task(executed_steps)
        if next_step is None:
            break

        executed_steps += next_step.step_id

    print(executed_steps)
