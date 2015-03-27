'''
print all catalogs, users, and organizations in the content exchange
'''
from air.api.orm import *
become_system()

ENTITY_NAME={}
for entity in Entity.find():
    ENTITY_NAME[entity.oid()]=entity.document['display_name']

print "Display All Organizations, Users, and Catalogs in Content exchange...."
#print all catalogs, users, and organizations in the content exchange
print "\nUsers in Content Exchange: "
for user in User.find():
    if user.is_in_content_exchange():
        print ' ', user.slug(), ':', ENTITY_NAME[user.oid()]

print "\nOrganizations in Content Exchange: "
for org in Organization.find():
    if org.is_in_content_exchange():
        print ' ', org.slug(), ':', ENTITY_NAME[org.oid()]

print "\nCatalogs in Content Exchange: [Owner]: Catalog Name (catalog slug) "
for catalog in Catalog.find():
    if catalog.is_in_content_exchange():
        print ' [', ENTITY_NAME[catalog.document['owner']], ']: ', catalog.document['display_name'], ' (', catalog.slug(), ')'

print "\n"