import bpy
import time

time.sleep(3)

bpy.ops.wm.open_mainfile(filepath="/home/decatrox/Blender projects/untitled.blend")
for area in bpy.context.window.screen.areas:
    print(area.type)
    # if area.type=='TEXT_EDITOR':
        # bpy.context.area = area
print(bpy.context.mode)
# bpy.context.space_data.region_3d

# for window in bpy.context.window_manager.windows:
#     screen = window.screen
#
#     for area in screen.areas:
#         if area.type == 'TEXT_EDITOR':
#             override = {'window': window, 'screen': screen, 'area': area}
#             bpy.ops.screen.screen_full_area(override)
#             break

# print("area type" + bpy.context.area.type)
area_type = 'TEXT_EDITOR' # change this to use the correct Area Type context you want to process in
areas  = [area for area in bpy.context.window.screen.areas if area.type == area_type]

if len(areas) <= 0:
    raise Exception(f"Make sure an Area of type {area_type} is open or visible in your screen!")

with bpy.context.temp_override(
    window=bpy.context.window,
    area=areas[0],
    # ui_type = 'UV',
    regions=[region for region in areas[0].regions if region.type == 'WINDOW'][0],
    screen=bpy.context.window.screen,
    space_data=bpy.data.texts["rot45.py"]
):
    print("ui type " + bpy.context.area.ui_type)
    print("area type " + bpy.context.area.type)
    bpy.ops.text.run_script()
    # bpy.ops.text.run_script(filepath="/home/decatrox/Blender projects/rot45.py")
