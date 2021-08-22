import collections


class RunningMean:
    def __init__(self, max_number_of_elements=100):
        self.max_number_of_elements = max_number_of_elements
        self.number_of_elements = 0
        self.elements = collections.deque(maxlen=max_number_of_elements)

    def add(self, number):
        self.elements.append(number)

    def mean(self):
        total = 0
        num_elements = 0
        for i in self.elements:
            total += i
            num_elements += 1

        return round(total / num_elements, 3)
