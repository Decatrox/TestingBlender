import bpy

# Set the path to the blend file to be monitored
filepath = "/home/decatrox/Blender projects/untitled.blend"

# Load the blend file
with bpy.data.libraries.load(filepath) as (data_from, data_to):
    # Get the cube object
    cube = data_from.objects["Cube"]

# Any Python object can act as the subscription's owner
owner = object()

# Define the callback function to be called when the data changes
def update_view(*args):
    # Redraw the viewport to update the view
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# Subscribe to changes in the data
bpy.msgbus.subscribe_rna(
    key=cube,
    owner=owner,
    args=(),
    notify=update_view,
)
