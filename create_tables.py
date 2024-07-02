import csv
import sqlite3

# Connecter à la base de données SQLite
conn = sqlite3.connect('/data/database.db')
c = conn.cursor()

# Créer la table magasins à partir du fichier CSV
with open('/data/magasins.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    c.execute('CREATE TABLE magasins ({})'.format(', '.join(header)))
    for row in reader:
        c.execute('INSERT INTO magasins VALUES ({})'.format(', '.join('?' for _ in row)), row)

# Créer la table produits à partir du fichier CSV
with open('/data/produits.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    c.execute('CREATE TABLE produits ({})'.format(', '.join(header)))
    for row in reader:
        c.execute('INSERT INTO produits VALUES ({})'.format(', '.join('?' for _ in row)), row)

# Commiter les changements et fermer la connexion
conn.commit()
conn.close()

