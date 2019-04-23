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
    <h1>YourPay</h1>
    <a href="/{{username}}/logout">Logout</a> |
    <a href="/datas/{{username}}/{{random_number}}/{{username}}.json" download>Download Your Data</a><br>
    <h2> Le mie ultime transazioni</h2><br>

    <div style="overflow-x:auto;">
      <table width="55%" id="table">
        <tbody>
          <tr>
            <td class="tg-us36"><p>ID</p></td>
            <td><p>Data</p></td>
            <td><p>Importo</p></td>
            <td><p>Conto</p></td>
            <td><p>Categoria</p></td>
            <td><p>Commento</p></td>
          </tr>

          % for element in account_name:
            <tr>
              <td>{{element}}</td>
              <td>{{account_name[element]['date']}}</td>
              <td>{{account_name[element]['amount']}}</td>
              <td>{{account_name[element]['account']}}</td>
              <td>{{account_name[element]['category']}}</td>
              <td>{{account_name[element]['comment']}}</td>
            </tr>
          % end
        </tbody>
      </table>
    </div><br>

    <form action="/{{username}}/pay" method="post" target="iframe">
      <input name="date" placeholder="Quando hai fatto il pagamento? dd/mm/yyyy" type="text" size="40/">
      <input name="amount" placeholder="Quanto hai speso?" type="text" size="17/">
      <input name="account" placeholder="Con che conto hai pagato?" type="text" size="25/">
      <input name="category" placeholder="Inserisci una categoria" type="text" size="20/">
      <input name="comment" placeholder="Aggiungi un commento" type="text">
      <input value="Inserisci i dati" type="submit" />
    </form><br>
    <form action="/{{username}}/remove_row" method="post" target="iframe">
      <input name="row_id" placeholder="Seleziona l'ID della riga da eliminare" type="text" size="32/">
      <input value="Elimina riga" type="submit" />
    </form><br>
    <h3><a href="javascript:window.location.reload(true)">Update Table</a></h3>
    <iframe name="iframe" width="0" height="0" tabindex="-1" class="hidden"></iframe>
    <br><br>
    <div style="overflow-x:auto;">
     <table width=55% id="table2">
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
   <br>
   <form action="/{{username}}/new_account" method="post" target="iframe">
     <input name="account_name" placeholder="Nome del nuovo conto" type="text" size="21/">
     <input name="balance" placeholder="Saldo attuale del conto" type="text" size="21/">
     <input value="Crea nuovo conto" type="submit" />
  </form>
  </center>

</body>
</html>
