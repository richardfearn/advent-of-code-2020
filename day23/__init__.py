ONE_MILLION = 1_000_000
NONE = 0


def part_1(cups, moves):

    cups = [int(c) for c in cups]
    circle = CupCircle(cups)

    for move in range(moves):
        circle.move()

    circle.current = 1
    return circle.label_string()[1:]


def part_2(cups, moves, extend):

    cups = [int(c) for c in cups]
    circle = CupCircle(cups, extend)

    for move in range(moves):
        circle.move()

    circle.current = 1
    second = circle.next[circle.current]
    third = circle.next[second]
    return second * third


class CupCircle:

    def __init__(self, items, extend=False):

        self.max = ONE_MILLION if extend else len(items)
        self.next = [NONE] * (self.max + 1)

        for i in range(1, len(items)):
            self.next[items[i - 1]] = items[i]

        if not extend:
            self.next[items[-1]] = items[0]

        else:
            max_item = max(items)
            self.next[items[-1]] = (max_item + 1)
            for i in range(max_item + 1, ONE_MILLION):
                self.next[i] = i + 1
            self.next[ONE_MILLION] = items[0]

        self.current = items[0]

    def move(self):

        # 1a. Find the 3 cups to pick up
        first = self.next[self.current]
        second = self.next[first]
        third = self.next[second]
        picked_up = {first, second, third}

        # 1b. Take the 3 cups out of the circle
        self.next[self.current] = self.next[third]
        self.next[third] = NONE

        # 2. Work out the destination
        dest = self.current - 1
        if dest == 0:
            dest = self.max
        while dest in picked_up:
            dest -= 1
            if dest == 0:
                dest = self.max

        # 3. Replace the 3 cups
        self.next[third] = self.next[dest]
        self.next[dest] = first

        # 4. Select new current cup
        self.current = self.next[self.current]

    def label_string(self):
        labels = []
        current = self.current
        for i in range(self.max):
            labels.append(current)
            current = self.next[current]
        return "".join(str(label) for label in labels)
