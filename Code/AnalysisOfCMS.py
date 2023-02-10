import pandas as pd
import re
import matplotlib.pyplot as plt
class AnalysisOfCMS:
    def __init__(self, actual_results_path, estimated_results_path) -> None:
        self.actual_results_path = actual_results_path
        self.estimated_results_path = estimated_results_path

    # Read the resultant csv files
    def read_files(self):
        self.actual_results = pd.read_csv(self.actual_results_path)
        self.estimated_results = pd.read_csv(self.estimated_results_path)

    # Compares the estimated and actual frequencies, create plots to show the comparison and saves them as .png files
    def comparison(self):
        self.read_files()
        result_df = pd.DataFrame({'N&K' : [], 'FrequencyOfOverestimation' : [], 'ProbOfOverestimation' : []})
        # Saving the frequency and probability of overestimations to result_df
        for col in self.estimated_results.columns:
            if(col != 'item'):
                temp =  self.estimated_results[col] - self.actual_results['frequency']
                result = []
                for value in temp:
                    if value > 0:
                        result.append(1)
                    else:
                        result.append(0)
                match = re.search(r"\((.*?)\)", col)
                result_df = result_df.append({'N&K' : match.group(1), 'FrequencyOfOverestimation' : sum(result), 'ProbOfOverestimation' : (sum(result) / len(result))}, ignore_index=True)
        result_df.to_csv("Comparison.csv", index=False) # Saving the dataframe to .csv file
        
        # Plotting the graph for frequency of overestimation
        x = result_df['N&K']
        y = result_df['FrequencyOfOverestimation']
        plt.bar(x, y)
        plt.title('Comparison Between various trade-offs between N and K')
        plt.xlabel('Values of N and K')
        plt.ylabel('Frequency Of Overestimation')
        # plt.show()
        plt.savefig('frequency.png') # Saving the graph as .png file

        # Plotting the graph for probability of overestimation
        y = result_df['ProbOfOverestimation']
        plt.bar(x, y)
        plt.title('Comparison Between various trade-offs between N and K for Real World Dataset')
        plt.xlabel('Values of N and K')
        plt.ylabel('Probability of Overestimation')
        # plt.show() 
        plt.savefig('probability.png') # Saving the graph as .png file

cms = AnalysisOfCMS('ActualFrequency.csv', 'EstimatedFrequency.csv')
cms.comparison()