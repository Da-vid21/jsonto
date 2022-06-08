import pandas as pd
import jsontocsv

output = jsontocsv.csvfile()
print(output)
# Then loading csv file
df = pd.read_csv(output)

# converting ;FRUIT_NAME' column into list
a = list(df['Sentences'])

# converting list into string and then joining it with space
b = '\n'.join(str(e) for e in a)

with open("test.txt", "w") as f:
    f.write(b)