import sqlite3
import pandas as pd

# Créer une connexion à la base de données SQLite
conn = sqlite3.connect('mydatabase.db')

# Lire les fichiers CSV à partir du répertoire git
csv_files = ['file1.csv', 'file2.csv', 'file3.csv']
for file in csv_files:
    # Lire le fichier CSV dans un DataFrame pandas
    df = pd.read_csv(f'https://raw.githubusercontent.com/monrepo/{file}')
    # Écrire le DataFrame dans la base de données SQLite
    df.to_sql(file.replace('.csv', ''), conn, if_exists='replace', index=False)

# Effectuer des requêtes SQL sur la base de données SQLite
cursor = conn.cursor()
cursor.execute('SELECT * FROM file1')
results = cursor.fetchall()
print(results)

# Fermer la connexion à la base de données SQLite
conn.close()
