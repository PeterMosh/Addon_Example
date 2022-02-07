import bpy
from . import OP

class Addon_Properties(bpy.types.PropertyGroup):

    prop1 : bpy.props.EnumProperty(
        name="prop1",
        description="",
        items=[ ('1', "Mode 1", "one"),
                ('2', "Mode 2", "two"),
                ('3', "Mode 3", "three"),
               ]
        )
    prop2 : bpy.props.BoolProperty(
        name="prop2",
        description="",
        default = True
        )
    prop3 : bpy.props.IntProperty(
        name="prop3",
        description="",
        default = 2,
        min = 1,
        max=10,
        subtype='UNSIGNED'
        )

classesName = (
    Addon_Properties,
)

def register():
    from bpy.utils import register_class
    for cls in classesName:
        register_class(cls)
    bpy.types.Scene.Addon_prop = bpy.props.PointerProperty(type = Addon_Properties)
    
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classesName):
        unregister_class(cls)
    del bpy.types.Scene.Addon_prop