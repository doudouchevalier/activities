from typing import Dict, List, Tuple

def calculate_average_coordinates(activities: Dict[str, List[Tuple[float, float]]]) -> Tuple[float, float]:
    """Calculates the average coordinates of all activities.
    :param activities: Dicitonary of activities.
    :return: Tuple of average coordinates.
    """
    total_latitude = 0.0
    total_longitude = 0.0
    count = 0

    for coordinates in activities.values():
        for latitude, longitude in coordinates:
            total_latitude += latitude
            total_longitude += longitude
            count += 1
    if count == 0:
        return 0.0, 0.0
    average_latitude = total_latitude / count
    average_longitude = total_longitude / count
    return average_latitude, average_longitude