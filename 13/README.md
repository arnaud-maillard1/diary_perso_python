# Cours 13

# Création d'un package à publié sur PyPi

## Fichier spéciaux

- `.editorconfig` : pour définir les règles de codage
- `.gitignore` : pour ignorer les fichiers à ne pas mettre sur git
- `README.md` : pour décrire le package
- `setup.py` : fichier utiliser par pip pour qu'il installe le package
- `setup.cfg` : fichier de configuration pour le package
- `pyproject.toml` : fichier de configuration pour le package

## Commandes

- `pip install -e .` : pour installer le package en mode développement en se trouvant dans le dossier du package

Si une erreur mentionne : _LookupError: setuptools-scm was unable to detect version for /mnt/c/Users/arnau/OneDrive/Documents/HEIGVD/Semestre_6/Python/diary_perso_python/13/heigvd_

Il faut faire crée un repo git et faire une version avec un tag.

1. `git init`
2. `git add .`
3. `git commit -m "Initial commit"`
4. `git tag -a 0.0.1`
5. `git describe` -> doit fonctionner
