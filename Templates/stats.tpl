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

    <div style="overflow-x:auto;">
      <table width="55%" id="nocolor">
        <tbody>
          <tr>
            <td><p>Totale Speso</p></td>
            <td><p>{{total_spent}}</p></td>
          </tr>
        </tbody>
      </table>
    </div><br>

    <div style="overflow-x:auto;">
      <table width="55%" id="table">
        <tbody>
          <tr>
            <td class="tg-us36"><p>Categoria</p></td>
            <td><p>Speso</p></td>
            <td><p>Percentuale</p></td>
          </tr>

          % for category in category_list:
            <tr>
              <td>{{category}}</td>
              <td>{{category_balance[category]['balance']}}</td>
              <td>{{category_balance[category]['percentage']}}</td>
            </tr>
          % end
        </tbody>
      </table>
    </div><br>
