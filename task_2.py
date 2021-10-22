import random
import pandas as pd

genres = ['hip', 'hop', 'hip-hop', 'rock', 'electro']
df = pd.DataFrame({'genre': [random.choice(genres) for _ in range(10)]})
print(df)
print(df.replace({'genre': {'hip': 'hip-hop', 'hop': 'hip-hop'}}))
