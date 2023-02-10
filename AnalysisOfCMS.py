import pandas as pd
import re
import matplotlib.pyplot as plt
class AnalysisOfCMS:
    def __init__(self, actual_results_path, estimated_results_path) -> None:
        self.actual_results_path = actual_results_path
        self.estimated_results_path = estimated_results_path

    def read_files(self):
        self.actual_results = pd.read_csv(self.actual_results_path)
        self.estimated_results = pd.read_csv(self.estimated_results_path)

    def comparison(self):
        self.read_files()
        result_df = pd.DataFrame({'N&K' : [], 'FrequencyOfOverestimation' : [], 'ProbOfOverestimation' : []})
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
        # result_df.to_csv("test.csv", index=False)
        result_df.plot(kind='bar', x='N&K', y='FrequencyOfOverestimation')
        plt.show()

cms = AnalysisOfCMS('ActualFrequency.csv', 'EstimatedFrequency.csv')
cms.comparison()