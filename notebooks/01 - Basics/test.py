with open('compounds.txt', 'w') as file:
    #suggest a list of compounds
    compounds = ['water', 'ammonia', 'methane', 'hydrogen sulfide', 'carbon dioxide']
    #write the list to the file each compound a new line
    print('\n'.join(compounds))
    file.write('\n'.join(compounds))

with open('compounds.txt', 'r') as file:
    #read the file lines without \n
    lines = file.read().splitlines()
    for line in reversed(lines):
        print(line)
    #lines = file.readlines()
    print(lines)
#%%
# Read the ESOL dataset into a DataFrame
import pandas as pd
df = pd.read_csv('data/delaney-processed.csv')


# Inspect the first 5 rows of the DataFrame
head = df.head()

