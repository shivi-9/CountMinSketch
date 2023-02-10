import pandas as pd
import random
import string

class DatasetCreater:
    # Initialize the length of the stream to be generated
    def __init__(self, length) -> None:
        self.length = length
        
    # Create a numerical dataset with certain frequency distribution
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

    # Create a dataset of ascii characters
    def create_ascii_dataset(self):
        stream = []
        alphabet = string.ascii_lowercase 
        for i in range(self.length):
            f = random.randint(0, len(alphabet)-1)
            stream.append(alphabet[f])
        random.shuffle(stream)
        self.write_to_csv(stream) 

    # Write the generated stream to a csv file
    def write_to_csv(self, stream):
        output_df = pd.DataFrame(columns=['item'])
        for item in stream:
            output_df = output_df.append({'item' : item}, ignore_index=True)
        output_df.to_csv('Dataset.csv', index=False)

creater = DatasetCreater(10000)
creater.create_ascii_dataset()