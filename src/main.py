from get_activities import *
from conversion import *
from map_builder import *

dossier_source = "../export_107498170/activities"
dossier_destination = '../activitesTCX'
#convert_to_tcx(dossier_source, dossier_destination)
list= get_activities_from_all_tcx_files(dossier_destination)
map = Map(list)
map.create_map_with_activities()