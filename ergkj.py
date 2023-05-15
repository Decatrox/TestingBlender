import bpy

# Set the path to the blend file to be monitored
filepath = "/home/decatrox/Blender projects/untitled.blend"

# Load the blend file
bpy.ops.wm.open_mainfile(filepath="/home/decatrox/Blender projects/untitled.blend")

cube = bpy.data.objects["Cube"]

# Any Python object can act as the subscription's owner
owner = object()
subscribe_to = bpy.context.object



# Define the callback function to be called when the data changes
def update_view(*args):
    # Redraw the viewport to update the view
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# Subscribe to changes in the data
bpy.msgbus.subscribe_rna(
    key=subscribe_to,
    owner=owner,
    args=(),
    notify=update_view,
)

cube.location.x -= 2
bpy.ops.wm.save_as_mainfile(filepath="/home/decatrox/Blender projects/untitled.blend")
