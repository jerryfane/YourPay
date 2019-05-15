<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../../static/style.css">
    <title>YourPAY</title>
</head>
<body>
  <center><br>
    <h1>YourPay</h1>
    <a href="/{{username}}/logout">Logout</a> |
    <a href="/{{username}}/{{random_number}}.html"> Dashboard </a> |
    <a href="/datas/{{username}}/{{random_number}}/{{username}}.json" download>Download Your Data</a> |
    <a href="/{{username}}/stats/{{random_number}}.html">Statistics</a><br>
    <h2> Le mie statistiche</h2><br>

    <h3>Create your tailored chart by category</h1><br>

    <form action="/{{username}}/category" method="post" target="iframe">
      <input name="chart" list="charts_category" placeholder="Select the chart" />
      <input name="category" list="categories" placeholder="Select the category" size="25/" />
      <datalist id="charts_category">
        <option value="Amount spent per day">
        <option value="Amount spent per month">
      </datalist>
      <datalist id="categories">
        % for category in category_list:
        <option value={{category}}>
        %end
      </datalist>
      <input value="Create the chart" type="submit" />
    </form><br>

    <h3>Create your tailored chart by account</h1><br>

    <form action="/{{username}}/account" method="post" target="iframe">
      <input name="chart" list="charts_account" placeholder="Select the chart" />
      <input name="account" list="accounts" placeholder="Select the account" size="25/" />
      <datalist id="charts_account">
        <option value="Balance per day">
        <option value="Balance per month">
        <option value="Amount spent per day">
        <option value="Amount spent per month">
      </datalist>
      <datalist id="accounts">
        % for account in accounts_list:
        <option value={{account}}>
        %end
      </datalist>
      <input value="Create the chart" type="submit" />
    </form><br>

    <iframe name="iframe"
            src="/nochart"
            width="98%"
            height="500px"
            frameBorder="0"
            scrolling="no"></iframe>

    <h2>More Charts</h2><br>
    <h3>Total balance per day</h3><br>
    <img src="/static/{{username}}/balance_per_day.png?{{random_integer}}" style='height: 100%; width: 55%' /><br>

    <h3>Total balance per month</h3><br>
    <img src="/static/{{username}}/balance_per_month.png?{{random_integer}}" style='height: 100%; width: 55%' /><br>

    <h3>Total amount spent per day</h3><br>
    <img src="/static/{{username}}/amount_spent_per_day.png?{{random_integer}}" style='height: 100%; width: 55%' /><br>

    <h3>Total amount spent per month</h3><br>
    <img src="/static/{{username}}/amount_spent_per_month.png?{{random_integer}}" style='height: 100%; width: 55%' /><br>


    </div><br>
