from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"
path_out = "./new_imgs"


for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)#.convert("L")

    # contrast
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{path_out}/{clean_name}_edited.png")