import plotly.figure_factory as pff
import pandas as pd
import csv 
import statistics
import random
import plotly.graph_objects as pgo

df=pd.read_csv('student_marks.csv')
data=df['Math_score'].tolist()

mean=statistics.mean(data)
stdev=statistics.stdev(data)
print(mean)
print(stdev)

# graph=pff.create_distplot([data],['Math Score'],show_hist=False)
# graph.show()

def random_set_mean(counter):
    dataset=[]

    for i in range(0,counter):
        index=random.randint(0,len(data)-1)
        value=data[index]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    return(mean)

mean_list=[]

for i in range(0,1000):
    set_of_means=random_set_mean(100)
    mean_list.append(set_of_means)

s_stdev=statistics.stdev(mean_list)
s_mean=statistics.mean(mean_list)
print(s_stdev)
print(s_mean)

first_start,first_end=mean-s_stdev,mean+s_stdev
second_start,second_end=mean-2*s_stdev,mean+2*s_stdev
third_start,third_end=mean-3*s_stdev,mean+3*s_stdev

df=pd.read_csv('data1.csv')
data=df['Math_score'].tolist()
mean1=statistics.mean(data)
print(mean1)

df=pd.read_csv('data2.csv')
data=df['Math_score'].tolist()
mean2=statistics.mean(data)
print(mean2)

df=pd.read_csv('data3.csv')
data=df['Math_score'].tolist()
mean3=statistics.mean(data)
print(mean3)


graph=pff.create_distplot([mean_list],['student_marks'],show_hist=False)
graph.add_trace(pgo.Scatter(x=[mean,mean],y=[0,0.20],mode='lines',name="Mean"))
graph.add_trace(pgo.Scatter(x=[mean1,mean1],y=[0,0.20],mode='lines',name="Mean1"))
graph.add_trace(pgo.Scatter(x=[mean2,mean2],y=[0,0.20],mode='lines',name="Mean2"))
graph.add_trace(pgo.Scatter(x=[mean3,mean3],y=[0,0.20],mode='lines',name="Mean3"))
graph.add_trace(pgo.Scatter(x=[first_start,first_start],y=[0,0.20],mode='lines',name="Mean Again"))
graph.add_trace(pgo.Scatter(x=[first_end,first_end],y=[0,0.20],mode='lines',name="Mean Again^2"))
graph.add_trace(pgo.Scatter(x=[second_start,second_start],y=[0,0.20],mode='lines',name="Mean Again^3"))
graph.add_trace(pgo.Scatter(x=[second_end,second_end],y=[0,0.20],mode='lines',name="Mean Notnotnotnot Again"))
graph.add_trace(pgo.Scatter(x=[third_start,third_start],y=[0,0.20],mode='lines',name="Mean notnotreally Again"))
graph.add_trace(pgo.Scatter(x=[third_end,third_end],y=[0,0.20],mode='lines',name="Mean lastcausethereisnothingelse"))
# graph.show()

z_score1=(mean1-mean)/s_stdev
print(z_score1)

z_score2=(mean2-mean)/s_stdev
print(z_score2)

z_score3=(mean3-mean)/s_stdev
print(z_score3)
