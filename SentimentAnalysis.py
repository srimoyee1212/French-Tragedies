import pandas as pd
import sys
import glob
import operator
import pprint
df1=pd.read_csv('C:/Users/Mahe/Desktop/abi/FEEL.csv', sep=';')     #reads the csv file into a dataframe
columns = ['id','joy','fear','sadness','anger','surprise','disgust']
df1.drop(columns, inplace=True, axis=1)                                            #drops the columns specified in the previous line from the dataframe 
#print(df1)
positive=df1['polarity']=="positive"         #creates a constraint to get the words which have positive polarity
df1[positive]
dfp=df1[positive]                                   #creates a new dataframe from the initial dataframe using a constraint to get only the positive words
#print(dfp)
colp=['polarity']
dfp.drop(colp, inplace=True, axis=1)   #drops the polarity column from the new dataframe
#print(dfp)
negative=df1['polarity']=="negative"    #creates a constraint to get the words which have negative polarity
dfn=df1[negative]                                #creates a new dataframe from the initial dataframe using a constraint to get only the negative words
#print(dfn)
coln=['polarity']
dfn.drop(coln, inplace=True, axis=1)    #drops polarity column from new dataframe
#print(dfn)
plist = dfp["word"].tolist()                     #converts dataframe containing positive words to a list of positive words
nlist = dfn["word"].tolist()                    #converts dataframe containing negative words to a list of negative words
#pprint(plist)
#pprint(nlist)
pcount=0
ncount=0
mlist=[]                                           #creates a list to contain paths of all the files in the dataset
mlist=glob.glob('Desktop/abi/dataset1/*.txt')    #uses glob module to get the paths of all files in the same directory
list2=[]
list3=[]
for p in mlist:
        with open(p) as quotes:                 #opens the file 
        #loop till the end of each file
        for line in quotes:
            
            for word in plist:                      #checks if the word in the file is in the list of positive words                
                if word in line.split():           #splits on encountering spaces
                    pcount+=1                     #increments counter on finding a match
            for word in nlist:                    #checks if the word in the file is in the list of negative words                
                if word in line.split():
                    ncount+=1                   #increments counter on finding a match
    
        list2.append(pcount)              #creates a list to contain the number of positive words in each file
        pcount=0
        list3.append(ncount)            #creates a list to contain the number of negative words in each file
        ncount=0
        
#printing the lists
print(list2)
print(list3)

#creating a separate list to store the difference in values of list2 and list3

list5=list(map(operator.sub, list2, list3))       #subtracts values of list3 from list2 and stores in another list i.e list5
print(list5)

#creating the final list containing the sentiment of each file in the order they are stored in the directory 
#for furthur reference print the mlist and the sentiment list side by side to compare which sentiment belongs to which file

sentiment=[]                                        #creates list to record the sentiment of each file

#loop for every element of list5 i.e the difference list

for i in list5:
    if (i>0):
        sentiment.append('positive')     #if difference is positive
    elif (i<0):
        sentiment.append('negative')   #if difference is negative
    else:
        sentiment.append('cannot say')  #if difference is 0

pprint.pprint(sentiment)
pprint.pprint(mlist)   