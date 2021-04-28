import pandas as pd
import numpy as np
s = pd.Series([1,2,4,4.97,8,0,3,11])
t = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
print(t)
