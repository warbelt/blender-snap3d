import bpy

class Snap_Cursor_Panel(bpy.types.Panel):
    bl_idname = "snap_cursor_panel"
    bl_label = "Snap 3D Cursor"
    bl_category = "Snap"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator("view3d.cursor_center", text="Center")
        row = layout.row()
        row.operator("view3d.cursor_selected", text="Selected")