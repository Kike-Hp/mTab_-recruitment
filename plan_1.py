import service

class Main():
    def __init__(self):
        self.service = service.Service('http://allegro.pl')
        self.title = 'Allegro.pl – najlepsze ceny, największy wybór i zawsze bezpieczne zakupy online'

    def start(self):
        if self.service.getTitle() != self.title:
            return False
        if self.service.getFindElementbySelector("div._3kk7b._vnd3k._1h8s6._13prn._12isx._kiiea._oeb1x").click():
            pass
        self.search()
        return self.condition()

    def search(self):
        self.search = self.service.getFindElementbyName("string")
        self.search.send_keys("rower")
        self.service.getAkcept(self.search)
        self.number_all_auctions = self.service.getFindElementbySelector("div._lsy4e._1hs1x._1ue2y._1t9p2._1h7wt._15mod._1vryf._1yfhn._3db39_1ZtAT._7ccvy").text.split()[-2]
        self.first_bicycle = self.service.getFindElementbySelector("div.bf8839e").text
        print("price first bicycle: ", self.first_bicycle)
        print("number of auctions per page: ", len(self.service.getFindElementsbySelector("div.bf8839e")))
        print("number of all auctions: ", self.number_all_auctions)

    def condition(self):
        self.prince_in_gr = self.first_bicycle.split()[0].split(',')
        print((int(self.prince_in_gr[0]) * 100) + int(self.prince_in_gr[1]))
        if ((int(self.prince_in_gr[0]) * 100) + int(self.prince_in_gr[1])) > int(self.number_all_auctions):
            return True
        else:
            return False