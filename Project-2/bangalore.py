from numpy.lib.function_base import rot90
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('D:\Projects\CodingNinjaproject1\startup_funding.csv',encoding='utf-8')
d1=df[['CityLocation']]
d1.dropna(inplace=True)
d=d1
a1=d[(d['CityLocation'].str.contains('Delhi'))|(d['CityLocation'].str.contains('delhi'))]
a3=(d[d['CityLocation'].str.contains('Noida')])
a4=(d[d['CityLocation'].str.contains('Gurgaon')])
BOM=(d[d['CityLocation'].str.contains('Mumbai')])
NCR=pd.concat([a1,a3,a4], ignore_index=True)
BLR= d[(d['CityLocation'].str.contains('Bangalore'))|(d['CityLocation'].str.contains('bangalore'))]
print('NCR =',end=' ')
print(NCR['CityLocation'].size)
print('Bangalore =',end=' ')
print(BLR['CityLocation'].size)
print('Mumbai =',end=' ')
print(BOM['CityLocation'].size)

# print(NCR.size)
# colors=['Red','Green','Blue']
# a=['NCR','Bangalore','Mumbai']
# b=[ NCR['CityLocation'].size,BLR['CityLocation'].size,BOM['CityLocation'].size]
# plt.bar(a,b,width=0.5,color=colors)
# plt.title('City with most funding')
# plt.xlabel('Cities')
# plt.ylabel('Total Startups')
# plt.show()


####################################################################################################

# Question 2
d=df[['CityLocation','InvestorsName','StartupName','InvestmentType']]
d.dropna(inplace=True)
a1=d[(d['CityLocation'].str.contains('Delhi'))|(d['CityLocation'].str.contains('delhi'))]
a3=(d[d['CityLocation'].str.contains('Noida')])
a4=(d[d['CityLocation'].str.contains('Gurgaon')])
NCR=pd.concat([a1,a3,a4], ignore_index=True)
print(NCR)
# print(NCR.size)


print(NCR['InvestmentType'].unique())
NCR['StartupName'].replace('Oyorooms','Oyo',inplace = True)
NCR['StartupName'].replace('OyoRooms','Oyo',inplace = True)
NCR['StartupName'].replace('Oyo Rooms','Oyo',inplace = True)
NCR['StartupName'].replace('OYO Rooms','Oyo',inplace = True)
NCR['StartupName'].replace('Olacabs','Ola',inplace = True)
NCR['StartupName'].replace('Ola Cabs','Ola',inplace = True)
NCR['StartupName'].replace('Olacabs','Ola',inplace = True)
NCR['StartupName'].replace('Flipkart.com','Flipkart',inplace = True)
NCR['StartupName'].replace('Paytm Marketplace','Paytm',inplace = True)
NCR = NCR[NCR.InvestorsName != 'Undisclosed Investors']
NCR = NCR[NCR.InvestorsName != 'Undisclosed investors']
NCR = NCR[NCR.InvestorsName != 'undisclosed investors']
NCR = NCR[NCR.InvestorsName != 'undisclosed investor']
NCR = NCR[NCR.InvestorsName != 'Undisclosed investor']

a=NCR['InvestorsName']
a=np.array(a)
l=[]
l2=np.array(l)
for i in range(0,len(a)):
    e=str(a[i])
    l1=e.strip().split(',')
    l2=np.append(l2,l1)
# l2=l2[l2!='Undisclosed']
# l2=l2[l2!='Undisclosed Investors']
# l2=l2[l2!='Undisclosed investors']
l2=l2[l2!='']
d1={}
for i in range(0,len(l2)):
    l2[i]=str(l2[i]).strip()
l2=pd.DataFrame(l2, columns=['Col'])
a=l2.value_counts()[0:5]
print('')
print('Part2')
print('')
print(a)
count=a.index
val=a.values
x=[]
y=[]
for i in range(0,len(val)):
    stri=str(count[i])
    stri=stri.removeprefix("('").removesuffix("',)")
    x.append(stri)
    y.append(val[i])

