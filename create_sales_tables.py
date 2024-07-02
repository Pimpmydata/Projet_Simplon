import csv
import sqlite3

# Connecter à la base de données SQLite
conn = sqlite3.connect('/data/database.db')
c = conn.cursor()

# Créer la table ventes à partir du fichier CSV
with open('/data/ventes.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    c.execute('CREATE TABLE ventes ({})'.format(', '.join(header)))
    for row in reader:
        c.execute('INSERT INTO ventes VALUES ({})'.format(', '.join('?' for _ in row)), row)