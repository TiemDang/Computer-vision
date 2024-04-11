import os
import pygame

def play_music_from_folder(folder_path):
    # Khởi tạo Pygame Mixer
    pygame.mixer.init()
    folder_path="F:/Voice_Vr"

    # Lặp qua các file trong thư mục và phát nhạc
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp3'):
            music_path = os.path.join(folder_path, file_name)
            print(f"Đang phát nhạc: {music_path}")
            pygame.mixer.music.load(music_path)
            pygame.mixer.music.play()

            # Chờ cho đến khi nhạc kết thúc
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

# Đường dẫn đến thư mục chứa nhạc của bạn
folder_path = 'duong_dan_thu_muc_chua_nhac'

# Phát nhạc từ thư mục
play_music_from_folder(folder_path)
