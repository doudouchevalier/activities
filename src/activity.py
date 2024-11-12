from typing import List, Tuple
import folium
from numpy.polynomial.polynomial import polyline


class Activity:
    def __init__(self, coordinates: List[Tuple[float, float]], activity_type: str, duration: float, distance: float,
                 pace: float, elevation_gain: float, datetime: str):
        self.coordinates = coordinates
        self.activity_type = activity_type
        self.duration = duration
        self.distance = distance
        self.pace = pace
        self.elevation_gain = elevation_gain
        self.datetime = datetime
        self.polyline = self.create_polyline_activity()

    def __str__(self):
        return f"{self.activity_type} {self.duration} {self.distance} {self.pace} {self.elevation_gain} {self.datetime}"

    def create_polyline_activity(self) -> folium.PolyLine:
        """Permet de créer le tracé d'une course
        :param coordinates: Liste des coordonnées de l'activité
        :return: objet Polyline à insérer dans la map folium
        """
        self.polyline = folium.PolyLine(
            locations=self.coordinates,
            color='blue',
            weight=4,
            opacity=0.8,
            popup=self.activity_type,
        )
        return self.polyline
