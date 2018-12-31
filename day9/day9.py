class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


class CircularLinkedList:
    def __init__(self, initial: int):
        self.head = Node(initial)
        self.head.next = self.head
        self.head.prev = self.head

    def remove(self):
        value = self.head.data
        self.head.next.prev = self.head.prev
        self.head.prev.next = self.head.next
        self.head = self.head.next

        return value

    def insert_after(self, value):
        new_node = Node(value)
        self.head.next.prev = new_node
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next = new_node
        self.head = new_node

    def advance_head(self):
        self.head = self.head.next

    def rewind_head(self, amount):
        while amount > 0:
            self.head = self.head.prev
            amount -= 1

    def __str__(self):
        start_value_of_head = self.head.data
        string = '({})'.format(start_value_of_head)
        while True:
            self.head = self.head.next
            if self.head.data == start_value_of_head:
                break
            string = '{} {}'.format(string, self.head.data)

        return string


if __name__ == '__main__':
    number_of_players = 10
    max_marble_score = 300

    player_scores = [0 for _ in range(0, number_of_players)]

    marble_circle = CircularLinkedList(0)

    current_marble_score = 1
    current_player = 0
    while current_marble_score <= max_marble_score:
        # if the marble that is about to be placed has a number which is a multiple of 23
        if current_marble_score % 23 == 0:
            # First, the current player keeps the marble they would have place, adding it to their score
            player_scores[current_player] += current_marble_score

            # The marble 7 marbles counter-clockwise from the current marble is removed from the circle and
            # also added to the current player's score.
            marble_circle.rewind_head(7)
            removed_marble = marble_circle.remove()
            player_scores[current_player] += removed_marble
        else:
            # Placing the lowest-numbered remaining marble into the circle
            # between the marbles that are 1 and 2 marbles clockwise
            marble_circle.advance_head()
            marble_circle.insert_after(current_marble_score)

        current_marble_score += 1
        current_player += 1
        current_player = current_player % len(player_scores)

    print("Marble circle:", marble_circle)

    print("Player scores", [score for score in player_scores])

    print("Highest score", max(player_scores))
