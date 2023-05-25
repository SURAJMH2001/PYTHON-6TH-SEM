class Bank():
    def _init_(self,bank,country):
        self.bank=bank
        self.country=country
    def displbank(self):
        print(f"bank name is {self.bank} and country is {self.country}")
        
class Branch(Bank):
    def _init_(self,state,branchName,total,bank,country):
        super()._init_(bank,country)
        self.state=state
        self.branchName=branchName
        self.__total=total
    def display(self):
        print(f"the state is {self.state} and branch is {self.branchName}")
        print(Bank.displaybank())
        
    def showtotal(self):
        print(f"total is {self.total}")
        
    def increment(self,x):
        self._total=self._total+x
        
class account(Bank):
    def _init_(self,accName,accId,balance,state,branchName,total,bank,country):
        super()._init_(self,state,branchName,total,bank,country)
        self.accName=accName
        self.accId=accId
        self.__balance=balance
    def credit(self,y):
        self.balance=self.balance+y
    def debit(self,y):
         self.balance=self.balance-y