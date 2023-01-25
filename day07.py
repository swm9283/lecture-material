# class

#class 생성
class Pokemon:
    def __init__(self,name, owner, skills):
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 {name} 생성됨.")
    def info(self):
        print(f"{self.owner}의 포켓몬은 {self.name}입니다.")
        print(f"{self.name}이 구사할 수 있는 스킬은")
        for skill in self.skills:
            print(skill)

p1 = Pokemon("피카츄","한지우","50만볼트/100만 볼트/번개")
p2 = Pokemon("꼬부기","오바람","고속스핀/거품/몸통박치기/하이드로펌프")

p1.info()
p2.info()

# inheritance(상속)
class Pikachu(Pokemon):
    pass

pi1 = Pikachu("피카츄","덴트","번개")
pi1.info()

















