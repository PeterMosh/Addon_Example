import bpy

class VIEW3D_PT_Addon_Panel_One(bpy.types.Panel):
    
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Addon Example"
    bl_label = "Panel One"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.Addon_prop
        row.label(text='Addon Panel One')
        col_main = layout.box().column(align=False)
        split = col_main.split(factor=0.6)
        col_1 = split.column(align=True)
        col_2 = split.column(align=True)

class VIEW3D_PT_Addon_Panel_Two(bpy.types.Panel):
    bl_parent_id = "VIEW3D_PT_Addon_Panel_One"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Addon Example"
    bl_label = "Panel Two"
    
    def draw(self, context):
        layout = self.layout    
        scene = context.scene
        mytool = scene.Addon_prop
        row = layout.row(align=True)
        row.label(text='Addon Panel Two')


classesName = (
    VIEW3D_PT_Addon_Panel_One,
    VIEW3D_PT_Addon_Panel_Two,
)

def register():
    from bpy.utils import register_class
    for cls in classesName:
        register_class(cls)
    
    
def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classesName):
        unregister_class(cls)