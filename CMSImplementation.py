import csv
import pandas as pd
import random
class CountMinSketch:
    def __init__(self, N = 10000, K = 10000) -> None:
        self.N = N
        self.K = K
        self.matrix = [[0 for j in range(self.K)] for i in range(self.N)]

    def read_dataset(self):
        self.data = pd.read_csv("artificial_dataset.csv")
        for item in self.data['item']:
            self.generate_matrix.add(item)

    def generate_hash(self, item, seed):
        random.seed(seed)
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        return (a * item) + b

    def generate_matrix(self, item):
        for i in range(self.N):
            self.matrix[i][self.generate_hash(item, i)] += 1

    def get_frequency(self, item):
        mini = float('inf')
        for i in range(self.N):
            ctr = self.matrix[i][self.generate_hash(item, i)]
            mini = min(mini, ctr)
        return mini

    def generate_output(self):
        output_df = pd.DataFrame(columns=['item_name', 'frequency'])
        for item in self.data['item']:
            output_df = output_df.append({'item_name' : item, 'frequency' : self.get_frequency(item)}, ignore_index=True)
        output_df.to_csv('output.csv', index=False)
