# #import bpy
# #import math
# #import time
#
#
# ## Select the default cube object
# #cube = bpy.data.objects['Cube']
#
# ## Rotate the cube by 45 degrees along the Y-axis
# #rotation_angle = math.radians(1)
# #rotation_axis = (0.0, 1.0, 0.0)
#
# #for i in range(45):
# #    cube.rotation_euler.rotate_axis('Y', rotation_angle)
#
# #    # Update the scene to reflect the changes
# #    bpy.context.view_layer.update()
# #    time.sleep(0.1)
# import bpy
# import math
# from easybpy import *
#
# #  bpy.context.active_object
# ## Select the default cube object
# #cube = bpy.data.objects['Cube']
#
# cube = get_object("Cube")
# select_object(cube)
# # or:
# #select_object("Cube")
#
# rot = rotation()
# #rotation(cube, [45.0, -25.0, 60.0])
# rotation(cube, rot)
# scale(cube, [2.0, 2.0, 2.0])
# # location(cube, [1.0, 2.0, 3.0])
# #cube.location[0] +=  1
# location(cube, [cube.location[0]+1.0, 2.0, 3.0])
#
# # Rotate the cube by 45 degrees along the Y-axis
# #rotation_angle = math.radians(45)
# #rotation_axis = (0.0, 1.0, 0.0)
# #cube.rotation_euler.rotate_axis('Y', rotation_angle)
#
#
#
# # Update the scene to reflect the changes
# bpy.context.view_layer.update()
#

import bpy
def Update3DViewPorts():
    for area in bpy.context.window.screen.areas:
        if area.type == 'VIEW_3D':
            area.tag_redraw()
    bpy.ops.wm.save_mainfile()
# Load the "untitled.blend" file
bpy.ops.wm.open_mainfile(filepath="/home/decatrox/Blender projects/untitled.blend")

# Get the "Cube" object by name
cube = bpy.data.objects["Cube"]
print(cube.location)
# Move the object by 2 units in the Y-axis
cube.location.x = 20
print(cube.location)
# bpy.ops.render.render(animation=False, write_still=False, use_viewport=False, layer='', scene='')
# for obj in bpy.context.scene.objects:
#     obj.hide_render = obj.hide_render


# area_type = 'VIEW_3D' # change this to use the correct Area Type context you want to process in
# areas  = [area for area in bpy.context.window.screen.areas if area.type == area_type]
#
# if len(areas) <= 0:
#     raise Exception(f"Make sure an Area of type {area_type} is open or visible in your screen!")
#
# with bpy.context.temp_override(
#     window=bpy.context.window,
#     area=areas[0],
#     # ui_type = 'UV',
#     regions=[region for region in areas[0].regions if region.type == 'WINDOW'][0],
#     screen=bpy.context.window.screen,
# ):
#     Update3DViewPorts()
#     bpy.context.view_layer.update()
Update3DViewPorts()
bpy.ops.wm.save_as_mainfile(filepath="/home/decatrox/Blender projects/untitled.blend")
Update3DViewPorts()
# bpy.ops.render.render(animation=False, write_still=False, use_viewport=False, layer='', scene='')
bpy.context.view_layer.update()


# for area in bpy.context.window.screen.areas:
#         if area.type == 'VIEW_3D':
#             area.tag_redraw()

# for area in bpy.context.screen.areas:
#     print(area.type)
# bpy.context.view_layer.update()
# for area in bpy.context.screen.areas:
#     if area.type == 'VIEW_3D':
#         override = bpy.context.copy()
#         override['area'] = area
#         override['region'] = area.regions[-1]
#         bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1, override=override)

#bpy.context.window.update()

# Redraw the viewport
# for area in bpy.context.screen.areas:
#     if area.type == 'VIEW_3D':
#         for region in area.regions:
#             if region.type == 'WINDOW':
#                 override = {'window': bpy.context.window, 'screen': bpy.context.screen, 'area': area, 'region': region}
#                 bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1, override=bpy.context.window)

# Get the active window and view layer
# window = bpy.context.window
# view_layer = bpy.context.view_layer

# scene = bpy.context.scene
# view_layer = bpy.context.view_layer
# view_layer.objects.active = cube
#
# # Check that both the window and view layer are valid before calling redraw_timer
# # if window and view_layer:
# #     #print("True yes yesy")
# #     override = {'window': bpy.context.window, 'screen': bpy.context.screen}
# #     bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1, override=override)
# # else:
# #     print("Error: Invalid context for redraw_timer operator")
# override = {'area': bpy.context.area, 'region': bpy.context.region, 'edit_object': cube}
# if bpy.ops.wm.redraw_timer.poll(context=override):
#     bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1, context=override)


# get the screen area


# import bpy
#
# # Create a cube and move it
# bpy.ops.mesh.primitive_cube_add()
# bpy.context.object.location[0] = 2.0
#
# # Render an animation
# bpy.context.scene.render.fps = 24
# bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
# bpy.context.scene.render.filepath = '/tmp/output.mp4'
# bpy.context.scene.frame_start = 0
# bpy.context.scene.frame_end = 100
# bpy.ops.render.render(animation=True)
