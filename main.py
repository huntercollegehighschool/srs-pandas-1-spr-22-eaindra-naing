"""
We'll be using the pandas (short for panels of data) module to analyze a large dataset.
"""

"""
1. The conventional way to import the pandas module is below. Note that the "as pd" part is optional (but widely used).
import pandas as pd
"""
import pandas as pd

"""
2. This folder contains a large .csv (spreadsheet) file named ign.csv. Import the data stored in the csv as a dataframe to Python and store it in a variable. Try printing the data.
pd.read_csv('<filename/url>')
"""
data = pd.read_csv('ign.csv')
#print (data)

"""
3. When you try to view the data on the console, you should notice that the row index appears twice. That's because if not specified, pandas will create it's own indices. In fact, when you look at the data, because it's so large, you can't even see the title of the game.

Change the dataframe so that the index are not integers starting from zero, but instead the title of the game. You'll have to go to the .csv file to find in which column the game titles are.
pd.read_csv('<filename/url>', index_col = <column number>)
"""
specdata = pd.read_csv ('ign.csv', index_col = 2)
print (specdata)

"""
4. Use <dataframe>.index and print the result to see a list of indices/row names. (Note: the console will not print all of them)
"""
print (specdata.index)

"""
5. Use <dataframe>.columns and print the result to see a list of column names.
"""
print (specdata.columns)
"""
6. In a pandas dataframe, columns are indexed by column name. For example, reviews['score_phrase'] returns a dataframe that contains only the index (the game title) and the score phrase given to that game.

Create a dataframe that only contains the score for each game. You can save it in a new dataframe variable, but you don't have to. Print that new dataframe.
"""
score = pd.read_csv('ign.csv',index_col = 2)
#print (score)

#specdata.reviews['score_phrase']
"""
7. Use the following functions to find and print the indicated values based off score. Use the dataframe you created in #6.
<dataframe>.max()
<dataframe>.min()
<dataframe>.mean()
<dataframe>.median()
<dataframe>.std()  # standard deviation
"""
print (score["score"].max())
print (score["score"].min())
print (score["score"].mean())
print (score["score"].median())
print (score["score"].std())
"""
8. pandas has a function that returns a series indicating how many of each value is in a dataframe (<dataframe>.value_counts()). Use that function to find the counts in the platform, score, and release_month columns, and print the results. You will want to create 3 new dataframes that you can use value_counts() on.
"""
platform = specdata["platform"]
print (platform.value_counts())
score = specdata["score"]
print (score.value_counts())
release_month = specdata["release_month"]
print (release_month.value_counts())
"""
9. pandas supports Boolean indexing. For example, reviews[reviews['score'] < 1] would return a dataframe containing games that got a score below a 1.

Create 2 new dataframes, one with only games that got scores below 2, and one with only games that got scores of 10. Print both dataframes.
"""
loser = specdata[specdata['score'] < 2]
winner = specdata[specdata['score'] == 10]
print (loser)
print (winner)
"""
10. Save both the new dataframes you created in #9 to a csv file (it will make it much nicer to look at). Name the files 'trash.csv' and 'perfect.csv'
<dataframe>.to_csv('<filename>')
"""
loser.to_csv('trash.csv')
winner.to_csv('perfect.csv')
