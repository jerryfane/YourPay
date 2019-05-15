import matplotlib.pyplot as plt

class Stats:
    def __init__(self, Account):
        self.Account = Account
    
    def get_month_from_number(self, number):
        months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', \
                  6: 'June', 7: 'July', 8: 'August', 9: 'September', \
                  10: 'October', 11: 'November', 12: 'December'}
        return months[number]
    
    def get_date_amount_per_account(self, account):
        dictionary = {}
        for i in self.Account.datas:
            if self.Account.datas[i]['account'] == account:
                date = self.Account.datas[i]['date']
                amount = self.Account.datas[i]['amount']
                if date not in dictionary:
                    dictionary[date] = amount
                else:
                    dictionary[date] += amount
        return dictionary
    
    def get_date_amount_per_category(self, category):
        dictionary = {}
        for i in self.Account.datas:
            if self.Account.datas[i]['category'] == category:
                date = self.Account.datas[i]['date']
                amount = self.Account.datas[i]['amount']
                if date not in dictionary:
                    dictionary[date] = amount
                else:
                    dictionary[date] += amount
        return dictionary
    
    def get_account_initial_balance(self, account):
        account_dictionary = self.get_date_amount_per_account(account)
        current_balance = self.Account.get_balance(account)
        initial_balance = current_balance
        for i in account_dictionary:
            amount = account_dictionary[i]
            initial_balance += amount
        return initial_balance
    
    def get_total_date_amount(self):
        dictionary = {}
        for i in self.Account.datas:
            date = self.Account.datas[i]['date']
            amount = self.Account.datas[i]['amount']
            if date not in dictionary:
                dictionary[date] = amount
            else:
                dictionary[date] += amount
                dictionary[date] = round(float(dictionary[date]), 2)
        return dictionary
    
    def get_total_month_amount(self):
        total_date_amount = self.get_total_date_amount()
        dictionary = {}
        for date in total_date_amount:
            amount = total_date_amount[date]
            month_num = date.split('-')[1]
            month_string = self.get_month_from_number(int(month_num))
            if month_string not in dictionary:
                dictionary[month_string] = amount
            else:
                dictionary[month_string] += amount
                dictionary[month_string] = round(float(dictionary[month_string]), 2)
        return dictionary         
          
    def get_total_initial_balance(self):
        total_dictionary = self.get_total_date_amount()
        current_balance = self.Account.get_total_balance()
        initial_balance = current_balance
        for i in total_dictionary:
            amount = total_dictionary[i]
            initial_balance += amount
        return initial_balance
    
    def get_total_amount_spent_perday(self):
        total_dictionary = self.get_total_date_amount()
        list_date = []
        list_amount = []
        for i in total_dictionary:
            list_date.append(i)
            amount = total_dictionary[i]
            list_amount.append(amount)
        return list_date, list_amount
    
    def get_total_amount_spent_permonth(self):
        total_dictionary = self.get_total_month_amount()
        list_month = []
        list_amount = []
        for month in total_dictionary:
            list_month.append(month)
            amount = total_dictionary[month]
            list_amount.append(amount)
        return list_month, list_amount
    
    def get_amount_spent_perday_account(self, account):
        account_dictionary = self.get_date_amount_per_account(account)
        list_date = []
        list_amount = []
        for i in account_dictionary:
            list_date.append(i)
            amount = account_dictionary[i]
            list_amount.append(amount)
        return list_date, list_amount
    
    def get_amount_spent_perday_category(self, category):
        category_dictionary = self.get_date_amount_per_category(category)
        list_date = []
        list_amount = []
        for date in category_dictionary:
            list_date.append(date)
            amount = category_dictionary[date]
            list_amount.append(amount)
        return list_date, list_amount
    
    def get_month_amount_spent_per_account(self, account):
        account_dictionary = self.get_date_amount_per_account(account)
        dictionary = {}
        for date in account_dictionary:
            month = date.split('-')[1]
            amount = account_dictionary[date]
            if month not in dictionary:
                dictionary[month] = amount
            else:
                dictionary[month] += amount
                dictionary[month] = round(float(dictionary[month]), 2)
        return dictionary
    
    def get_month_amount_spent_per_category(self, category):
        category_dictionary = self.get_date_amount_per_category(category)
        dictionary = {}
        for date in category_dictionary:
            month_num = date.split('-')[1]
            month_string = self.get_month_from_number(int(month_num))
            amount = category_dictionary[date]
            if month_string not in dictionary:
                dictionary[month_string] = amount
            else:
                dictionary[month_string] += amount
                dictionary[month_string] = round(float(dictionary[month_string]), 2)
        return dictionary
        
    def get_amount_spent_permonth_account(self, account):
        month_dictionary = self.get_month_amount_spent_per_account(account)
        list_month_num = list(month_dictionary.keys())
        list_amount = list(month_dictionary.values())
        list_month = []
        for month in list_month_num:
            month_string = self.get_month_from_number(int(month))
            list_month.append(month_string)
        return list_month, list_amount
    
    def get_amount_spent_permonth_category(self, category):
        month_dictionary = self.get_month_amount_spent_per_category(category)
        list_month = []
        list_amount = []
        for month in month_dictionary:
            list_month.append(month)
            amount = month_dictionary[month]
            list_amount.append(amount)
        return list_month, list_amount
    
    def get_balance_permonth_account(self, account):
        month_dictionary = self.get_month_amount_spent_per_account(account)
        initial_balance = self.get_account_initial_balance(account)
        list_month_num = list(month_dictionary.keys())
        list_month = []
        for month in list_month_num:
            month_string = self.get_month_from_number(int(month))
            list_month.append(month_string)
        list_balance = []
        balance = initial_balance
        for i in month_dictionary:
            amount = month_dictionary[i]
            balance -= amount
            list_balance.append(balance)
        return list_month, list_balance
    
    def get_total_balance_permonth(self):
        month_dictionary = self.get_total_month_amount()
        initial_balance = self.get_total_initial_balance()
        list_month = []
        list_balance = []
        balance = initial_balance
        for month in month_dictionary:
            list_month.append(month)
            amount = month_dictionary[month]
            balance -= amount
            balance = round(float(balance), 2)
            list_balance.append(balance)
        return list_month, list_balance          
        
    def get_balance_perday_account(self, account):
        account_dictionary = self.get_date_amount_per_account(account)
        initial_balance = self.get_account_initial_balance(account)
        list_date = []
        list_balance = []
        balance = initial_balance
        for i in account_dictionary:
            list_date.append(i)
            amount = account_dictionary[i]
            balance -= amount
            list_balance.append(balance)
        return list_date, list_balance
    
    def get_total_balance_perday(self):
        account_dictionary = self.get_total_date_amount()
        initial_balance = self.get_total_initial_balance()
        list_date = []
        list_balance = []
        balance = initial_balance
        for date in account_dictionary:
            list_date.append(date)
            amount = account_dictionary[date]
            balance -= amount
            balance = round(float(balance), 2)
            list_balance.append(balance)
        return list_date, list_balance
    
    def compress_list_date(self, list_date):
        new_list_date = []
        for date in list_date:
            month = date.split('-')[1]
            day = date.split('-')[2]
            new_date = month + '-' + day
            new_list_date.append(new_date)
        return new_list_date 

    def compress_list_amount(self, list_amount):
        new_list_amount = []
        for amount in list_amount:
            new_amount = round(float(amount), 2)
            new_list_amount.append(new_amount)
        return new_list_amount
    
    def chart_total_amount_spent_perday(self):
        title = "Total amount spent per day"
        list_date, list_amount = self.get_total_amount_spent_perday()
        list_date = self.compress_list_date(list_date)
        list_amount = self.compress_list_amount(list_amount)
        color_list = []
        for i in list_amount:
            if i > 0:
                color = '#3983E4' #blue
                color_list.append(color)
            else:
                color = '#4CAF50' #green
                color_list.append(color)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_date, list_amount, color=color_list)
        for index,data in enumerate(list_amount):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig
    
    def chart_total_amount_spent_permonth(self):
        title = "Total amount spent per month"
        list_month, list_amount = self.get_total_amount_spent_permonth()
        list_amount = self.compress_list_amount(list_amount)
        color_list = []
        for i in list_amount:
            if i > 0:
                color = '#3983E4' #blue
                color_list.append(color)
            else:
                color = '#4CAF50' #green
                color_list.append(color)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_month, list_amount, color=color_list)
        for index,data in enumerate(list_amount):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig
    
    def chart_amount_spent_permonth_account(self, account):
        title = account + " amount spent per month"
        list_month, list_amount = self.get_amount_spent_permonth_account(account)
        list_amount = self.compress_list_amount(list_amount)
        color_list = []
        for i in list_amount:
            if i > 0:
                color = '#3983E4' #blue
                color_list.append(color)
            else:
                color = '#4CAF50' #green
                color_list.append(color)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_month, list_amount, color=color_list)
        for index,data in enumerate(list_amount):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig
    
    def chart_amount_spent_permonth_category(self, category):
        title = category + " amount spent per month"
        list_month, list_amount = self.get_amount_spent_permonth_category(category)
        list_amount = self.compress_list_amount(list_amount)
        color_list = []
        for i in list_amount:
            if i > 0:
                color = '#3983E4' #blue
                color_list.append(color)
            else:
                color = '#4CAF50' #green
                color_list.append(color)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_month, list_amount, color=color_list)
        for index,data in enumerate(list_amount):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig
    
    def chart_amount_spent_perday_account(self, account):
        title = account + " amount spent per day"
        list_date, list_amount = self.get_amount_spent_perday_account(account)
        list_date = self.compress_list_date(list_date)
        list_amount = self.compress_list_amount(list_amount)
        color_list = []
        for i in list_amount:
            if i > 0:
                color = '#3983E4' #blue
                color_list.append(color)
            else:
                color = '#4CAF50' #green
                color_list.append(color)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_date, list_amount, color=color_list)
        for index,data in enumerate(list_amount):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig
    
    def chart_amount_spent_perday_category(self, category):
        title = category + " amount spent per day"
        list_date, list_amount = self.get_amount_spent_perday_category(category)
        list_date = self.compress_list_date(list_date)
        list_amount = self.compress_list_amount(list_amount)
        color_list = []
        for i in list_amount:
            if i > 0:
                color = '#3983E4' #blue
                color_list.append(color)
            else:
                color = '#4CAF50' #green
                color_list.append(color)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_date, list_amount, color=color_list)
        for index,data in enumerate(list_amount):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig

    def chart_balance_permonth_account(self, account):
        color = '#3983E4' #blue
        title = account + " balance per month"
        list_month, list_balance = self.get_balance_permonth_account(account)
        list_balance = self.compress_list_amount(list_balance)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_month, list_balance, color=color)
        for index,data in enumerate(list_balance):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig
    
    def chart_balance_perday_account(self, account):
        color = '#3983E4' #blue
        title = account + " balance per day"
        list_date, list_balance = self.get_balance_perday_account(account)
        list_date = self.compress_list_date(list_date)
        list_balance = self.compress_list_amount(list_balance)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_date, list_balance, color=color)
        for index,data in enumerate(list_balance):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig
    
    def chart_balance_permonth(self):
        color = '#3983E4' #blue
        title = "Total balance per month"
        list_month, list_balance = self.get_total_balance_permonth()
        list_balance = self.compress_list_amount(list_balance)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_month, list_balance, color=color)
        for index,data in enumerate(list_balance):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        #plt.show()
        return fig
    
    def chart_balance_perday(self):
        color = '#3983E4' #blue
        title = "Total balance per day"
        list_date, list_balance = self.get_total_balance_perday()
        list_date = self.compress_list_date(list_date)
        list_balance = self.compress_list_amount(list_balance)
        plt.rcParams["figure.figsize"] = (16,9)
        fig = plt.figure(figsize=(16, 9))
        fig.suptitle(title, fontsize=20)
        plt.bar(list_date, list_balance, color=color)
        for index,data in enumerate(list_balance):
            plt.text(x=index-0.17 , y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
        return fig