# #print(x)
# color=['Red','Green','Blue','Orange','Cyan']
# plt.bar(x,y,width=0.5,color=color)
# plt.xticks(rotation=40)
# plt.xlabel('Investors')
# plt.ylabel('No. of Investments')
# plt.title('Top investors in NCR')
# plt.show()

#######################################################################################
#Question 3

investor_name = []
startup_name = []

for index,row in NCR.iterrows():
    s = row['InvestorsName']
    v = row['StartupName']
    
    i = str(s)
    l = i.split(',')
    
    for j in l:
        if j != '':
            j = j.strip()
            investor_name.append(j)
            startup_name.append(v)

df1 = pd.DataFrame({'InvestorsName' : investor_name,'StartupName' : startup_name})
df1 = df1.groupby('InvestorsName')['StartupName'].nunique()
df1 = df1.sort_values(ascending = False)
print('')
print('Part 3')
print('')
df1 = df1.head(5)
name = []
count = []
for i in range(5):
    print(df1.index[i],df1.values[i])
    name.append(df1.index[i])
    count.append(df1.values[i])
#print(NCR) 
# color=['Red','Green','Blue','Orange','Cyan']
# plt.bar(name,count,width=0.5,color=color)
# plt.xticks(rotation=40)
# plt.xlabel('Top 5 Investors')
# plt.ylabel('No_Of_Investments')
# plt.title('Top Investors')
# plt.show()


###############################################################################

# Question 4 
#print(NCR)
print('')
print('Part 4')
print('')
df=NCR[NCR['InvestmentType']=='Seed Funding']

investor_name = []
startup_name = []

for index,row in df.iterrows():
    s = row['InvestorsName']
    v = row['StartupName']
    
    i = str(s)
    l = i.split(',')
    
    for j in l:
        if j != '':
            j = j.strip()
            investor_name.append(j)
            startup_name.append(v)

df1 = pd.DataFrame({'InvestorsName' : investor_name,'StartupName' : startup_name})
df1 = df1.groupby('InvestorsName')['StartupName'].nunique()
df1 = df1.sort_values(ascending = False)
df1 = df1.head(5)
name = []
count = []
for i in range(5):
    print(df1.index[i],df1.values[i])
    name.append(df1.index[i])
    count.append(df1.values[i])
  
# color=['Red','Green','Blue','Orange','Cyan']  
# plt.bar(name,count,width=0.5,color=color)
# plt.xticks(rotation=40)
# plt.xlabel('Top 5 Investors')
# plt.ylabel('No_Of_Investment')
# plt.title('Top Investors')
# plt.show()

##################################################################################################
#Question 5
print('')
print("Part5")
print('')
df=NCR[NCR['InvestmentType']=='Private Equity']

investor_name = []
startup_name = []

for index,row in df.iterrows():
    s = row['InvestorsName']
    v = row['StartupName']
    
    i = str(s)
    l = i.split(',')
    
    for j in l:
        if j != '':
            j = j.strip()
            investor_name.append(j)
            startup_name.append(v)

df1 = pd.DataFrame({'InvestorsName' : investor_name,'StartupName' : startup_name})
df1 = df1.groupby('InvestorsName')['StartupName'].nunique()
df1 = df1.sort_values(ascending = False)
df1 = df1.head(5)
name = []
count = []
for i in range(5):
    print(df1.index[i],df1.values[i])
    name.append(df1.index[i])
    count.append(df1.values[i])
# color=['Red','Green','Blue','Orange','Cyan']
# plt.bar(name,count,width=0.5,color=color)
# plt.xticks(rotation=40)
# plt.xlabel('Top 5 Investors')
# plt.ylabel('No_Of_Investment')
# plt.title('Top Investors')
# plt.show()
