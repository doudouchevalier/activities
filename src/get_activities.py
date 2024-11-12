import xml.etree.ElementTree as ET
import os
from typing import List, Tuple
from activity import Activity
from src.tcx_reader import Reader

def _read_activity_from_tcx_file(chemin_fichier: str) -> Activity:
    """Récupère les coordonnées GPS d'un fichier .tcx
    :param chemin_fichier: chemin du fichier
    :return: liste de tuples contenant les coordonnées GPS (latitude, longitude)
    """
    try:
        reader = Reader(chemin_fichier)
        return reader.get_activity()
    except ET.ParseError:
        print(f"Erreur de lecture du fichier XML : {chemin_fichier}")
    except Exception as e:
        print(f"Erreur inattendue lors de la lecture des coordonnées : {e}")

def get_activities_from_all_tcx_files(dossier: str) -> List[Activity]:
    """Récupère les coordonnées GPS de tous les fichiers .tcx contenus dans le dossier
    :param dossier: Chemin du dossier contenant les fichiers .tcx
    :return: Dictionnaire où les clés sont les noms de fichiers
    et les valeurs sont les listes de coordonnées GPS
    """
    activities = []
    for filename in os.listdir(dossier): #Pour chaque fichier
        if filename.endswith('.tcx'): #si il finit par .tcx
            chemin_fichier = os.path.join(dossier, filename) #Créer le fichier
            activity = _read_activity_from_tcx_file(chemin_fichier)
            activities.append(activity)
    return activities