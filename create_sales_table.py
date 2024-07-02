import csv
import sqlite3

# Connecter à la base de données SQLite
conn = sqlite3.connect('/data/database.db')
c = conn.cursor()

# Créer la table ventes à partir du fichier CSV
with open('/data/ventes.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    c.execute('CREATE TABLE IF NOT EXISTS ventes ({})'.format(', '.join(header)))
    for row in reader:
        c.execute('INSERT OR IGNORE INTO ventes VALUES ({})'.format(', '.join('?' for _ in row)), row)
        # Si la valeur existe déjà, ignore l'instrustion

# Valider les modifications
conn.commit()

# Fermer la connexion à la base de données
conn.close()
