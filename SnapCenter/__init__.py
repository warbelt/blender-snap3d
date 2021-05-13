# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "Snap3D",
    "author" : "Mario Durántez",
    "description" : "Simple test addon",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . snap_cursor_to_center    import Snap_Cursor_Center_Operator
from . snap_cursor_to_selected  import Snap_Cursor_Selected_Operator
from . toolbox_panel            import Snap_Cursor_Panel

classes = (Snap_Cursor_Center_Operator, Snap_Cursor_Selected_Operator, Snap_Cursor_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)
