from get_coordinates import *
from conversion import *
from coordinates_calculations import *
from map import *

dossier_source = "../export_107498170/activities"
dossier_destination = '../activitesTCX'
#convert_to_tcx(dossier_source, dossier_destination)
dico = get_coordinates_from_all_tcx_files(dossier_destination)
#print_all_activity_coordinates(dico)
average = calculate_average_coordinates(dico)
create_map_with_activities(average, dico)