from pytube import YouTube
import requests
from io import BytesIO
from PIL import Image
import os

def download_thumbnail(video_id, output_folder='/workspaces/vscode-remote-try-python/thumbnail'):
    try:
        # Buat URL video berdasarkan ID
        video_url = f'https://www.youtube.com/watch?v={video_id}'

        # Ambil objek YouTube
        yt = YouTube(video_url)

        # Dapatkan URL thumbnail
        thumbnail_url = yt.thumbnail_url

        # Unduh thumbnail menggunakan requests
        response = requests.get(thumbnail_url)
        thumbnail_data = BytesIO(response.content)

        # Periksa apakah folder penyimpanan sudah ada, jika tidak, buat folder baru
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Ubah nama file berdasarkan ID video
        output_path = os.path.join(output_folder, f'{video_id}.jpg')

        # Simpan thumbnail sebagai file gambar
        img = Image.open(thumbnail_data)
        img.save(output_path)

        print(f'Thumbnail berhasil diunduh ke: {output_path}')

    except Exception as e:
        print(f'Error: {e}')

# Ganti 'VIDEO_ID1', 'VIDEO_ID2', dll. dengan ID video yang sesuai
video_ids = [
        'd3UTywBDSW4',
        ]

for video_id in video_ids:
    download_thumbnail(video_id)
