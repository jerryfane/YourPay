<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/style.css">
    <title>YourPAY - Homepage</title>
</head>
<body>
  <center><br>
    <h1>YourPay</h1><br>
    <h2> Creating your account {{username}}:</h2><br>
    <form action="/{{username}}/account_created" method="post">

        % for i in range(0, account_number):
        Account Name #{{i+1}}: <input name="account_name_{{i+1}}" type="text" />
        Account #{{i+1}} Balance <input name="account_balance_{{i+1}}" type="number" /><br>
        % end
        <input value="Continua" type="submit" />
    </form>
  </center>
</body>
