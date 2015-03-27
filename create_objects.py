from air.api.orm import *

obj_to_create=raw_input('p=Player, u=User, o=Organization, d=Distribution, c=Catalog, ag=AlgoPlaylist, ad=Ad: ')
if obj_to_create=='u':
    num=raw_input('enter number of users to create: ')
    become_system()
    for i in range(int(num)):
        display_name=raw_input('enter display_name: ')
        hande=raw_input('enter handle: ')
        password=raw_input('enter password: ')
        email=raw_input('enter email: ')
        u=Users.new(display_name=display_name, handle=handle, password=password, email=email)
        check_set_in_content_exchange=raw_input('does this User have access to view all the content? (y/n): ')
        if check_set_in_content_exchange=='y':
            u.set_in_content_exchange(True)
        print "[{}:{}] scope:{}".format(u.document['handle'], u.slug(), u.document['scope'])
        if u.is_in_content_exchnage()==True
            print "{} is in content exchange.".format(u.document['handle'])

elif obj_to_create=='o':
    num=raw_input('enter number of organizations to create: ')
    get_credentials().clear()
    become_system()
    for i in range(int(num)):
        display_name=raw_input('enter display_name: ')
        hande=raw_input('enter handle: ')
        o=Organization.new(display_name=display_name, handle=handle)
        check_set_owner=raw_input('do you want to set owners? (y/n): ')
        if check_set_owner=='y':
            num_owners=raw_input('how many owners?': )
            for j in range(int(num_owners))
                ## check to make sure input is an actual UUID
                owner=raw_input('enter owner slug: ')
                owner_UUID=slug2uuid(owner)
                if not isinstance(owner_UUID, UUID)
                    raise TypeError ('not an UUID')
                if isinstance(owner_UUID, UUID)
                    o.add_owner(owner)
        check_set_in_content_exchange=raw_input('does this Organization have access to view all the content? (y/n): ')
        if check_set_in_content_exchange=='y':
            o.set_in_content_exchange(True)
        print o.export()
        print "[{}:{}] scope:{}".format(o.document['handle'], o.slug(), o.document['scope'])
        if o.is_in_content_exchnage()==True
            print "{} is in content exchange.".format(o.document['handle'])

elif obj_to_create=='c':
    num=raw_input('enter number of Catalogs to create: ')
    get_credentials().clear()
    become_system()
    for i in range(int(num)):
        display_name=raw_input('enter display_name: ')
        owner=raw_input('enter owner slug: ')
        owner_UUID=slug2uuid(owner)
        if not isinstance(owner_UUID, UUID)
            raise TypeError ('not an UUID')
        if isinstance(owner_UUID, UUID)
            c=Catalog.new(display_name=display_name, owner=owner)
        check_set_in_content_exchange=raw_input('does this catalog belong in the content exchange? (y/n): ')
        if check_set_in_content_exchange=='y':
            c.set_in_content_exchange(True)
        print c.export()
        print "[{}:{}] owner:{} scope:{}".format(c.document['display_name'], c.slug(), c.document['owner'], c.document['scope'])
        if c.is_in_content_exchnage()==True
            print "{} is in content exchange.".format(c.document['display_name'])

elif obj_to_create=='d'
    num=(raw_input'enter number of Distributions to create: ')
    get_credentials().clear()
    become_system()
    for i in range(int(num)):
        display_name=raw_input('enter display_name: ')
        owner=raw_input('enter owner slug: ')
        owner_UUID=slug2uuid(owner)
        if not isinstance(owner_UUID, UUID)
            raise TypeError ('not an UUID')
        if isinstance(owner_UUID, UUID)
            d=Distribution.new(display_name=display_name, owner=owner)
        print d.export()
        print "[{}:{}] owner:{}".format(d.document['display_name'], d.slug(), d.document['owner'])

