# Scavenger Hunt:
import pandas

# Open the file and convert directly to a list
csv_url = "https://raw.githubusercontent.com/fivethirtyeight/data/90a4272cbace9a9dbbc2d004d82de9ea5bf9eb61/congress-age/congress-terms.csv"

# Read the CSV directly from the URL into a DataFrame
df = pandas.read_csv(csv_url)

# Convert the DataFrame rows into a list of dictionaries
list_of_dicts = df.to_dict(orient="records")

# Preview the result
print(list_of_dicts)

# Question 1: What was the average age of the 80th and 113th congress?

# Question 2: Which congress had the youngest and oldest average age?