## Import libraries
import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

# Import url of interest
url = "https://www.towardssustainability.be/Investment-Product"

# Initialise results
result = pd.DataFrame(columns=['Name','Type','Managers'])

r = rq.get(url)
data_list = []
new_item = []

soup=BeautifulSoup(r.content, 'html.parser')
#Name of fund
td_list_name = soup('td', {'class':'views-field views-field-title active'})
# Type
td_list_type = soup('td', {'class':'views-field views-field-field-product-type views-align-left'})
# Managers
td_list_managers = soup('td', {'class':'views-field views-field-field-manager views-align-left'})

for i in range(len(td_list_managers)):
    result = result.append({'Name':td_list_name[i].a.string.strip(),
                            'Type':td_list_type[i].string.strip(),
                            'Managers':td_list_managers[i].string.strip()}, ignore_index=True)

print(result)
