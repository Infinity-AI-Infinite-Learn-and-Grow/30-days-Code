import math
from collections import Counter


class Statistics:

    def __init__(self, data):
        self.data = data
        self.length = len(data)

    def mean(self):
        return sum(self.data) / self.length

    def median(self):
        sorted_data = sorted(self.data)
        mid = self.length // 2
        if self.length % 2 == 0:
            return (sorted_data[mid-1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        data_count = Counter(self.data)
        mode_dict = dict(data_count)
        mode = [k for k, v in mode_dict.items() if v == max(
            list(data_count.values()))]
        if len(mode) == self.length:
            return None
        else:
            return mode

    def range(self):
        return max(self.data) - min(self.data)

    def variance(self):
        mean = self.mean()
        return sum((xi - mean) ** 2 for xi in self.data) / (self.length - 1)

    def std_dev(self):
        return math.sqrt(self.variance())

    def min_max(self):
        return min(self.data), max(self.data)

    def count(self):
        return self.length

    def percentile(self, percentile):
        sorted_data = sorted(self.data)
        k = (self.length - 1) * percentile / 100
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return sorted_data[int(k)]
        else:
            d0 = sorted_data[int(f)] * (c - k)
            d1 = sorted_data[int(c)] * (k - f)
            return d0 + d1

    def frequency(self):
        data_count = Counter(self.data)
        freq_dict = dict(data_count)
        for key in freq_dict:
            freq_dict[key] /= self.length
        return freq_dict


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24,
        32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
stats = Statistics(ages)

print("Mean:", stats.mean())
print("Median:", stats.median())
print("Mode:", stats.mode())
print("Range:", stats.range())
print("Variance:", stats.variance())
print("Standard Deviation:", stats.std_dev())
print("Min and Max:", stats.min_max())
print("Count:", stats.count())
print("25th Percentile:", stats.percentile(25))
print("Frequency Distribution:", stats.frequency())
