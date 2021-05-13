import bpy

class Snap_Cursor_Center_Operator(bpy.types.Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Snap to center"
    bl_description = "Snap 3D Cursor to Center "

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {"FINISHED"}