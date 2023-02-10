import csv
import pandas as pd
import random
import math
import os
class CountMinSketch:
    # Initialize the object with the dataset path, result path, epsilon and delta values
    def __init__(self, dataset_path, result_path, epsilon = 0.01, delta = 0.01) -> None:
        self.dataset_path = dataset_path
        self.result_path = result_path
        self.K = math.ceil(2/epsilon)
        self.N = math.ceil(math.log(1 / delta))
        self.matrix = [[0 for j in range(self.K)] for i in range(self.N)]

    # Read the dataset from the file 
    def read_dataset(self):
        self.data = pd.read_csv(self.dataset_path)

    # Generate hash values using the item, seed values
    def generate_hash(self, item, seed):
        random.seed(seed)
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        return (((a * hash(item)) + b) % self.K)

    # Generate the matrix with frequency count of the items
    def generate_matrix(self, item):
        for i in range(self.N):
            self.matrix[i][self.generate_hash(item, i)] += 1

    # Get the frequency of the item from the matrix
    def get_frequency(self, item):
        mini = float('inf') # Set minimum value to positive infinity
        for i in range(self.N):
            ctr = self.matrix[i][self.generate_hash(item, i)]   # Get the count from the matrix
            mini = min(mini, ctr) # Get the minimum count
        return mini
    
    # Add a column to the existing result dataframe
    def add_column(self, output_df, column_name):
        output = []
        temp = []
        for item in self.data['item']:
            if(item not in temp):
                temp.append(item)
                output.append(self.get_frequency(item))
        output_df[column_name] = output
        return output_df

    # Update the result dataframe with the new results
    def update_df(self, output_df, column_name):
        for i in self.data['item']:
            if(i not in output_df['item'].values):
                output_df = output_df.append({'item' : i, column_name: self.get_frequency(i)}, ignore_index=True)
        return output_df

    # Driver function: reads the data set performs CMS and then writes the result into a csv file
    def generate_output(self):
        self.read_dataset()
        for item in self.data['item']: # Loop through each item in the dataset
            self.generate_matrix(item) # Generate the matrix
        column_name = "frequency(N" + str(self.N) + "K" + str(self.K) + ")" # Unique name for each column
        if os.path.exists(self.result_path):
            output_df = pd.read_csv(self.result_path)
            output_df = self.add_column(output_df, column_name)
        else:
            output_df = pd.DataFrame(columns=['item', column_name])
            output_df = self.update_df(output_df, column_name)
        # print(output_df)
        output_df.to_csv(self.result_path, index=False)

cms = CountMinSketch("Dataset.csv", "EstimatedFrequency.csv")
cms.generate_output()