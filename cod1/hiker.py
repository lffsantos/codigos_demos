class Hiker:

    def __init__(self, sequency=[]):
        self.sequency = sequency
        self.sequency.sort()

    def min_value_seq(self):
        return self.sequency[:1][0] if self.sequency else 0

    def max_value_seq(self):
        return self.sequency[::-1][0] if self.sequency else 0

    def number_elements(self):
        return len(self.sequency)

    def avg_seq(self):
        if self.sequency:
            avg = sum(self.sequency)/len(self.sequency)
            return float("%.6f" % avg)
        else:
            return 0

