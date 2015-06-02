import pandas as pd
head_names = ['title', 'year', 'released_date', 'language', 'runtime',
              'writer', 'director', 'imdb_rating', 'family_rating',
              'imdb_ID', 'imdb_votes', 'genre', 'awards']
df = pd.read_csv('merged.csv', names=head_names)
print df.head()