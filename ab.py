import subprocess
import time

# Path to the Blender executable
blender_path = "/snap/blender/3486/blender"

# Path to the blend file to open
blend_file_path = "/home/decatrox/Blender projects/untitled.blend"

# Open Blender in the background
process = subprocess.Popen([blender_path, blend_file_path])

# Wait for Blender to start
time.sleep(5)

# Connect to Blender using the Blender API
import bpy
bpy.context.scene.render.engine = 'CYCLES'
# bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object

# Rotate the cube
for i in range(0, 360, 5):
    cube.rotation_euler = (0, 0, i * 0.0174533)
    bpy.context.view_layer.update()

# Terminate the Blender process
process.terminate()
