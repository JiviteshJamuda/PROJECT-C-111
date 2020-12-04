import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

#Change the School data here
df = pd.read_csv("medium_data.csv")
data = df["claps"].tolist()

rng = []
for i in range(0,50):
    rng.append(random.randint(0,1000))


def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def plot_graph(mean_list):
    data_frame = mean_list

    std_deviation = statistics.stdev(mean_list)
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution:- ",mean)
    print("Standard deviation of sampling distribution:- ", std_deviation)

    first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
    second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
    third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
    print("std1",first_std_deviation_start, first_std_deviation_end)
    print("std2",second_std_deviation_start, second_std_deviation_end)
    print("std3",third_std_deviation_start,third_std_deviation_end)

    new_sampling_mean = statistics.mean(rng)
    print("mean of new sampling distribution:- ",new_sampling_mean)

    graph = ff.create_distplot([data_frame], ["temp"], show_hist=False)
    graph.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
    graph.add_trace(go.Scatter(x=[new_sampling_mean, new_sampling_mean], y=[0, 0.17], mode="lines", name="MEAN OF NEW SAMPLING DISTRIBUTION"))
    graph.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
    graph.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
    graph.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
    graph.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
    graph.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
    graph.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
    graph.show()

    z_score = (new_sampling_mean - mean)/std_deviation
    print("The z score is = ",z_score)


# Function to get the mean of 100 data sets
def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    plot_graph(mean_list)
    
setup()