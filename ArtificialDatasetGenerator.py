import pandas as pd
import random
import string
import csv

class DatasetCreater:
    def __init__(self, length) -> None:
        self.length = length
        
    def create_numerical_dataset(self):
        frequncy = random.randint(0, 100)
        stream = []
        for i in range(self.length//frequncy):
            for j in range(frequncy):
                stream.append(i)
        if(len(stream) < self.length):
            for i in range(len(stream), self.length):
                stream.append(random.randint(0, 100))
        random.shuffle(stream)
        self.write_to_csv(stream)  

    def create_ascii_dataset(self):
        stream = []
        alphabet = string.ascii_lowercase 
        for i in range(self.length):
            f = random.randint(0, len(alphabet)-1)
            stream.append(alphabet[f])
        random.shuffle(stream)
        self.write_to_csv(stream) 

    def write_to_csv(self, stream):
        output_df = pd.DataFrame(columns=['item_name'])
        for item in stream:
            output_df = output_df.append({'item_name' : item}, ignore_index=True)
        output_df.to_csv('output.csv', index=False)

creater = DatasetCreater(1000)
creater.create_ascii_dataset()