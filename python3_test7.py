# abcモジュールをインポート
from abc import ABCMeta,abstractclassmethod

# 乗り物抽象クラス
class Vehicle(metaclass = ABCMeta):

    def __init__(self,forward_movement):
        self.forward_movement = forward_movement

    @abstractclassmethod
    def forward(self):
        pass

# 自動車クラス
class car(Vehicle):
    def forward(self):
        print("自動車は" + self.forward_movement + "と進みます。")

# 自転車クラス
class bicycle(Vehicle):
    def forward(self):
        print("自転車は" + self.forward_movement + "と進みます。")

# 船クラス
class ship(Vehicle):
    def forward(self):
        print("船は" + self.forward_movement + "と進みます。")

# 飛行機クラス
class airplane(Vehicle):
    def forward(self):
        print("飛行機は" + self.forward_movement + "と進みます。")

# インスタンス
car = car("アクセルを踏む")
bicycle = bicycle("ペダルを漕ぐ")
ship = ship("スクリューを回す")
airplane = airplane("プロペラを回す")

# メソッド呼び出し
car.forward()
bicycle.forward()
ship.forward()
airplane.forward()