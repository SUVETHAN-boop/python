             #conduct sampling and create a report

import numpy as np
import pandas as pd
from scipy.stats import norm

url ="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

sample = df["Age"].sample(30,random_state=42)

mean = sample.mean()
std = sample.std()
data_len = len(sample)

z_value = norm.ppf(0.975)
margin_error = z_value * (std / np.sqrt(data_len))
ci = (mean - margin_error),(mean + margin_error)

print("sample mean : ",mean)
print("95% confidence interval : ",ci)