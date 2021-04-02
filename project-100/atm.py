class Atm(object):
    def __init__(self,cardnumder,pinnumber,moneybalance,cashwithdraw):
        self.cardnumder = cardnumder
        self.pinnumber = pinnumber
        self.moneybalance = moneybalance
        self.cashwithdraw = cashwithdraw

    def gettingbalance(self):
        print("geting balance of the account")

    def start(self):
        print("started counting")

    def stop(self):
        print("stop counting")

    def gettingMoney(self):
        print("getting Money out")

varun = Atm("1234567890","12345",10000,1000)
print("Card number : "+varun.cardnumder,",","Pin number : "+varun.pinnumber)
