# https://pypi.org/project/colorgram.py/
import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

# import os
# import colorgram

# # Print the current working directory for debugging
# print("Current working directory:", os.getcwd())

# # Try to extract colors from "image.jpg"
# try:
#     rgb_colors = []
#     colors = colorgram.extract("image.jpg", 30)
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         rgb_colors.append(new_color)
#     print(rgb_colors)
# except Exception as e:
#     print("Error:", e)
