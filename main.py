import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

books = pd.read_csv('data/BX-Books.csv', sep=';', encoding="latin-1", on_bad_lines='skip')
print(books.shape)
