import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
empdata=pd.read_csv('pythonproject.csv')
empdata['Height']= np.random.randint(150,180,size=len(empdata))
print(empdata)
print(empdata.isnull().sum())
print(empdata.duplicated().sum())
empdata['College']=empdata['College'].fillna(empdata['College'].mode()[0])
empdata['Salary']=empdata['Salary'].fillna(empdata['Salary'].median())
print("After Data is processed"+str(empdata.isnull().sum()))
print(empdata.info())
print(empdata.head())


#############Question 1 perecntage
teamdis = empdata['Team'].value_counts()
teamper=(teamdis/len(empdata))*100
print("Team Count"+str(teamper))

################Position
position=empdata['Position'].value_counts()
print(position)

#######################age group
agepre=empdata['Age'].value_counts()
disagepre=empdata['Age'].unique()
print("MOst 5 predominnat age groups are"+str(agepre.head()))


###################### team and Position
team_salary = empdata.groupby('Team')['Salary'].sum().sort_values(ascending=True)
team_name = team_salary.index
print(team_salary)

#############################Correlation between age and salary
corre = empdata[['Age','Salary']].corr()
print(corre)
sns.heatmap(corre)
plt.show()

################################Visulaisation
#########################linechart

# # Question1
plt.plot(teamdis,marker='o')
plt.title('Employee Distribution by Team')
plt.xlabel('Team')
plt.ylabel('Number of Employees')
plt.xticks(rotation=90) 
plt.show() 

##question2
plt.plot(position,marker='o')
plt.title('Position by company name')
plt.xlabel('Postion')
plt.ylabel('Number of Positions')
plt.xticks(rotation=90) 
plt.show() 


##question3
plt.bar(disagepre,agepre)
plt.title('Divided by Age Group')
plt.xlabel('Age')
plt.ylabel('Age Range')
plt.xticks(rotation=90) 
plt.show() 

##question4
plt.bar(team_name,team_salary)
plt.title('Salary')
plt.xlabel('Team')
plt.ylabel('Team Names')
plt.xticks(rotation=90) 
plt.show() 

