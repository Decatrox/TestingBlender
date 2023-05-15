import bpy
from easybpy import *

a = link_object('/home/decatrox/Blender projects/untitled.blend', "Cube")
select_object("Cube")
location(a, [1.0, 2.0, 3.0])


