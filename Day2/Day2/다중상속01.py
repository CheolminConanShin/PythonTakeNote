class Tiger:
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")
    def Cry(self):
        print("호랑이 어흥")

class Lion:
    def Bite(self):
        print("사자처럼 한입에 꿀꺽하기")
    def Cry(self):
        print("사자 으르릉")

class Liger(Tiger, Lion):
    def Play(self):
        print("라이거만의 사육사와 재미있게 놀기")

l = Liger()
l.Jump() #호랑이처럼 멀리 점프하기 출력
l.Play() #라이거만의 사육사와 재미있게 놀기 출력
l.Cry() #호랑이 어흥 출력
print("mro순서: ", Liger.__mro__)
#mro순서:  (<class '__main__.Liger'>, <class '__main__.Tiger'>, <class '__main__.Lion'>, <class 'object'>)