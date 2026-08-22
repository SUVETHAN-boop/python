import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

data = {
            "student_id":[3,4,6],
            "mark":[450,489,490],
            "attenence":[80,75,90]
}
df = pd.DataFrame(data)

sns.pairplot(df)
plt.show()

