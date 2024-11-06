import xml.etree.ElementTree as ET
import os
from typing import List, Tuple, Dict

def _read_coordinates_from_tcx_file(chemin_fichier: str) -> List[Tuple[float, float]]:
    """Récupère les coordonnées GPS d'un fichier .tcx
    :param chemin_fichier: chemin du fichier
    :return: liste de tuples contenant les coordonnées GPS (latitude, longitude)
    """
    try:
        tree = ET.parse(chemin_fichier)
        root = tree.getroot()
        namespace = {'ns': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}
        trackpoints = root.findall('.//ns:Trackpoint', namespace)
        coordonnees = []
        for trackpoint in trackpoints:
            latitude = trackpoint.find('ns:Position/ns:LatitudeDegrees', namespace)
            longitude = trackpoint.find('ns:Position/ns:LongitudeDegrees', namespace)
            if latitude is not None and longitude is not None:
                coordonnees.append((float(latitude.text), float(longitude.text)))
        return coordonnees
    except ET.ParseError:
        print(f"Erreur de lecture du fichier XML : {chemin_fichier}")
    except Exception as e:
        print(f"Erreur inattendue lors de la lecture des coordonnées : {e}")

def get_coordinates_from_all_tcx_files(dossier: str) -> Dict[str, List[Tuple[float, float]]]:
    """Récupère les coordonnées GPS de tous les fichiers .tcx contenus dans le dossier
    :param dossier: Chemin du dossier contenant les fichiers .tcx
    :return: Dictionnaire où les clés sont les noms de fichiers
    et les valeurs sont les listes de coordonnées GPS
    """
    all_coordinates = {}
    for filename in os.listdir(dossier): #Pour chaque fichier
        if filename.endswith('.tcx'): #si il finit par .tcx
            chemin_fichier = os.path.join(dossier, filename) #Créer le fichier
            coordonnees = _read_coordinates_from_tcx_file(chemin_fichier)
            all_coordinates[filename] = coordonnees#ajouter les coordonnées du fichier de l'activité
    return all_coordinates

def print_single_activity_coordinates(activity : List[Tuple[float, float]]) -> None:
    """Afficher tous les tuples de coordonnées GPS d'une activité.
    :param activity: Liste de tuples de coordonnées GPS d'une activité
    :return: Nothing
    """
    for tuple in activity:
        print_tuple_x_y(tuple)

def print_tuple_x_y(tuple: Tuple[float, float]) -> None:
    print(f"Latitude: {tuple[0]}, Longitude: {tuple[1]}\n")

def print_all_activity_coordinates(activities : Dict[str, List[Tuple[float, float]]]) -> None:
    """Afficher les coordonnées GPS de toutes les activités contenues dans le dictionnaire.
    :param activities: Dictionnaire des activités
    :return: Nothing
    """
    for filename, coordonnees in activities.items():
        print(f"\nCoordonnées pour l'activité '{filename}'")
        print_single_activity_coordinates(coordonnees)