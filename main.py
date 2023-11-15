import colorgram
color_list = []
colors = colorgram.extract('image.jpg', 100)
for color in colors:
    color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))

print(color_list)
