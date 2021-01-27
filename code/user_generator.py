import pandas as pd

users = []
for i in range(1, 2001):
    users.append(["testuser" + str(i) + "@mail.com",  "hogeuser" + str(i)])
    
df = pd.DataFrame(users ,columns=['email', 'nickname'])
df.to_csv("../csv/2000users.csv", index=False)