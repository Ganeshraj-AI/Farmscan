from PIL import Image
from local_model import analyze_crop_image_local

img = Image.open(
    r"C:\Users\Ganesh\Downloads\farmscan_fixed\farmscan_fixed\dataset\Healthy\fb084c48-8c42-43a1-8193-191ba873bd2d___GH_HL Leaf 514.1.JPG"
).convert("RGB")

result = analyze_crop_image_local(img)
print(result)
