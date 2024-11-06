import os

import folium
from typing import List, Tuple, Dict
import webbrowser

def create_map_with_activities(center: Tuple[float, float], activities: Dict[str, List[Tuple[float, float]]], output_file: str = "map.html"):
    """Créer une map folium avec les coordonnées GPS de chaque activité reliées par des lignes
    :param activities: Dicitionnaire où chaque clé est le nom de l'activité
    et chaque valeur est une liste de coordonnées GPS
    :param output_file: Nom du fichier de sortie pour la carte HTML. Par défaut 'map.html'
    :return: Nothing
    """
    if not activities:
        print("Aucune activité pour créer la carte.")
        return
    folium_map = folium.Map(location=center, zoom_start=13)

    #Couleurs pour les tracés
    colors = ['blue', 'green', 'red', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen',
              'cadetblue']
    #Ajouter chaque activité dans la carte
    for i, (activity_name, coords) in enumerate(activities.items()):
        if coords:
            folium.PolyLine(
                locations=coords,
                color=colors[i % len(colors)],
                weight=4,
                opacity=0.8,
                popup=activity_name
            ).add_to(folium_map)
    folium_map.save(output_file)
    print(f"Carte créée et enregistrée sous : {output_file}")

    file_path = os.path.abspath(output_file)
    webbrowser.open(f"file://{file_path}")