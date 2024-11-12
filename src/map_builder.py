import os
import folium
from typing import List, Tuple
import webbrowser
from activity import Activity

class Map:
    def __init__(self, activities: List[Activity]):
        self.activities = activities
        self.center = None
        self.center = self._get_map_center()
        self.map = folium.Map(location=self.center, zoom_start=8)

    def create_map_with_activities(self, output_file: str = "map.html"):
        """Créer une map folium avec les coordonnées GPS de chaque activité reliées par des lignes
        :param activities: Dicitionnaire où chaque clé est le nom de l'activité
        et chaque valeur est une liste de coordonnées GPS
        :param output_file: Nom du fichier de sortie pour la carte HTML. Par défaut 'map.html'
        :return: Nothing
        """
        if not self.activities:
            print("Aucune activité pour créer la carte.")
            return

        #Ajouter chaque activité dans la carte
        for activity in self.activities:
            if activity.coordinates:
                 activity.polyline.add_to(self.map)
        self.map.save(output_file)
        print(f"Carte créée et enregistrée sous : {output_file}")

        file_path = os.path.abspath(output_file)
        webbrowser.open(f"file://{file_path}")

    def _get_map_center(self) -> Tuple[float, float]:
        """Calculates the average coordinates of all activities.
        :param activities: Dicitonary of activities.
        :return: Tuple of average coordinates.
        """
        total_latitude = 0.0
        total_longitude = 0.0
        count = 0

        for activity in self.activities:
            for latitude, longitude in activity.coordinates:
                total_latitude += latitude
                total_longitude += longitude
                count += 1
        if count == 0:
            return 0.0, 0.0
        average_latitude = total_latitude / count
        average_longitude = total_longitude / count
        return average_latitude, average_longitude

    def get_activities_from_type(self, type: str, output_file: str = "map.html") -> List[folium.PolyLine]:
        """Récupère tous les tracés d'un type d'activité donné
        :param type: type d'activité
        :return: liste des tracés
        """
        polylines_list = []
        for activity in self.activities:
            if activity.activity_type == type:
                polylines_list.append(activity.polyline)
        return polylines_list

    def _add_polylines_to_map(self, polylines: List[folium.PolyLine], output_file: str = "map.html") -> None:
        """Supprime tous les tracés ajoutés sur la map."""
        self.map = folium.Map(location=self.center, zoom_start=8)
        for polyline in polylines:
            self.map.add_to(self.map)
        self.map.save(output_file)
        file_path = os.path.abspath(output_file)
        webbrowser.open(f"file://{file_path}")
