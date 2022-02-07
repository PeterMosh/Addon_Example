import sys

bl_info = {
    'name': 'Add-on name',
    'author': "Petr Moshkantsev",
    'category': 'All',
    'version': (0, 0, 2),
    'blender': (2, 93, 8)
}

debug = 0 # 0 (ON) or 1 (OFF)
 
modules = ["OP", "Prop", "PT"]
 
for mod in modules:
    try:
        exec("from . import {mod}".format(mod=mod))
    except Exception as e:
        print(e)
 
def register():
    
    import importlib
    for mod in modules:
        try:
            if debug:
                exec("importlib.reload({mod})".format(mod=mod))
            exec("{mod}.register()".format(mod=mod))
        except Exception as e:
            print(e)
 
def unregister():
    for mod in modules:
        try:
            exec("{mod}.unregister()".format(mod=mod))
        except Exception as e:
            print(e)
            
if __name__ == "__main__":
    register()