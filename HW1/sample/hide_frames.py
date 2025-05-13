import cv2
import numpy as np
import os

def hide_video_to_frames(video_A_path, video_B_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 打開影片 A 和 B
    cap_A = cv2.VideoCapture(video_A_path)
    cap_B = cv2.VideoCapture(video_B_path)
    
    frame_count = 0
    
    while True:
        ret_B, frame_B = cap_B.read()
        ret_A, frame_A = cap_A.read()

        if not ret_B:  # 如果影片 B 沒有更多幀，結束處理
            break

        if ret_A:  # 影片 A 還有幀
            # 將 A 幀轉換為灰度黑白圖像，確保是單通道
            frame_A = cv2.cvtColor(frame_A, cv2.COLOR_BGR2GRAY)
            frame_A = cv2.resize(frame_A, (frame_B.shape[1], frame_B.shape[0]))
            grayscale_data = (frame_A[:, :] >> 6) & 0x03
            frame_B[:, :, 0] = (frame_B[:, :, 0] & 0xFC) | grayscale_data
            new_frame = frame_B
        else:
            # 影片 A 已無更多幀，只處理影片 B 的幀
            new_frame = frame_B

        # 將每一幀保存為 PNG 圖片
        output_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(output_filename, new_frame)

        frame_count += 1

    # 釋放資源
    cap_A.release()
    cap_B.release()
    print(f"影片 A 的幀已成功隱藏在影片 B 中，並保存為 PNG 圖片序列在文件夾：{output_folder}")
    
video_A_path = './videos/bad_apple.mp4'
video_B_path = './videos/raputa.mp4'
output_folder = 'hidden_video_frames'

hide_video_to_frames(video_A_path, video_B_path, output_folder)
