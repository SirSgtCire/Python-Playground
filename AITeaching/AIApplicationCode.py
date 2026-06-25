# Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd

# PART 1: Extract the data from the Google document
input_file = 'https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub'

response = requests.get(input_file)
# print(response)

soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
# print(table)

rows = table.find_all('tr')
# print(rows)

header = [cell.get_text(strip=True) for cell in rows[0].find_all('td')]
# print(header)

data = []
for row in rows[1:]:
    cells = row.find_all('td')
    row_data = {header[i]: cells[i].get_text(strip=True) for i in range(len(cells))}
    data.append(row_data)
# print(data)

# PART 2: Construct visual matrix using data
df = pd.DataFrame(data)
df[header[0]] = df[header[0]].astype(int)
df[header[2]] = df[header[2]].astype(int)
# print(df.to_string())
# print(df.to_markdown(index=False))

xcoordinatelist = df[header[0]].tolist()
ycoordinatelist = df[header[2]].tolist()
# print(max(xcoordinatelist))
# print(max(ycoordinatelist))

max_x = max(xcoordinatelist) + 1
max_y = max(ycoordinatelist) + 1
grid_df = pd.DataFrame('.', index=range(max_x), columns=range(max_y))
for _, nrow in df.iterrows():
    grid_df.iat[nrow['x-coordinate'], nrow['y-coordinate']] = nrow['Character']
print(grid_df.to_string())

# END