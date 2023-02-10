import pandas as pd
class BasicFrequencyCalculator:
    def __init__(self, dataset_path) -> None:
        self.dataset_path = dataset_path
        self.frequency= {}

    # function to read the dataset from a csv file
    def read_dataset(self):
        self.data = pd.read_csv(self.dataset_path)

    # function to calculate frequency of items in the data
    def calculate_frequency(self):
        for item in self.data['item']:
            if item in self.frequency:
                self.frequency[item] += 1
            else:
                self.frequency[item] = 1
    
    # function to generate the output (frequency) and saving it as a csv file
    def generate_output(self):
        self.read_dataset()
        self.calculate_frequency()
        output_df = pd.DataFrame(columns=['item', 'frequency'])
        for item in self.frequency:
            output_df = output_df.append({'item' : item, 'frequency' : self.frequency[item]}, ignore_index=True)
        output_df.to_csv('ActualFrequency.csv', index=False)

calculator = BasicFrequencyCalculator("Dataset.csv")
calculator.generate_output()