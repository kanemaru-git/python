# Pillowをインポート
from PIL import Image, ImageFilter

# 画像の情報を表示する関数
def image_infomation(image):
    print("画像の高さは{}pxです。".format(image.height))
    print("画像の横幅は{}pxです。".format(image.width))
    print("画像のアスペクト比は{:.2f}:1です。".format(image.width / image.height))

# 画像を選択
image = Image.open('../images/img.jpg')

# 画像の情報を出力
image_infomation(image)
