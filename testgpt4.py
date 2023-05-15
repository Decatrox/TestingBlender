import bpy

bpy.ops.wm.open_mainfile(filepath="/home/decatrox/Blender projects/untitled.blend")

text_editor = None

# Find text editor
for area in bpy.context.screen.areas:
    if area.type == 'TEXT_EDITOR':
        text_editor = area
        break

if text_editor is None:
    raise Exception("No text editor found")

# Override the context
override = bpy.context.copy()
override['area'] = text_editor
override['space_data'] = text_editor.spaces.active
override['region'] = text_editor.regions[-1]
override['edit_text'] = bpy.data.texts["rot45.py.001"]

bpy.ops.text.run_script(override)
