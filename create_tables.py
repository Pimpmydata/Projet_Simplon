import csv
import sqlite3

# Connecter à la base de données SQLite
conn = sqlite3.connect('/data/database.db')
c = conn.cursor()

# Créer la table magasins à partir du fichier CSV
with open('/data/magasins.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    columns = ', '.join([col.replace('<', '_').replace('>', '_').replace('"', '_').replace("'", '_') for col in header])
    c.execute('CREATE TABLE magasins (id_magasin INTEGER PRIMARY KEY, ville TEXT, nb_salaries INT)')
    # Ignorer la première ligne du fichier CSV
    next(reader)
    for row in reader:
        # Vérifier que le nombre de valeurs correspond au nombre de colonnes
        if len(row) == len(header):
            c.execute('INSERT INTO magasins VALUES ({})'.format(', '.join('?' for _ in row)), row)
        else:
            print(f"Erreur : la ligne {reader.line_num} du fichier magasins.csv contient {len(row)} valeurs au lieu de {len(header)}")

# Créer la table produits à partir du fichier CSV
with open('/data/produits.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    columns = ', '.join([col.replace('<', '_').replace('>', '_').replace('"', '_').replace("'", '_') for col in header])
    c.execute('CREATE TABLE produits (nom VARCHAR(50),id_produit VARCHAR(6) PRIMARY KEY, prix FLOAT, stock INT)')
    for row in reader:
       c.execute('INSERT INTO produits (nom, id_produit, prix, stock) VALUES ({})'.format(', '.join('?' for _ in row)), row)


# Commiter les changements et fermer la connexion
conn.commit()
conn.close()
