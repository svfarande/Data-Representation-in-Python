import pandas as pd
import matplotlib.pyplot as plt
%matplotlib notebook

choice = ["C/C++", "Java", "Python", "PHP", "Matlab", "Objective-C", "JavaScript", "Visual Basic", "Perl", "C#"]
data = pd.read_csv('Popularity of Programming Languages from 2004 to 2023.csv', usecols=choice+["Date"])
data["Date"] = pd.to_datetime(data["Date"])
mean_data = data.groupby(data['Date'].dt.year).mean().reset_index()
mean_data.plot(x="Date", y=mean_data.columns.to_list().remove('Date'), kind="line", figsize=(15,10))
plt.ylabel("Trends")
plt.xlabel("Year")
plt.title("Trends of Programming Languages 2004 to 2023")
sy = ['2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', 
      '2017', '2018', '2019', '2020', '2021', '2022', '2023']
plt.xticks(list(range(2004, 2024)), sy)
plt.show() 
