'''
print all objects owned by org
'''
from air.api.orm import *
from pprint import pprint as pp

become_system()

def add_to_dict(obj_dict, obj_type, scope_lookup):
    if obj_type is Organization:
        lookup_value={'owners': scope_lookup}
    elif obj_type is Content:
        lookup_value={'catalog': scope_lookup}
    elif obj_type is Catalog:
        lookup_value={'owner': scope_lookup}
    else:
        lookup_value={'scope': scope_lookup}
    for obj in obj_type.find(lookup_value):
        if isinstance(obj, Content):
            if not obj.document['title']:
                dict_value="none"
            else:
                dict_value=obj.document['title']
        else:
            dict_value=obj.document['display_name']
        obj_dict[obj.document['_id']]=dict_value
    if None in obj_dict:
        del obj_dict[None]

def check_if_owns(obj_type, scope_lookup):
    sum=0
    check_owned=False
    if obj_type is Organization:
        lookup_value={'owners': scope_lookup}
    elif obj_type is Catalog:
        lookup_value={'owner': scope_lookup}
    elif obj_type is Content:
        lookup_value={'catalog': scope_lookup}
    else:
        lookup_value={'scope': scope_lookup}
    for x in obj_type.find(lookup_value):
        sum+=1
    if sum > 0:
        check_owned=True
    return check_owned

def print_objs(obj_dict):
    if not obj_dict:
        print "No owned objects"
    for k in obj_dict.keys():
        print ' ', k, ':', obj_dict[k]

ENTITY_NAME={None: "<none>"}
for org in Organization.find():
    ENTITY_NAME[org.slug()]=org.document['display_name']

ORGS_OWNED={None: "<none>"}
CATS_OWNED={None: "<none>"}
PLAYERS_OWNED={None: "<none>"}
DIST_OWNED={None: "<none>"}
ADS_OWNED={None: "<none>"}
PLAYLISTS_OWNED={None: "<none>"}
ALGOS_OWNED={None: "<none>"}

print "Will display all objects owned by Organization\n"
slug_to_load=raw_input('Enter slug of Organization: ')

if slug_to_load in ENTITY_NAME:
    org_to_load=Organization.load(slug_to_load)
if check_if_owns(Organization, org_to_load.oid()):
    add_to_dict(ORGS_OWNED, Organization, org_to_load.oid())
if check_if_owns(Distribution, org_to_load.oid()):
    add_to_dict(DIST_OWNED, Distribution, org_to_load.oid())
if check_if_owns(Ad, org_to_load.oid()):
    add_to_dict(ADS_OWNED, Ad, org_to_load.oid())
if check_if_owns(Player, org_to_load.oid()):
    add_to_dict(PLAYERS_OWNED, Player, org_to_load.oid())
if check_if_owns(Catalog, org_to_load.oid()):
    add_to_dict(CATS_OWNED, Catalog, org_to_load.oid())
    for catalog in CATS_OWNED.keys():
        if check_if_owns(Playlist, catalog):
            add_to_dict(PLAYLISTS_OWNED, Playlist, catalog)
        if check_if_owns(AlgoPlaylist, catalog):
            add_to_dict(ALGOS_OWNED, AlgoPlaylist, catalog)

print "\nOrganizations owned:"
print_objs(ORGS_OWNED)
print "\nCatalogs owned:"
print_objs(CATS_OWNED)
print "\nDistributions owned:"
print_objs(DIST_OWNED)
print "\nAds owned:"
print_objs(ADS_OWNED)
print "\nPlayers owned:"
print_objs(PLAYERS_OWNED)
print "\nPlaylists owned:"
print_objs(PLAYLISTS_OWNED)
print "\nAlgoPLaylists owned:"
print_objs(ALGOS_OWNED)
print "\n"