import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6,4), index=list('abcdef'), columns=list('ABCD'))
print(df)