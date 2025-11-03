# loader.py
import pandas as pd

def load_spotify_dataset(path='dataset.csv'):
    df = pd.read_csv(path)
    
    # Remove linhas sem popularidade
    df = df.dropna(subset=['popularity'])
    
    dataset = []
    for _, row in df.iterrows():
        dados = {
            'track_name': row['track_name'],
            'artist_name': row['artists'],   # nome exato da coluna
            'genre': row['track_genre']
        }
        dataset.append({'popularity': int(row['popularity']), **dados})
    
    return dataset
