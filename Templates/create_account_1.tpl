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
      <h2>Create new user: {{username}}</h2><br>
      <form action="/{{username}}/create_account" method="get">
          Numero di conti da registrare: <input name="account_number" type="number" />
          <input value="Crea" type="submit" />
      </form>
    </center>
</body>
