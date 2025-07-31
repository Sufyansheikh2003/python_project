import os.path
from fileinput import filename

import pandas
from pydriller import Repository

url = input("Enter the Repository URL: ")
comittername, comitteremail, date, projectname, commitmsg = [], [], [], [], []
print(f"Fetching{url}")
for a in Repository(url).traverse_commits():
    comittername.append(a.author.name)
    comitteremail.append(a.author.email)
    date.append(a.committer_date)
    projectname.append(a.project_name)
    commitmsg.append(a.msg)
print("Fetching Complete")
github_dict = {
    "Project Name": projectname,
    "Comitter Name": comittername,
    "Comitte Email": comitteremail,
    "Date": date,
}
github_df = pandas.DataFrame(github_dict)

filename = input("Enter the filename: ")
if os.path.exists(f"{filename}.csv"):
    print(f"File {filename}.csv already exists!")
else:
    github_df.to_csv(f"{filename}.csv", index=False)
    print(f"File {filename}.csv has been created!")

