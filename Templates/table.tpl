<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/style.css">
    <title>YourPAY</title>
</head>
<body>
  <center><br>
    <h1>YourPay</h1> <a href="/{{username}}/logout">Logout</a><br>
    <h2> Le mie ultime transazioni</h2><br>

    <div style="overflow-x:auto;">
      <table width="50%" id="table">
        <tbody>
          <tr>
            <td class="tg-us36"><p>Data</p></td>
            <td><p>Importo</p></td>
            <td><p>Conto</p></td>
            <td><p>Commento</p></td>
          </tr>

          % for element in account_name:
            <tr>
              <td>{{account_name[element]['date']}}</td>
              <td>{{account_name[element]['amount']}}</td>
              <td>{{account_name[element]['account']}}</td>
              <td>{{account_name[element]['comment']}}</td>
            </tr>
          % end
        </tbody>
      </table>
    </div><br>

    <form action="/{{username}}/pay" method="post" target="iframe">
      <input name="date" placeholder="Quando hai fatto il pagamento? dd/mm/yyyy" type="text" size="36/">
      <input name="amount" placeholder="Quanto hai speso?" type="text" size="14/">
      <input name="account" placeholder="Con che conto hai pagato?" type="text" size="20/">
      <input name="comment" placeholder="Aggiungi un commento" type="text">
      <input value="Inserisci i dati" type="submit" />
    </form><br>
    <h3><a href="javascript:window.location.reload(true)">Update Table</a></h3>
    <iframe name="iframe" width="0" height="0" tabindex="-1" class="hidden"></iframe>
    <br><br>
    <div style="overflow-x:auto;">
     <table width=50% id="table2">
       <tbody>
         <tr>
           <td>
             <p>Conto</p>
           </td>
           <td>
             <p>Balances</p>
           </td>
         </tr>

         % for element in account_balances:
         <tr>
           <td>
             <p>{{element[0]}}</p>
           </td>
           <td>
             <p>{{element[1]}}</p>
           </td>
         </tr>
         % end
      </tbody>
     </table>
   </div>
  </center>

</body>
</html>