elif obj_to_create=='ad':
    num=raw_input('enter number of Ads to create: ')
    get_credentials().clear()
    become_system()
    for i in range(int(num)):
        display_name=raw_input('enter display_name: ')
        link=raw_input('url: ')
        set_type=raw_input('type: ')
                owner=raw_input('enter owner slug: ')
        owner_UUID=slug2uuid(owner)
        if not isinstance(owner_UUID, UUID)
            raise TypeError ('not an UUID')
        if isinstance(owner_UUID, UUID)
            x=Ad.new(display_name=display_name, owner=owner, url=link, type=set_type)
        print x.export()
        print "[{}:{}] owner:{}".format(x.document['display_name'], x.slug(), x.document['owner'])

elif obj_to_create=='p'
    num=raw_input('enter number of Players to create: ')
    get_credentials().clear()
    become_system()
    for i in range(int(num)):
        display_name=raw_input('enter display_name: ')
        owner=raw_input('enter owner slug: ')
        owner_UUID=slug2uuid(owner)
        if not isinstance(owner_UUID, UUID)
            raise TypeError ('not an Entity UUID')
        distribution=raw_input('enter distribution slug:')
        distribution_UUID=slug2uuid(distribution)
        if not isinstance(distribution_UUID, UUID)
            raise TypeError ('not a Distribution UUID')
        if isinstance(owner_UUID, UUID)
            if isinstance(distribution_UUID, UUID)
                p=Player.new(display_name=display_name, owner=owner, distribution=distribution)
        check_autoplay=raw_input('is player autoplay? (y/n): ')
        if check_autoplay=='y':
            p.document['autoplay']=True
        check_mouse_over=raw_input('mouse over for sound? (y/n): ')
        if check_mouse_over=='y':
            p.document['hover']=True
            volume=raw_input('volume: ')
            p.document['volume']=int(volume)
            hover_volume=raw_input('hover_volume:')
            p.document['hover_volume']=int(hover_volume)
        size_type=raw_input('size_type: ')
        h=raw_input('height: ')
        w=raw_input('width: ')
        check_playlist_bar=raw_input('do you wish to set playlist_bar? (y/n): ')
        if check_playlist_bar=='n'
            if size_type=='fixed'
                p.document['size']={'type':size_type, 'width':int(w), 'height':int(h)}
            elif size_type=='shrink-to-fit'
                p.document['size']={'type':size_type, 'aspect_ratio':16/9.0, 'extra_height':0}
        elif check_playlist_bar=='y'
            bar_height=raw_input('playlist bar height: ')
            p.document['playlist_bar']={'type':'bottom', 'height':int(bar_height)}
            p.document['size']={'type':size_type, 'aspect_ratio':16/9.0, 'extra_width':100, 'extra_height':int(bar_height)}
        check_ad=raw_input('has the ad already been created? (y/n): ')
        if check_ad=='y':
            ad_tag=raw_input('enter ad slug: ')
            ad_UUID=slug2uuid(ad_tag)
            if not isinstance(ad_UUID, UUID)
                raise TypeError ('not an Ad UUID')
            if isinstance(ad_UUID, UUID)
                p.document['preroll']=ad_tag
        print "Player Name: {} [{}], Owner: {}, Distribution: {}".format(p.document['display_name'], p.slug(), p.document['owner'], p.document['distribution'])

elif obj_to_create=='ag':
    num=raw_input('enter number of AlgoPlaylists to create: ')
    get_credentials().clear()
    become_system()
    for i in range(int(num)):
        title=raw_input('title: ')
        owner=raw_input('enter owner slug: ')
        owner_UUID=slug2uuid(owner)
        if not isinstance(owner_UUID, UUID)
            raise TypeError ('not a Owner UUID')
        catalog=raw_input('enter catalog slug: ')
        catalog_UUID=slug2uuid(catalog)
        if not isinstance(catalog_UUID, UUID)
            raise TypeError ('not a Catalog UUID')
        if isinstance(owner_UUID, UUID)
            if isinstance(catalog_UUID, UUID)
                y=AlgoPlaylist.new(title=title, owner=owner, catalog=catalog)
        print "Title: {} [{}], Owner: {}, Catalog: {}".format(y.document['title'], y.slug(), y.document['owner'], y.document['catalog'])