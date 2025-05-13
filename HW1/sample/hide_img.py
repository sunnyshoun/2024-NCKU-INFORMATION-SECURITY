from PIL import Image
import numpy as np

def hide_image(A_path, B_path, output_path):
    # 讀取圖片 A 和 B
    img_A = Image.open(A_path)
    img_B = Image.open(B_path)
    
    if img_A.mode != 'RGB':
        img_A = img_A.convert('RGB')
    if img_B.mode != 'RGB':
        img_B = img_B.convert('RGB')
        
    # 確保圖片 A 的大小與 B 一樣
    img_A = img_A.resize(img_B.size)
    
    # 轉換成 numpy 數組
    array_A = np.array(img_A)
    array_B = np.array(img_B)
    
    # 將 A 圖片的數據存儲到 B 圖片中
    # 保留 B 的高 4 位，並使用 A 的高 4 位來隱藏圖片
    new_array = (array_B & 0xFC) | (array_A >> 6)
    
    # 轉換回圖片
    hidden_img = Image.fromarray(new_array)
    
    # 保存結果圖片
    hidden_img.save(output_path)
    print(f"圖片 A 已成功隱藏在圖片 B 中，結果保存為 {output_path}")

# 調用函數
A_path = './imgs/bad_apple.png'
B_path = './imgs/raputa.png'
output_path = './imgs/hidden_img.png'

hide_image(A_path, B_path, output_path)