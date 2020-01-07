import pandas as pd
import glob
import re

files = [f for f in glob.glob("*.csv", recursive=True)]
colnames=['id', 'text', 'time']
data=""
for i in files:
    user1 = pd.read_csv(i, names=colnames, header=None)
    t=list(user1.text)
    g=[i.replace('.csv','')]*len(t)
    data+='\n'.join([str(k)+"|"+str(j) for k,j in list(zip(t,g))])+'\n'

with open('data.set','w',encoding='utf-8') as f:
    f.write(data)
 
with open('data-nottag.set','w',encoding='utf-8') as f:
    f.write(re.sub('\[.*?]', '',data))