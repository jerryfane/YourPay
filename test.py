
#######################################################
#                                                     #
#  Questo programma serve a tener conto dei pagamenti #
#  effettuatti dall'utente. Una specie di conto excel #
#  dove l'utente potrÃ  interagire tramite Telegram    #
#  e tenere sempre aggiornati tutti i suoi conti.     #
#                                                     #
#######################################################
import json
from collections import OrderedDict

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

    def create_account(self, lists):
        lists.sort()
        for i in range(int(len(lists))):
            account_name = lists[i][0]
            balance = lists[i][1]
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
        current_object['account'] = account_name.lower().capitalize()
        current_object['category'] = category.lower().capitalize()
        current_object['comment'] = comment

        #Aggiorno il balance del conto utilizzato
        #quando l'utente usa i soldi del suo account, dovrÃ  inserire un numero positivo
        #che verrÃ  sottratto dal balance attuale
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
            #print(i, 'Saldo:', self.get_balance(i))
            x = [i, self.get_balance(i)]
            accounts_list.append(x)
        return accounts_list
    
    def get_accounts_list(self):
        accounts_list = list(self.accounts.keys())
        return accounts_list

    def get_amount_by_category_date(self, category, initial_date):
        total_amount = 0
        for i in self.datas:
            current_object = self.datas[i]
            if current_object['date'] == initial_date or current_object['date'] > initial_date:
                if current_object['category'] == category:
                    total_amount += current_object['amount']
        return total_amount

    def get_total_spent(self):
        total_spent = 0
        for i in self.datas:
            if self.datas[i]['category'] != "Giroconto" and self.datas[i]['amount'] > 0:
                total_spent += self.datas[i]['amount']
        return total_spent

    def get_total_balance(self):
        accounts = self.get_accounts()
        total_balance = 0
        for i in accounts:
            balance = i[1]
            total_balance += balance
        return total_balance

    def get_amount_by_month_year(self, month, year):
        total_amount = 0
        for i in self.datas:
            current_object = self.datas[i]
            object_month = current_object['date'].split('/')[1]
            object_year = current_object['date'].split('/')[2]
            if object_month == month and object_year == year:
                total_amount += current_object['amount']
        return total_amount

    def get_category_list(self):
        category_list = []
        for i in self.datas:
            category = self.datas[i]['category'].lower().capitalize()
            if category in category_list:
                pass
            else:
                category_list.append(category)
        return category_list

    def get_first_date(self):
        if len(self.datas) == 0:
            return ''
        else:
            first_date = self.datas[0]['date']
            return first_date

    def get_rows(self, date):
        return self.datas[date]

    def get_all_rows(self):
        ordered_datas = self.reorder_datas()
        return ordered_datas

    def remove_row(self, row_id):
        self.datas.pop(row_id)

    def reorder_datas(self):
        ordered_datas = OrderedDict(sorted(self.datas.items(), key=lambda x: x[1]['date']))
        return ordered_datas

    #convert the Class to a JSON string (str type)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=False)

    def loadJSON(self, dictionary, change_balance):
        #recreate accounts
        accounts = dictionary['accounts']
        accounts_list = []
        for e, i in enumerate(accounts):
            accounts_list.append([i, round(accounts[i]['balance'],2)])
        accounts_list.sort()
        self.create_account(accounts_list)
        #readd rows
        datas = dictionary['datas']
        #start reordering rows by date
        for i in datas:
            try:
                int(datas[i]['date'][0])
            except:
                datas[i]['date'] = datas[i]['date'][1:]
        datas = OrderedDict(sorted(datas.items(), key=lambda x: x[1]['date']))
        #here I finished reordering rows
        for i in datas:
            date = datas[i]['date']
            amount = datas[i]['amount']
            account_name = datas[i]['account']
            category = datas[i]['category']
            comment = datas[i]['comment']
            self.new_row(date, amount, account_name, category, comment, change_balance)
        return ''
