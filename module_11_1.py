import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

# 1. NumPy: Создание массива чисел и выполнение операций

array = np.arange(10)
print(f"Массив: {array}")
array_doubled = array * 2
print(f"Массив, умноженный на 2: {array_doubled}")
array_sin = np.sin(array)
print(f"Синус значений массива: {array_sin}")

# 2. Matplotlib: Визуализация данных

plt.plot(array, array_sin, label="sin(x)")
plt.title("График функции sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()

# 3. Pillow: Обработка изображения

image = Image.open('sample_image.jpg')
blurred_image = image.filter(ImageFilter.BLUR)
resized_image = blurred_image.resize((300, 300))
resized_image.save('blurred_resized_image.png')
print("Изображение обработано и сохранено.")
