import pandas as pd
import requests
from bs4 import BeautifulSoup

web_url = "https://www.nueplex.com/ticket.html"
response = requests.get(web_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")


    tables = soup.find_all("table", class_="table")

    all_data = []

    for table in tables:

        headers = [th.get_text(strip=True) for th in table.find_all("th")]


        rows = table.find_all("tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            data = [td.get_text(strip=True) for td in cols]
            if data:
                all_data.append(data)


    df = pd.DataFrame(all_data, columns=headers)
    print(df)
    df.to_csv("Nueplex_Ticket_Data.csv", index=False)

else:
    print(f"Failed to fetch page. Status code: {response.status_code}")
