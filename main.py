import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Charger les données (remplacez le chemin par celui de votre fichier CSV)
df = pd.read_csv('/mnt/data/cosmetics.csv')

# 1. Filtrage des produits par type de peau et budget

# Fonction pour filtrer les produits selon le type de peau et le budget
def filter_products(df, skin_type, budget):
    # Filtrer par type de peau
    if skin_type == 'dry':
        filtered_df = df[df['Dry'] == 1]
    elif skin_type == 'oily':
        filtered_df = df[df['Oily'] == 1]
    elif skin_type == 'combination':
        filtered_df = df[df['Combination'] == 1]
    elif skin_type == 'sensitive':
        filtered_df = df[df['Sensitive'] == 1]
    else:
        filtered_df = df  # Si aucun type de peau spécifique n'est choisi

    # Filtrer par budget
    if budget == 'economical':
        filtered_df = filtered_df[filtered_df['Price'] < 50]
    elif budget == 'standard':
        filtered_df = filtered_df[(filtered_df['Price'] >= 50) & (filtered_df['Price'] <= 150)]
    elif budget == 'premium':
        filtered_df = filtered_df[filtered_df['Price'] > 150]

    return filtered_df