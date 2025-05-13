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
    
    for y in range(height-1, -1, -1):
        for x in range(width-1, -1, -1):
            pixel_value = image_b_gray[y, x]
            lsb = pixel_value & 0b111  # 拿B圖最低三位
            
            if lsb == 0: # 左
                orig_x = (x - step) % width
                orig_y = y
            elif lsb == 1: # 上
                orig_x = x
                orig_y = (y - step) % height
            elif lsb == 2: # 右
                orig_x = (x + step) % width
                orig_y = y
            elif lsb == 3: # 下
                orig_x = x
                orig_y = (y + step) % height
            elif lsb == 4:  # 左上
                orig_x = (x - step) % width
                orig_y = (y - step) % height
            elif lsb == 5:  # 右上
                orig_x = (x + step) % width
                orig_y = (y - step) % height
            elif lsb == 6:  # 左下
                orig_x = (x - step) % width
                orig_y = (y + step) % height
            else:  # 右下
                orig_x = (x + step) % width
                orig_y = (y + step) % height
            
            #交換pixel 
            swapped_image[y, x], swapped_image[orig_y, orig_x] = swapped_image[orig_y, orig_x].copy(), swapped_image[y, x].copy()
    
    return swapped_image

#用圖B最低3位元反推原圖
image_a_path = 'hidden_image.png'
image_b_path = './imgs/raputa.png'
output_path = 'origin_image.png'

image_a, image_b_resized = load_and_resize_images(image_a_path, image_b_path)
swapped_image = swap_pixels(image_a, image_b_resized, 300)

cv2.imwrite(output_path, swapped_image)
print(f"Save to {output_path}")