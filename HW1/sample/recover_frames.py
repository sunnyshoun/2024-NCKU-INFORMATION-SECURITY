import cv2
import os
import numpy as np

def recover_frames_to_mp4(image_folder, output_video_path, fps=30):
    # 取得圖片序列的所有文件名
    images = [img for img in sorted(os.listdir(image_folder)) if img.endswith(".png")]
    
    if not images:
        print("圖片序列文件夾中沒有 PNG 文件！")
        return
    
    # 讀取第一幀圖片，來獲取圖片尺寸
    first_frame_path = os.path.join(image_folder, images[0])
    first_frame = cv2.imread(first_frame_path)
    height, width = first_frame.shape[:2]

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), isColor = False)

    # 讀取每一張圖片並寫入影片
    for image in images:
        image_path = os.path.join(image_folder, image)
        frame = cv2.imread(image_path)
        recover_frame = (frame[:, :, 0] & 0x03) << 6
        out.write(recover_frame.astype(np.uint8))

    out.release()
    print(f"影片已成功保存為 {output_video_path}")

# 調用函數來將圖片序列生成影片
image_folder = 'hidden_video_frames'
output_video_path = 'recover_video.mp4'

recover_frames_to_mp4(image_folder, output_video_path, 30)
