import pandas
import requests
from bs4 import BeautifulSoup

web_url = "https://www.pchotels.com/hotel-and-resort/pearl-continental-hotel-karachi?gad_source=1&gad_campaignid=22773155038&gbraid=0AAAAADMyAoh70i4Mll24OHLJEbbblJmlG&gclid=Cj0KCQjw-ZHEBhCxARIsAGGN96KblHbv2kvJ12orwzvOkQThHmqipScmlj8VXybUV5OPYO-3H_z3hMwaAumpEALw_wcB"
response = requests.get(web_url)

data_uthao = BeautifulSoup(response.text, "html.parser")
div_lao = data_uthao.find_all("div",class_="accomodation-content-bx")
RoomName,Description = [],[]
print(response)


for lala in div_lao:
    h3kolao = lala.find_all("h3")
    p_lao = lala.find_all("p")
    for p in p_lao:
        RoomName.append(p.text)
        for p in p_lao:
            Description.append(p.text)

    Room_Data = {
        "RoomName":RoomName,
        "Description":Description,
    }

df = pandas.DataFrame(Room_Data)
print(df)
df.to_csv("Room_Data.csv", index=False)
