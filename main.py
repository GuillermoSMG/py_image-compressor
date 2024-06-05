import os
import shutil
from PIL import Image


downloads_folder = f"{os.getcwd()}/toCompress/"
output_folder = f"{os.getcwd()}/compressed/"
already_compressed_folder = f"{os.getcwd()}/alreadyCompressed/"

os.makedirs(output_folder, exist_ok=True)
os.makedirs(already_compressed_folder, exist_ok=True)

if __name__ == '__main__':
    amount = 0
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        amount += 1
        name, extension = os.path.splitext(file_path)
        if extension.lower() in ['.jpg', '.jpeg', '.png', '.webp']:
            picture = Image.open(downloads_folder + filename)
            picture.save(output_folder +
                         f"compressed_{filename}", optimize=True, quality=60)
            ruta_actual_completa = os.path.join(downloads_folder, filename)
            ruta_destino_completa = os.path.join(
                already_compressed_folder, filename)
            shutil.move(ruta_actual_completa, ruta_destino_completa)
    print(f'Se ha/n comprimido {amount} elemento/s.')
