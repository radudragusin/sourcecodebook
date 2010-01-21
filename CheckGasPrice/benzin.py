from HTMLParser import HTMLParser

class extractFuelPrice(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.ok = False
	self.price95 = 100
        self.data = []
    def handle_starttag(self,tag,attrs):
        if tag == 'div':
            for name,value in attrs:
                if name == 'class' and value == 'productgroup petrol':
                    self.ok = True
        else:
            self.ok = False
    def handle_data(self,data):
        data = data.strip()
        if self.ok and len(data)>=4:
            self.data.append(data)
    def close(self):
        self.price95 = float(self.data[3].replace(",","."))

if __name__ == "__main__":
    from urllib2 import urlopen
    jet = urlopen("http://jet.dk")
    #q8 = urlopen("http://q8.dk/Priser/Prisliste.aspx")
    jet_data = jet.read()
    #q8_data = q8.read()
    e = extractFuelPrice()
    charset = jet.info().getparam("charset")
    e.feed(jet_data.decode(charset))
    e.close()
    print "Data = ", e.data
    print "Benzina 95 = ", e.price95

