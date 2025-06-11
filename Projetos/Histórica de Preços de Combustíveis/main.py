
# %%
import pandas as pd

combustiveis_2018_01_df = pd.read_csv('ca-2018-01.csv', sep=';')
display(combustiveis_2018_01_df)  # type: ignore

# %%
combustiveis_2018_01_df.info()

# %%
