import pandas as pd
df = pd.read_csv('d:\\04_python\\12_csv\\car-price.csv')
d_frame = df.columns
d_index = df.index
print(d_index)
print('---------------')
print(d_frame)
print(df.head())
print('---------------')
print(df.iloc[0,0])
print(df.shape)
i = 0
j = 0
for j in range(205):
    for i in range(26):
        aa = df.iloc[j,i]
        if aa == '?':
            df.iloc[j,i] = ""
        i += 1
    j += j
df.to_csv('d:\\04_python\\12_csv\\car_pr.csv')
