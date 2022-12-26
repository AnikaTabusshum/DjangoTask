fetch("stock_market_data.json")
.then(function(response){
   return response.json();
})
.then(function(items){
   let placeholder = document.querySelector("#data-output");
   let out = "";
   for(let item of items){
      out += `
         <tr>
            <td>${item.date}</td>
            <td>${item.trade_code}</td>
            <td>${item.high}</td>
            <td>${item.low}</td>
            <td>${item.open}</td>
            <td>${item.close}</td>
            <td>${item.volume}</td>
         </tr>
      `;
   }
 
   placeholder.innerHTML = out;
});

