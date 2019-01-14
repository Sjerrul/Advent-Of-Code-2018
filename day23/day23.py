import re
import networkx as nx
from collections import namedtuple
from operator import attrgetter


INPUT_PATTERN = re.compile(r'pos=<([+-]?\d+),([+-]?\d+),([+-]?\d+)>, r=([+-]?\d+)')


class Nanobot(namedtuple('Nanobot', 'x y z strength')):
    def __str__(self):
        return "<Nanobot ({}, {}, {}) - {}>".format(self.x, self.y, self.z, self.strength)

    @classmethod
    def from_input(cls, line):
        match = INPUT_PATTERN.match(line)
        if match:
            return cls(*map(int, match.groups()))

def parse_input(file_path):
    with open(file_path, "r") as f:
        for line in f:
            yield Nanobot.from_input(line)


def manhattan_distance(bot1, bot2):
    return abs(bot1.x - bot2.x) + abs(bot1.y - bot2.y) + abs(bot1.z - bot2.z)

def manhattan_distance2(x, y, z, bot2):
    return abs(x - bot2.x) + abs(y - bot2.y) + abs(z - bot2.z)

def is_in_range(x, y, z, bot):
    return (abs(x - bot.x) + abs(y - bot.y) + abs(z - bot.z)) <= bot.strength


def find_limits(bots):
    all_x = [bot.x for bot in bots]
    all_y = [bot.y for bot in bots]
    all_z = [bot.z for bot in bots]

    limits = namedtuple("limits", "min_x min_y min_z max_x max_y max_z")
    return limits(min_x=min(all_x), min_y=min(all_y), min_z=min(all_z),
                  max_x=max(all_x), max_y=max(all_y), max_z=max(all_z))


if __name__ == '__main__':
    bot_generator = parse_input("input.txt")
    bots = list(bot_generator)

    strongest_bot = max(bots, key=attrgetter('strength'))
    print("Strongest bot:", strongest_bot)

    bots_in_range = 0
    for bot in bots:
        if manhattan_distance(strongest_bot, bot) <= strongest_bot.strength:
            bots_in_range += 1

    print("No. of bots in range of strongest bot", bots_in_range)

    print("build a graph with edges between overlapping nanobots")
    graph = nx.Graph()
    for bot in bots:
        # two bots overlap if their distance is smaller or equal than the sum of their ranges
        overlaps = [(bot, other) for other in bots if manhattan_distance(bot, other) <= bot.strength + other.strength]
        graph.add_edges_from(overlaps)

    print("find sets of overlapping nanobots (i.e. fully-connected sub-graphs)")
    cliques = list(nx.find_cliques(graph))
    cliques_size = [len(c) for c in cliques]

    assert len([s for s in cliques_size if s == max(cliques_size)]) == 1

    print("select the largest cluster of overlapping nanobots (maximum clique sub-graph)")
    clique = max(cliques, key=len)

    print("calculate the point on the nanobots surface which is closest to the origin")
    surfaces = [manhattan_distance2(0, 0, 0, bot) - bot.strength for bot in clique]

    print("the furthest away surface point is the minimum manhattan distance")
    print(max(surfaces))