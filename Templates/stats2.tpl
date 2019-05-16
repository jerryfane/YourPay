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
      <select name="chart" placeholder="Select the chart" />
        <option value="Amount spent per day">Amount spent per day</option>
        <option value="Amount spent per month">Amount spent per month</option>
      </select>
      <select name="category" placeholder="Select the category" >
          % for category in category_list:
          <option value="{{category}}">{{category}}</option>
          %end
      </select>
      <input value="Create the chart" type="submit" />
    </form><br>

    <h3>Create your tailored chart by account</h1><br>

    <form action="/{{username}}/account" method="post" target="iframe">
      <select name="chart" placeholder="Select the chart" />
        <option value="Balance per day">Balance per day</option>
        <option value="Balance per month">Balance per month</option>
        <option value="Amount spent per day">Amount spent per day</option>
        <option value="Amount spent per month">Amount spent per month</option>
      </select>
      <select name="account" placeholder="Select the account" />
        % for account in accounts_list:
        <option value="{{account}}">{{account}}</option>
        %end
      </select>
      <input value="Create the chart" type="submit" />
    </form><br>

    <div class="wrapper">
      <iframe name="iframe"
              src="/nochart"
              frameBorder="0"
              scrolling="no"></iframe>
    </div>

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
