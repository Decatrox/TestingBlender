import bpy
import os

def process_commands(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r') as f:
        lines = f.readlines()

    cube = bpy.data.objects.get('Cube')

    for line in lines:
        if cube:
            command, value = line.strip().split(':')
            value = float(value)

            if command == "rotate_x":
                cube.rotation_euler.x += value
            elif command == "rotate_y":
                cube.rotation_euler.y += value
            elif command == "move_x":
                cube.location.x += value
            elif command == "move_y":
                cube.location.y += value
            # Add more commands here as needed

class ModalTimerOperator(bpy.types.Operator):
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Modal Timer Operator"

    _timer = None
    commands_file = "/home/decatrox/PycharmProjects/TestingBlender/commands.txt"

    def modal(self, context, event):
        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':
            process_commands(self.commands_file)

        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

def register():
    bpy.utils.register_class(ModalTimerOperator)

def unregister():
    bpy.utils.unregister_class(ModalTimerOperator)

if __name__ == "__main__":
    register()

    # Start the operator
    bpy.ops.wm.modal_timer_operator()
