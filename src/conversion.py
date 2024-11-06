import os
import gzip

def convert_to_tcx(dossier_source: str, dossier_destination: str):
    """

    :param dossier_source: Dossier source contenant les fichiers .tcx compressés
    :param dossier_destination: Dossier destination contenant les fichiers .tcx décompressés
    :return: Nothing
    """

    #Création du dossier destination s'il n'existe pas
    os.makedirs(dossier_destination, exist_ok=True)
    #Récupérer tous les fichiers .gz dans le dossier source
    fichiers_gz = [f for f in os.listdir(dossier_source) if f.endswith('.gz')]

    if not fichiers_gz:
        print(f"Aucun fichier dans le dossier {dossier_source}")
        return

    for filename in fichiers_gz:
        chemin_fichier_gz = os.path.join(dossier_source,filename)
        nom_fichier_decompresse = os.path.splitext(filename)[0]
        chemin_fichier_decompresse = os.path.join(dossier_destination, nom_fichier_decompresse)

        try:
            with gzip.open(chemin_fichier_gz, 'rb') as fichier_comprime:
                with open(chemin_fichier_decompresse, 'wb') as fichier_decompresse:
                    fichier_decompresse.write(fichier_comprime.read())
            print(f"Succès de la conversion : {filename} -> {nom_fichier_decompresse}")
        except OSError as e:
            print(f"Erreur lors de la conversion de {filename} : {e}")

