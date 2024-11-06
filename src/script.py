from gmplot import gmplot
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt

nbcoord = 0

    # Afficher les coordonnées



def add_coordinates_to_map(gmap, coordinates: list):
    latitudes, longitudes = zip(*coordinates)
    gmap.scatter(latitudes, longitudes, 'red', size=40, marker=True)



# Exécuter la fonction pour traiter tous les fichiers .tcx dans le dossier
all_coords = process_all_files("activitesTCX")
# Créer une carte Google Map
gmap = gmplot.GoogleMapPlotter(latitude_centre, longitude_centre, 13)

print("Nombre de coordonnées : ", nbcoord)

# Calculer les moyennes
mean_latitude, mean_longitude = calculate_mean_coordinates(all_coords)
print(f"Moyenne des latitudes : {mean_latitude}, Moyenne des longitudes : {mean_longitude}")

# Ajouter toutes les coordonnées à la carte
add_coordinates_to_map(gmap, [(mean_latitude, mean_longitude)])

# Enregistrer et ouvrir la carte dans le navigateur
fichier_html = 'ma_carte.html'
gmap.draw(fichier_html)
webbrowser.open(fichier_html)