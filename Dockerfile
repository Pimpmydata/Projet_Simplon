# Utiliser l'image nouchka/sqlite3:latest comme base
FROM nouchka/sqlite3:latest

# Installer Python et git
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv git

# Créer un répertoire pour l'environnement virtuel
RUN mkdir -p /venv

# Créer l'environnement virtuel
RUN python3 -m venv /venv

# Activer l'environnement virtuel
ENV PATH="/venv/bin:$PATH"

# Cloner le dépôt Git (uniquement la branche data)
RUN git clone -b data https://github.com/Pimpmydata/Projet_Simplon.git /data

# Copier les fichiers CSV dans le conteneur
COPY ./data/magasins.csv /data/magasins.csv
COPY ./data/produits.csv /data/produits.csv
COPY ./data/ventes.csv /data/ventes.csv


# Installer les bibliothèques Python à partir de requirements.txt
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Copier le script Python pour créer les tables dans le conteneur
COPY ./create_tables.py /create_tables.py

# Créer la base de données SQLite
RUN python3 /create_tables.py

# Exposer les ports pour se connecter à la base de données SQLite
EXPOSE 8080

# Définir le point d'entrée du conteneur
ENTRYPOINT ["python3"]
