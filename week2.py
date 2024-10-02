import numpy as np
import pandas as pd
import os

database = pd.read_csv("PerovskiteML_project/Data/Perovskite_database_content_all_data.csv", low_memory=False)
print(database.columns)