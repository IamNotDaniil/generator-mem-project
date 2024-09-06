from PIL import Image, ImageDraw, ImageFont

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = int(input("Введите номер картинки: "))

if image_number == 1:
    image_file = "Кот в ресторане.png"
elif image_number == 2:
    image_file = "Кот в очках.png"
else:
    print("Неверный номер картинки.")
    exit()

try:
    image = Image.open(image_file)
except FileNotFoundError:
    print("Файл изображения не найден. Убедитесь, что картинка существует.")
    exit()

draw = ImageDraw.Draw(image)

top_text = input("Введите верхний текст мема: ")
bottom_text = input("Введите нижний текст мема: ")

try:
    font = ImageFont.truetype("arial.ttf", size=50)
except IOError:
    font = ImageFont.load_default()

width, height = image.size

top_text_size = draw.textbbox((0, 0), top_text, font=font)
bottom_text_size = draw.textbbox((0, 0), bottom_text, font=font)

top_text_x = (width - (top_text_size[2] - top_text_size[0])) / 2
top_text_y = 10
bottom_text_x = (width - (bottom_text_size[2] - bottom_text_size[0])) / 2
bottom_text_y = height - (bottom_text_size[3] - bottom_text_size[1]) - 10

draw.text((top_text_x, top_text_y), top_text, font=font, fill="black")
draw.text((bottom_text_x, bottom_text_y), bottom_text, font=font, fill="black")

new_image_file = "new_meme.jpg"
image.save(new_image_file)

print(f"Мем сохранен как {new_image_file}")
