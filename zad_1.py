import service

class Main():
    def __init__(self):
        self.service = service.Service('http://allegro.pl')
        self.title = 'Allegro.pl – najlepsze ceny, największy wybór i zawsze bezpieczne zakupy online'
        self.serch_item = 'rower'

    def start(self):
        if self.service.getTitle() != self.title:
            return False
        if self.service.getFindElementbySelector("div._4f735_Ag0om._ur8qq > div > div._3kk7b._vnd3k._1h8s6._13prn._12isx._kiiea._oeb1x > button").click():
            pass
        self.getSearch()
        self.service.sesionClose()
        return True

    def getSearch(self):
        self.look_for = self.service.getFindElementbyName("string")
        self.look_for.send_keys(self.serch_item)
        self.service.getAkcept(self.look_for)