import pandas as pd

# Carga el dataset
df = pd.read_csv("training.1600000.processed.noemoticon.csv", encoding='latin-1', names=["target", "ids", "date", "flag", "user", "text"])

# Define términos de búsqueda relacionados con Obama y eventos de 2009
keywords = ["Obama", "president", "election", "White House", "healthcare", "Barack", "McCain", "Biden", "Hillary Clinton", "democrats"]

# Filtra tweets que contengan cualquiera de los términos (case-insensitive)
df_filtered = df[df['text'].str.contains('|'.join(keywords), case=False, na=False)]

# Convierte etiquetas de sentimiento (0=negativo, 4=positivo)
df_filtered = df_filtered.copy()
df_filtered.loc[:, 'sentiment'] = df_filtered['target'].map({0: 'negative', 4: 'positive'})

# Selecciona columnas relevantes
df_filtered = df_filtered[['date', 'text', 'sentiment']]

# Guarda el dataset filtrado
df_filtered.to_csv("filtered_tweets.csv", index=False)

# Imprime estadísticas
print(f"Filas filtradas: {len(df_filtered)}")
print(f"Tamaño del archivo (bytes): {df_filtered.memory_usage(deep=True).sum()}")
