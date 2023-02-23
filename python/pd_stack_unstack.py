import pandas as pd
import numpy as np

index = pd.MultiIndex.from_tuples([('one','a'),('one','b'),('two','a'),('two','b')])
print(index)
s=pd.Series(np.arange(1.0,5.0),index=index)
print(s)
##########3
# print(s.unstack())
s_new=s.unstack(level=0)
print(s_new)
#########
print(s_new.stack(0))
