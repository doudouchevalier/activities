import xml.etree.ElementTree as ET
from typing import List, Tuple

from src.activity import Activity


class Reader:
    def __init__(self, chemin_fichier: str):
        self.chemin_fichier = chemin_fichier
        self.namespace = {'ns': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}
        self.tree = ET.parse(chemin_fichier)
        self.root = self.tree.getroot()

    def get_activity(self) -> Activity:
        coordinates = self._extract_coordinates()
        activity_type = self._extract_activity_type()
        duration = self._extract_duration()
        distance = self._extract_distance()
        pace = duration / distance
        elevation_gain = self._extract_elevation_gain()
        datetime = self._extract_datetime()
        return Activity(coordinates, activity_type, duration, distance, pace, elevation_gain, datetime)

    def _extract_coordinates(self) -> List[Tuple[float, float]]:
        trackpoints = self.root.findall('.//ns:Trackpoint', self.namespace)
        coordonnees = []
        for trackpoint in trackpoints:
            latitude = trackpoint.find('ns:Position/ns:LatitudeDegrees', self.namespace)
            longitude = trackpoint.find('ns:Position/ns:LongitudeDegrees', self.namespace)
            if latitude is not None and longitude is not None:
                coordonnees.append((float(latitude.text), float(longitude.text)))
        return coordonnees

    def _extract_activity_type(self) -> str:
        return self.root.find('.//ns:Activity', self.namespace).get('Sport')

    def _extract_duration(self) -> float:
        """Obtenir la durée en minutes
        :param root:
        :param namespace:
        :return:
        """
        return float(self.root.find('.//ns:TotalTimeSeconds', self.namespace).text) / 60

    def _extract_distance(self) -> float:
        """Obtenir la distance en km
        :param root:
        :param namespace:
        :return:
        """
        return float(self.root.find('.//ns:DistanceMeters', self.namespace).text) / 1000

    def _extract_elevation_gain(self) -> float:
        elevation_gains = self.root.findall('.//ns:AltitudeMeters', self.namespace)
        if elevation_gains:
            elevations = [float(e.text) for e in elevation_gains]
            elevation_gain = max(elevations) - min(elevations)
        else:
            elevation_gain = 0.0
        return elevation_gain

    def _extract_datetime(self):

        # Espace de noms utilisé dans les fichiers TCX

        # Trouver tous les éléments de type 'Activity'
        activities = self.root.findall('.//ns:Activity', self.namespace)

        # Récupérer la première date de début d'activité trouvée
        if activities:
            activity = activities[0]
            start_time = activity.find('ns:Id', self.namespace).text
            return start_time
        else:
            return None