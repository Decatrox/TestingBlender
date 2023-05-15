import bpy

bpy.ops.wm.open_mainfile(filepath="/home/decatrox/Blender projects/untitled.blend")

# Get the text data block
text_block = bpy.data.texts.get("rot45.py.001")

if text_block is None:
    raise Exception("Script not found in .blend file")

# Execute the script
exec(text_block.as_string())
