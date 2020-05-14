class Jason_V:
    """Создание Джейсона"""
    def __init__(self, mask, knife):
        self.mask = mask
        self.knife = knife
    def go_hunt(self):
        print("""Снова наступила пятница 13 и на дне озера ото сна пробуждается тот, 
кому лучше было не просыпаться...""")
        print("На нём " + self.mask + ", а в руках у него " + self.knife)
        print("Горе тому путнику, кто попадётся ему на глаза...\nИгра начинается!")


if __name__ == "__main__":
    Jason = Jason_V("хоккейная маска", "мачете")
    Jason.go_hunt()
