import bpy
import time

# Get the default cube object
cube = bpy.data.objects['Cube']

# Set initial rotation and rotation speed
rotation = 0.0
rotation_speed = 0.1

# Define start and stop conditions
rotate = False  # Start condition
stop_rotation = False  # Stop condition


# Define a function to handle key presses
def handle_key_press(event):
    global rotate, stop_rotation

    if event.type == 'LEFTMOUSE' and event.value == 'PRESS':
        # Start the rotation on left mouse click
        rotate = True
    elif event.type == 'RIGHTMOUSE' and event.value == 'PRESS':
        # Stop the rotation on right mouse click
        rotate = False
        stop_rotation = True


# Register the key press handler function
bpy.types.SpaceView3D.draw_handler_add(handle_key_press, (), 'WINDOW', 'POST_PIXEL')


# Define a function to rotate the cube
def rotate_cube():
    global rotation

    # Rotate the cube
    cube.rotation_euler[2] += rotation_speed

    # Update the rotation angle
    rotation += rotation_speed

    # Reset rotation angle if it exceeds 360 degrees
    if rotation >= 2 * 3.14159:
        rotation = 0.0

    # Stop the rotation if stop condition is met
    if stop_rotation:
        return False

    return True


# Define a function to handle the rendering loop
def render_loop():
    if rotate:
        rotate_cube()
        time.sleep(6)

    # Schedule the next rendering update
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)


# Start the rendering loop
bpy.app.timers.register(render_loop)
