import pandas as pd

data = {
    "id":[1,2,3,3,1],
    "score":[80,84,93,90,55],
     "mark":[37,58,69,50,80]
}

df = pd.DataFrame(data)

grouped = df.groupby("id").mean()

print(grouped)

state =df.groupby("id").agg({"score":["mean","max","min"],"mark":["mean","max","min"]})
print(state)