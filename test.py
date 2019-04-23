
#######################################################
#                                                     #
#  Questo programma serve a tener conto dei pagamenti #
#  effettuatti dall'utente. Una specie di conto excel #
#  dove l'utente potrà interagire tramite Telegram    #
#  e tenere sempre aggiornati tutti i suoi conti.     #
#                                                     #
#######################################################
import json

class Account:
    def __init__(self, name, account_number):
        self.name = name #nome dell'utente
        self.account_number = account_number #numero dei conti che l'utente vuole attivare
        self.datas = {}
        self.accounts = {}

        '''
        for i in range(self.account_number):
            account_name = input('Name of the account #'+str(i)+': ')
            self.accounts[account_name] = {}
            self.accounts[account_name]['balance'] = float(input("What's the current balance of this account? "))
        '''

    def create_account(self, list):
        for i in range(int(len(list))):
            account_name = list[i][0]
            balance = list[i][1]
            self.accounts[account_name] = {}
            self.accounts[account_name]['balance'] = float(balance)
        self.account_number = len(self.accounts)

    def new_row(self, date, amount, account_name, category, comment, change_balance):
        #prendo l'id del dato da introdurre nella data odierna
        if len(self.datas) == 0:
            current_key = 0
        else:
            for i in self.datas:
                last_key = i
            current_key = last_key + 1

        #inizio a introdurrre i dati
        self.datas[current_key] = {}
        current_object = self.datas[current_key]
        current_object['date'] = date
        current_object['amount'] = amount
        current_object['account'] = account_name
        current_object['category'] = category
        current_object['comment'] = comment

        #Aggiorno il balance del conto utilizzato
        #quando l'utente usa i soldi del suo account, dovrà inserire un numero positivo
        #che verrà sottratto dal balance attuale
        if change_balance:
            self.accounts[account_name]['balance'] -= amount
        if self.accounts[account_name]['balance'] < 0:
            print('Warning: the balance of this account is below 0')

        print('I dati sono stati salvati correttamente')

    def get_balance(self, account_name):
        return self.accounts[account_name]['balance']

    def get_accounts(self): #Mostra la lista di tutti i conti creati
        accounts_list = []
        for i in self.accounts.keys():
            print(i, 'Saldo:', self.get_balance(i))
            x = [i, self.get_balance(i)]
            accounts_list.append(x)
        return accounts_list

    def get_amount_by_category_date(self, category, initial_date):
        total_amount = 0
        for i in self.datas:
            current_object = self.datas[i]
            if current_object['date'] == initial_date or current_object['date'] > initial_date:
                if current_object['category'] == category:
                    total_amount += current_object['amount']
        return total_amount

    def get_amount_by_month_year(self, month, year):
        total_amount = 0
        for i in self.datas:
            current_object = self.datas[i]
            object_month = current_object['date'].split('/')[1]
            object_year = current_object['date'].split('/')[2]
            if object_month == month and object_year == year:
                total_amount += current_object['amount']
        return total_amount

    def get_rows(self, date):
        return self.datas[date]

    def get_all_rows(self):
        return self.datas

    def remove_row(self, row_id):
        self.datas.pop(row_id)

    #convert the Class to a JSON string (str type)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=False)

    def loadJSON(self, dictionary, change_balance):
        #recreate accounts
        accounts = dictionary['accounts']
        accounts_list = []
        for e, i in enumerate(accounts):
            accounts_list.append([i, accounts[i]['balance']])
        self.create_account(accounts_list)
        #readd rows
        datas = dictionary['datas']
        for i in datas:
            date = datas[i]['date']
            amount = datas[i]['amount']
            account_name = datas[i]['account']
            category = datas[i]['category']
            comment = datas[i]['comment']
            self.new_row(date, amount, account_name, category, comment, change_balance)
        return ''

#obj = json.loads(Jerry.toJSON())
