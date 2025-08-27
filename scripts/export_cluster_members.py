import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv('data/pokemon_stats.csv')

# Normalize type columns
for col in ['PrimaryType','SecondaryType']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().replace({'': np.nan, 'None': np.nan, 'none': np.nan, 'nan': np.nan})
        mask = df[col].notna()
        df.loc[mask, col] = df.loc[mask, col].str.title()

# Deduplicate by Name
df_clean = df.drop_duplicates(subset=['Name'], keep='first').reset_index(drop=True)

clustering_features = ['HP','Att','Def','S.Att','S.Def','Spd']
pokemon_stats = df_clean[clustering_features].copy()

# Standardize
scaler = StandardScaler()
pokemon_stats_scaled = scaler.fit_transform(pokemon_stats)

# Final KMeans (k=5)
k_final = 5
kmeans = KMeans(n_clusters=k_final, n_init=50, random_state=42)
clusters = kmeans.fit_predict(pokemon_stats_scaled)

df_clean['Cluster'] = clusters

# Create long table of Cluster -> Pokemon
rows = []
for c, names in df_clean.groupby('Cluster')['Name']:
    for name in names:
        rows.append({'Cluster': int(c), 'Pokemon': name})

out_df = pd.DataFrame(rows).sort_values(['Cluster','Pokemon']).reset_index(drop=True)

out_path = 'data/cluster_members_k5.csv'
out_df.to_csv(out_path, index=False)

print(f"Saved {out_path}; unique Pokemon: {len(df_clean)}")
for c, g in df_clean.groupby('Cluster'):
    print(f"Cluster {c}: {len(g)} Pokemon")

# Print preview
print('\nPreview (first 100 rows):')
print(out_df.head(100).to_csv(index=False))
