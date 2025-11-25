import pandas as pd

df = pd.read_csv(r"C:\Users\dines\OneDrive\Documents\python\\dataset\\Sample_ Superstore.csv")
df["Ship Date"] = df["Ship Date"].astype(str).str.replace("-","/")
df["Ship Date"] = pd.to_datetime(
     df["Ship Date"],
     format="mixed",
     dayfirst=True,
     errors="coerce"
     )

df["Order Date"] = df["Order Date"].astype(str).str.replace("-","/")
df["Order Date"] = pd.to_datetime(
     df["Order Date"],
     format="mixed",
     dayfirst=True,
     errors="coerce"
     )

df["shiping days"] = df["Ship Date"] - df["Order Date"]


df=df.fillna(0)

df["Ship Mode"] = df["Ship Mode"].str.strip().str.title()

df["Country"] = df["Country"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()
df["Region"] = df["Region"].str.strip().str.title()
df["State"] = df["State"].str.strip().str.title()
df["Category"] = df["Category"].str.strip().str.title()
df["Product Name"] = df["Product Name"].str.strip().str.title()
df["Sub-Category"] = df["Sub-Category"].str.strip().str.title()
df["Segment"] = df["Segment"].str.strip().str.title()

Q1 = df["Profit"].quantile(0.25)
Q3 = df["Profit"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5*IQR
upper = Q3 + 1.5*IQR
df = df[(df["Profit"]>=lower) & (df["Profit"]<=upper)]


df["Profit Margin%"] = (df["Profit"]/df["Sales"])*100

df["Year of Order"] = df["Order Date"].dt.year
df["Month of Order"] = df["Order Date"].dt.month

df["High Discount"] = df["Discount"].apply(lambda x:1 if x > 0.3 else 0)

###high level cleaning using rapidfuzz
#correcting = {
#     
#     "United Statess":"United States"
#}
#df["Country"] = df["Country"].replace(correcting)
#print(df["Country"])

#method2
from rapidfuzz import process
def correct_spelling(x, choices):
     match = process.extractOne(x, choices)
     return match[0]   
allowedcountries = ['United States','Canada']
#unique_countries = df["Country"].unique()
df["Country"] = df["Country"].apply(lambda x:correct_spelling(x,allowedcountries) )

df.to_csv("cleaned_superstore.csv", index = False)
print(df)


