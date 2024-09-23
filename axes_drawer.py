from PIL import ImageDraw, ImageFont

def draw_axes(draw: ImageDraw, width: int, height: int, tick_interval: int = 50):
    """
    Рисует оси X и Y с делениями и метками на изображении.
    
    :param draw: Объект ImageDraw для рисования на изображении.
    :param width: Ширина изображения.
    :param height: Высота изображения.
    :param tick_interval: Интервал для делений на осях.
    """
    # Параметры осей
    axis_color = 'gray'
    axis_width = 2
    tick_color = 'gray'
    tick_length = 10
    label_font = ImageFont.load_default()  # Шрифт для меток (используется стандартный шрифт PIL)

    # Центр изображения
    center_x = width // 2
    center_y = height // 2

    # Рисование осей X и Y
    draw.line([(0, center_y), (width, center_y)], fill=axis_color, width=axis_width)  # Ось X
    draw.line([(center_x, 0), (center_x, height)], fill=axis_color, width=axis_width)  # Ось Y

    # Нанесение делений и меток на оси X и Y
    for x in range(center_x - (center_x // tick_interval) * tick_interval, width, tick_interval):
        if x != center_x:  # Пропустить центр, чтобы не дублировать деление
            draw.line([(x, center_y - tick_length), (x, center_y + tick_length)], fill=tick_color, width=axis_width)
            draw.text((x + 2, center_y + tick_length + 2), str(x - center_x), fill=tick_color, font=label_font)

    for y in range(center_y - (center_y // tick_interval) * tick_interval, height, tick_interval):
        if y != center_y:  # Пропустить центр, чтобы не дублировать деление
            draw.line([(center_x - tick_length, y), (center_x + tick_length, y)], fill=tick_color, width=axis_width)
            draw.text((center_x + tick_length + 2, y - 7), str(center_y - y), fill=tick_color, font=label_font)

    # Обозначение осей
    draw.text((center_x + 10, center_y - 20), 'Y', fill=axis_color, font=label_font)
    draw.text((width - 30, center_y + 10), 'X', fill=axis_color, font=label_font)
