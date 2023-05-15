import bpy

print("Running script...")

# Select the default cube object
cube = bpy.data.objects['Cube']

if cube:
    print("Cube found, changing color...")

    # Ensure the cube has a material
    if cube.data.materials:
        mat = cube.data.materials[0]
    else:
        # Create a new material
        mat = bpy.data.materials.new(name="New_Material")
        cube.data.materials.append(mat)

    # Change the material's color
    mat.diffuse_color = (0, 0, 0, 1)  # Set color to red

    # Force screen update
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            area.tag_redraw()
else:
    print("Cube not found!")
