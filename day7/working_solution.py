# Gotten from Reddit: https://www.reddit.com/r/adventofcode/comments/a3wmnl/2018_day_7_solutions/eb9zcvl

from functools import total_ordering
from string import ascii_uppercase

from parse import parse
import networkx as nx
import traitlets

node_costs = {
    letter: i + 61 for i, letter in enumerate(ascii_uppercase)
}
pattern = 'Step {start} must be finished before step {stop} can begin.'
sleigh_steps = nx.DiGraph()

for line in open('input.txt'):
    result = parse(pattern, line)
    sleigh_steps.add_edge(result['start'], result['stop'])

nodes = list(nx.lexicographical_topological_sort(sleigh_steps))
completed_nodes = set()
ordered_completed_nodes = []


@total_ordering
class Worker(traitlets.HasTraits):
    node = traitlets.Unicode(allow_none=True)
    time_left = traitlets.Integer(default_value=0)
    is_working = traitlets.Bool(default_value=False)

    def __eq__(self, other):
        return self.time_left == other.time_left

    def __lt__(self, other):
        return self.time_left < other.time_left

    def tick(self, time):
        self.time_left -= time
        if self.time_left <= 0:
            self.is_working = False
            completed_nodes.add(self.node)
            ordered_completed_nodes.append(self.node)
            self.node = None

    def assign_task(self, node):
        self.node = node
        self.time_left = node_costs[node]
        self.is_working = True


workers = [Worker() for i in range(5)]
total_time = 0

while len(completed_nodes) < len(sleigh_steps):
    available_nodes = []
    for node in nodes:
        ancestors = nx.ancestors(sleigh_steps, node)
        if not ancestors - completed_nodes:
            available_nodes.append(node)

    available_workers = (
        w for w in workers
        if not w.is_working
    )

    for worker, node in zip(available_workers, available_nodes):
        worker.assign_task(node)
        nodes.remove(node)

    active_workers = [
        w for w in workers
        if w.is_working
    ]

    tick = min(active_workers).time_left
    total_time += tick
    for worker in active_workers:
        worker.tick(tick)


print(''.join(ordered_completed_nodes))
print(total_time)
