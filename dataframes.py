import pandas as pa
Rishta_Profile = {
    "name": ["Zubair", "Hamza", "Ali", "Hania", "Kinza" ],
    "gender": ["Male", "Male", "Male", "Female", "Female"],
    "preferred_caste": ["Mughal", "Syed", "Shia", "Sheikh", "Qureshi"],
    "preferred_area" : ["Nazimabad", "Surjani", "Hayderabad", "Naya Nazimabad", "DHA"],
    "profession" : ["Software Engineer", "Digital Marketing", "Graphic Designer", "House Wife", "HR"],
    "no_of_siblings" : [1,3,4,5,2]
}


df_profile = pa.DataFrame(Rishta_Profile)
df_profile["age"] = [21, 50, 23, 40, 30]
print(df_profile[df_profile["age"] == "Pathan"])
print(df_profile[df_profile["no_of_siblings"] > 2])
print(df_profile[df_profile["preferred_area"] == "DHA"])
print(df_profile[(df_profile["gender"] == "Female") & (df_profile["preferred_area"] == "Nazimabad")])
df_profile["merital_status"] = ["Single", "Divorce", "Single", "Divorce", "widower"]
df_profile["nationality"] = "Pakistani"

del df_profile["profession"]
print(df_profile)



