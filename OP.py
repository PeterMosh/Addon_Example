import bpy


class OBJECT_OT_Addon_Op1(bpy.types.Operator):
    bl_idname = "object.op1"
    bl_label = "NFT generate"
    
    def execute(self,context):
        scene = context.scene
        mytool = scene.Addon_prop
        
        return {'FINISHED'}
   
classesName = (
    OBJECT_OT_Addon_Op1,
)

def register():
    from bpy.utils import register_class
    for cls in classesName:
        register_class(cls)
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classesName):
        unregister_class(cls)