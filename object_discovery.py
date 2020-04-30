def object_discovery(O, detailed=False, name='Unknown'):
    """This will check is the object has a dictionary __dict__ and show what is going on for 
       discovery."""
    obj_id = id(O)

    # This only works if the function is inside of the maincode.
    #for item in globals().keys():
    #    print("item: " + str(item) + " " + str(id(item)))
    #    if id(globals()[item]) == obj_id:
    #        name=str(item)
    #        break

    print("Object name: " + name)
    print("Object id: " + str(obj_id))
    print("Object type: " + str(type(O)))
    if hasattr(O, '__dict__'):
        print("Methods for " + name + ":")
        #if detailed:
            #[print("\t" + str(x) + "\t" + str(type(O.x))) for x in dir(O)]
        #    [print("\t" + str(x)) for x in dir(O)]
        #else:
        [print("\t" + str(x)) for x in dir(O)]


        print("Attributes for object:")
        for key, value in sorted(O.__dict__.items()):
            if detailed:
                #print("\t" + str(key))
                print("\t" + str(key).ljust(30,'-') + str(type(value)))
            else:
                print("\t" + str(key))
