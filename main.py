# This is a sample Python script.
import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import bpy

# Set the path to the blend file
blend_file_path = '/home/decatrox/Blender projects/untitled.blend1'

# Load the blend file
with bpy.data.libraries.load(blend_file_path) as (data_from, data_to):
    data_to.objects = data_from.objects

# Get the cube object
# cube = data_to.objects['Cube']
cube = bpy.context.view_layer.objects.active

# Rotate the cube
# Rotate the cube by 45 degrees along the Y-axis
rotation_angle = math.radians(45)
rotation_axis = (0.0, 1.0, 0.0)
cube.rotation_euler.rotate_axis('Y', rotation_angle)
# Save the changes
bpy.ops.wm.save_as_mainfile(filepath=blend_file_path)




# Update the scene to reflect the changes
# bpy.context.view_layer.update()

