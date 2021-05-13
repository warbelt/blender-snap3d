import bpy

class SNAP3D_PT_snapCursorPanel(bpy.types.Panel):
    bl_idname = "SNAP3D_PT_snapCursorPanel"
    bl_label = "Snap 3D Cursor"
    bl_category = "Snap3D"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("view3d.cursor_center", text="Center")
        row = layout.row()
        row.operator("view3d.cursor_selected", text="Selected")
