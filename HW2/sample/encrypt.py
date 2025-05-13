import cv2
import numpy as np

def load_and_resize_images(image_a_path, image_b_path):
    image_a = cv2.imread(image_a_path, cv2.IMREAD_COLOR)
    if image_a is None:
        raise ValueError(f"无法加载图像 A: {image_a_path}")
    
    image_b = cv2.imread(image_b_path, cv2.IMREAD_COLOR)
    if image_b is None:
        raise ValueError(f"无法加载图像 B: {image_b_path}")
    
    image_b_resized = cv2.resize(image_b, (image_a.shape[1], image_a.shape[0]), interpolation=cv2.INTER_AREA)
    
    return image_a, image_b_resized

def swap_pixels(image_a, image_b, step = 100):
    image_b_gray = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)
    height, width = image_a.shape[:2]
    swapped_image = image_a.copy()
    
    for y in range(height):
        for x in range(width):
            pixel_value = image_b_gray[y, x]
            lsb = pixel_value & 0b111  # 拿B圖最低三位
            
            if lsb == 0: # 左
                new_x = (x - step) % width
                new_y = y
            elif lsb == 1: # 上
                new_x = x
                new_y = (y - step) % height
            elif lsb == 2: # 右
                new_x = (x + step) % width
                new_y = y
            elif lsb == 3: # 下
                new_x = x
                new_y = (y + step) % height
            elif lsb == 4:  # 左上
                new_x = (x - step) % width
                new_y = (y - step) % height
            elif lsb == 5:  # 右上
                new_x = (x + step) % width
                new_y = (y - step) % height
            elif lsb == 6:  # 左下
                new_x = (x - step) % width
                new_y = (y + step) % height
            else:  # 右下
                new_x = (x + step) % width
                new_y = (y + step) % height
              
            swapped_image[y, x], swapped_image[new_y, new_x] = swapped_image[new_y, new_x].copy(), swapped_image[y, x].copy()
    
    return swapped_image

#要隱藏的圖A，用圖B最低3位元隱藏
image_a_path = './imgs/bad_apple.png'
image_b_path = './imgs/raputa.png'
output_path = 'hidden_image.png'

image_a, image_b_resized = load_and_resize_images(image_a_path, image_b_path)

swapped_image = swap_pixels(image_a, image_b_resized, 300)

cv2.imwrite(output_path, swapped_image)
print(f"Save to {output_path}")