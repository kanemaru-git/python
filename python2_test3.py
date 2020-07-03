# 画像の高さ
def height(image):
    return image.height

# 画像の横幅
def width(image):
    return image.width

# 画像のアスペクト比
def aspect(image):
    return image.height / image.width

# Pillowをインポート
from PIL import Image, ImageFilter
image = Image.open('../images/img.jpg')

# 高さ、横幅、アスペクト比を出力
print("画像の高さは",height(image),"pxです。")
print("画像の横幅は",width(image),"pxです。")
print("画像のアスペクト比は",aspect(image),"%です。")