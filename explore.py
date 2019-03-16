import pandas as pd

reviews = pd.read_csv('data/amazon_alexa.tsv', sep='\t')

print(reviews.head)
print(reviews.describe())

#print(reviews.loc[reviews['verified_reviews'].str.contains('privacy|Privacy')])

reviews['verified_reviews'] = reviews['verified_reviews'].str.lower()

df = reviews.loc[reviews['verified_reviews'].str.contains('eavesdrop')]

for row in df.iterrows():
    print(row[1][0], row[1][1], row[1][2], row[1]['verified_reviews'].replace('eavesdrop', '***EAVESDROP***'))


df = reviews.loc[reviews['verified_reviews'].str.contains('privacy|Privacy|PRIVACY')]

for row in df.iterrows():
    print(row[1][0], row[1][1], row[1][2], row[1][4], row[1]['verified_reviews'].lower().replace('privacy', '***PRIVACY***'))


df = reviews.loc[reviews['verified_reviews'].str.contains('interrupt')]

for row in df.iterrows():
    print(row[1][0], row[1][1], row[1][2], row[1][4], row[1]['verified_reviews'].lower().replace('interrupt', '***INTERRUPT***'))

df = reviews.loc[reviews['verified_reviews'].str.contains('surveillance|collection|identification|violation|leak')]

print('OTHER REVIEWS')
for row in df.iterrows():
    print(row[1][0], row[1][1], row[1][2], row[1][4], row[1]['verified_reviews'])
