
class person:
    
    """ Описание человаека """
    def __init__(self, name):
        """Конструктор"""
        self.name = name
        self.is_alive = True
        self.opoznan = True

    def kto_takoi(self):
        if self.is_alive == True:
            print(self.name + " всё ещё жив(а)!")
        else:
            print(self.name + " мёртв(а)!")
            if self.opoznan == True:
                print("опознать возможно")
            else:
                print("невозможно опознать")

    def izmenenie_imeni(self, name):
        self.name = name

    def ne_opoznan(self):
        self.opoznan = False

    def ubit(self):
        self.is_alive = False
   



