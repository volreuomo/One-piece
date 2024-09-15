from PIL import Image


def conv_rgba_to_rgb(file: str) -> Image.Image:
    rgba = Image.open(file)
    rgb = Image.new("RGB", rgba.size, (255, 255, 255))
    rgb.paste(rgba)
    return rgb
