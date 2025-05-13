from PIL import Image
import numpy as np

def reveal_image(hidden_image_path, output_path):
    # 讀取隱藏了圖片 A 的圖片
    hidden_img = Image.open(hidden_image_path)
    
    # 轉換成 numpy 數組
    hidden_array = np.array(hidden_img)
    
    # 將 B 圖片中的隱藏部分提取出來
    # 使用 & 0x0F 提取低 4 位，然後左移 4 位恢復原本的圖像數據
    revealed_array = (hidden_array & 0x03) << 6
    
    # 轉換回圖片
    revealed_img = Image.fromarray(revealed_array)
    
    # 保存解密出的圖片 A
    revealed_img.save(output_path)
    print(f"圖片 A 已成功從隱藏圖片中解密，結果保存為 {output_path}")

# 調用函數來解密出圖片 A
hidden_image_path = './imgs/hidden_img.png'
revealed_output_path = './imgs/revealed_img.png'

reveal_image(hidden_image_path, revealed_output_path)