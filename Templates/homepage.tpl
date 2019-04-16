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
        <h2>Login:</h2>
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input type="submit" value="Login" />
        </form><br>
        <h2>Create New Account</h2>
        <form action="/create_account" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input type="submit" value="Create Account" />
        </form>
    </center>
</body>
