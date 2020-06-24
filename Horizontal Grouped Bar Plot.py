import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plt.xkcd()
plt.style.use("fivethirtyeight")
df = pd.read_csv("starbucks_final.csv")

ind = np.arange(len(df))
width = 0.25

fig, ax = plt.subplots()
ax.barh(ind, df["Fat"], width, label='Fat')
ax.barh(ind + width,  df["Carb"], width, label='Carb')
ax.barh(ind + width * 2, df["Protein"], width, label='Fiber')

ax.set(yticks=ind + width,
       yticklabels=df["Name"], ylim=[2 * width - 1, len(df)])
ax.legend()
plt.grid(False)
plt.tight_layout()
plt.show()
