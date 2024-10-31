import pandas as pd
import numpy as np

# importando o conjunto de dados usando dataframe
df = pd.read_csv("python-dataanalysis\agricultural-materials")

# explorando o conjunto de dados
df.sample(10)