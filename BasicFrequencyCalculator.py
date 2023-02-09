import pandas as pd
class BasicFrequencyCalculator:
    def __init__(self, dataset_path) -> None:
        self.dataset_path = dataset_path
        self.frequency= {}

    def read_dataset(self):
        self.data = pd.read_csv(self.dataset_path)

    def calculate_frequency(self):
        for item in self.data['item']:
            if item in self.frequency:
                self.frequency[item] += 1
            else:
                self.frequency[item] = 1
    
    def generate_output(self):
        output_df = pd.DataFrame(columns=['item_name', 'frequency'])
        for item in self.frequency:
            output_df = output_df.append({'item_name' : item, 'frequency' : self.frequency[item]}, ignore_index=True)
        output_df.to_csv('output.csv', index=False)