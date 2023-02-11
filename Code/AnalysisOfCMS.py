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
                # For number of times frequency was overestimated
                deviations =  self.estimated_results[col] - self.actual_results['frequency']
                frequency = 0
                for value in deviations:
                    if value > 0:
                        frequency += 1

                # Plotting the deviations
                # self.plot_deviation(self.estimated_results['item'], deviations)

                # For probability of deviation/overestimation being more than 2S/K
                S = len(self.estimated_results[col])
                p = r"frequency\(N\d*K(\d*)" 
                K = int(re.findall(p,col)[0]) 
                prob = 0
                upper_bound = (2*S)/K
                for i in deviations:
                    if(i >= upper_bound):
                        prob += 1
                
                match = re.search(r"\((.*?)\)", col)
                result_df = result_df.append({'N&K' : match.group(1), 'FrequencyOfOverestimation' : frequency, 'ProbOfOverestimation' : (prob / S)}, ignore_index=True)
        result_df.to_csv("Comparison.csv", index=False) # Saving the dataframe to .csv file
        
        # Plotting the graph for frequency of overestimation
        x = result_df['N&K']
        y = result_df['FrequencyOfOverestimation']
        plt.bar(x, y)
        plt.title('Comparison Between various trade-offs between N and K')
        plt.xlabel('Values of N and K')
        plt.ylabel('Number of times Frequency was Overestimated')
        # plt.show()
        plt.savefig('frequency.png') # Saving the graph as .png file

        # Plotting the graph for probability of overestimation
        y = result_df['ProbOfOverestimation']
        plt.bar(x, y)
        plt.title('Comparison Between various trade-offs between N and K for Artificial Dataset')
        plt.xlabel('Values of N and K')
        plt.ylabel('Probability of Overestimation')
        # plt.show() 
        plt.savefig('probability.png') # Saving the graph as .png file

    def plot_deviation(self, item, deviations):
        deviation = pd.DataFrame({'item' : item, 'deviation' : deviations})
        
        # Plot graph of top 10 deviations
        deviation.sort_values(by='deviation', ascending=False, inplace=True)
        top_10 = deviation.head(10)
        # Plot a bar graph
        x = top_10['item']
        y = top_10['deviation']
        plt.bar(x, y)
        plt.title('Top 10 Deviations')
        plt.xlabel('Items')
        plt.ylabel('Deviations')
        # plt.show()
        plt.savefig('./top10deviations.png') # Saving the graph as .png file

        return deviation

cms = AnalysisOfCMS('./ArtificialDatasetResults/ActualFrequency(ArtificialDataset).csv', './ArtificialDatasetResults/EstimatedFrequency(ArtificialDataset).csv')
cms.comparison()