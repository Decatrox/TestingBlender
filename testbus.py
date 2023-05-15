import bpy

# Any Python object can act as the subscription's owner.\
bpy.ops.wm.open_mainfile(filepath="/home/decatrox/Blender projects/untitled.blend")
cube = bpy.data.objects["Cube"]
owner = cube

subscribe_to = bpy.context.object.location


def msgbus_callback(*args):
    # This will print:
    # Something changed! (1, 2, 3)
    print("Something changed!", args)


bpy.msgbus.subscribe_rna(
    key=subscribe_to,
    owner=owner,
    args=(1, 2, 3),
    notify=msgbus_callback,
)
owner.location[1] -= 2.0

