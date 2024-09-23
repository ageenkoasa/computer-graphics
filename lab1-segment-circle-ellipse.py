from PIL import Image, ImageDraw
from axes_drawer import draw_axes

# Создание нового изображения (белый фон, размер 500x500 пикселей)
width, height = 500, 500
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Центр изображения
center_x = width // 2
center_y = height // 2


# Рисование осей, делений и меток
draw_axes(draw, width, height, tick_interval=50)

# Рисование отрезка
line_start = (-200, -200)
line_end = (200, 200)
draw.line([line_start[0] + center_x, center_y - line_start[1],
           line_end[0] + center_x, center_y - line_end[1]], fill='red', width=3)

# Рисование окружности
circle_center = (0, 0)
circle_radius = 50
# draw.ellipse([circle_center[0] - circle_radius, circle_center[1] - circle_radius,
#               circle_center[0] + circle_radius, circle_center[1] + circle_radius],
#              outline='green', width=3)
draw.ellipse([circle_center[0] - circle_radius + center_x, center_y - circle_center[1] - circle_radius,
              circle_center[0] + circle_radius + center_x, center_y - circle_center[1] + circle_radius],
                outline='green', width=3)

# Рисование эллипса
ellipse_bbox = [-200, -200, 200, 0] # [Коорд-та X левого верхнего угла огран.прям-ка, Коорд-та Y левого верхнего угла огран. прям-ка, Коорд-та X правого нижнего угла огран. прям-ка, Коорд-та Y правого нижнего угла огран. прям-ка]
draw.ellipse([ellipse_bbox[0] + center_x, center_y - ellipse_bbox[3],
              ellipse_bbox[2] + center_x, center_y - ellipse_bbox[1]], outline='blue', width=3)



# Сохранение изображения
image.save('imgs/lab1-output.png')

# Открытие изображения (для проверки результата)
image.show()
