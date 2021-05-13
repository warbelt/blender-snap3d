import bpy

class Snap_Cursor_Selected_Operator(bpy.types.Operator):
    bl_idname = "view3d.cursor_selected"
    bl_label = "Snap to selected"
    bl_description = "Snap 3D Cursor to Selected "

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        return {"FINISHED"}