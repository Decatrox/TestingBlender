# with open("/home/decatrox/Blender projects/untitled.blend", 'r', encoding='UTF-16') as blend:
#     with open("blendout.txt", 'w') as out:
#         lines = blend.readlines()
#         for line in lines:
#             out.writelines(line)

import codecs

with open('/home/decatrox/Blender projects/untitled.blend', 'rb') as f:
    data = f.read()

# Add a BOM to the beginning of the data
data_with_bom = codecs.BOM_UTF16_LE + data

# Decode the data as UTF-16
# Assume 'data' contains the byte string you're trying to decode
decoded_data = data.decode('utf-16-le', errors='ignore')
with open("blendout.txt", 'w') as out:
    out.writelines(decoded_data)

