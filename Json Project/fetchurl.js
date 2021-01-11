let  selectpicklist1 = document.querySelector(".picklist1");
let  selectpicklist2 = document.querySelector(".picklist2");
let    currencyValue = document.querySelector(".div1");
let  textbox = document.querySelector(".textbox");
console.log(textbox);

//fetch url
 const apiUrl = "http://data.fixer.io/api/latest?access_key=d4495a69497d34870f0142408b966fb6";
 console.log(apiUrl);

 fetch(apiUrl, {method:"GET" 
}).then(response => {
  return response.json();
   
}).then((information) => {
    console.log(information);  
       
       for(let  property in  information["rates"]){
          let createOption = document.createElement("option");
             createOption.innerHTML= property;
          selectpicklist1.append(createOption);             
                 }
                  
               
                 for(let  property1 in  information["rates"]){
                 let createOption1 =   document.createElement("option");
                  createOption1.innerHTML=   property1;
                  selectpicklist2.append(createOption1);            
                 
               }
            
              //
               let  onchangeEvent = document.querySelector(".picklist1");
                       onchangeEvent.onclick = function(){
                       let sel1 = document.querySelector(".picklist1");
                       let strUser1 = sel1.options[sel1.selectedIndex].value;
                       console.log(strUser1);



                       let onchangeEvent1 = document.querySelector(".picklist2");
                       onchangeEvent1.onclick = () => {
                        let sel2 = document.querySelector(".picklist2");
                        let strUser2 = sel2.options[sel2.selectedIndex].value;
                      console.log(strUser2);

if(textbox.value>0 ){

 if(strUser1 =="EUR"&& strUser2=="AED"){
  let  currency = textbox.value*information.rates.AED;
  console.log(currency);
  currencyValue.innerHTML=  currency;                   

}
else if(strUser1 =="EUR"&& strUser2 =="AFN"){
let currency =  textbox.value*information.rates.AFN;
currencyValue.innerHTML=  currency;
}

else if(strUser1 =="EUR"&& strUser2 =="ALL"){
   let currency =  textbox.value*information.rates.ALL;
   currencyValue.innerHTML=  currency;
   }

   else if(strUser1 =="EUR"&& strUser2 =="AMD"){
      let currency =  textbox.value*information.rates.AMD;
      currencyValue.innerHTML=  currency;
      }
      else if(strUser1 =="EUR"&& strUser2 =="ANG"){
         let currency =  textbox.value*information.rates.ANG;
         currencyValue.innerHTML=  currency;
         }
         else if(strUser1 =="EUR"&& strUser2 =="AOA"){
            let currency =  textbox.value*information.rates.AOA;
            console.log(currency);
            currencyValue.innerHTML=  currency;
            }

            else if(strUser1 =="EUR"&& strUser2 =="ARS"){
               let currency =  textbox.value*information.rates.ARS;
               console.log(currency);
               currencyValue.innerHTML=  currency;
               }
   
               else if(strUser1 =="EUR"&& strUser2 =="AUD"){
                  let currency =  textbox.value*information.rates.AUD;
                  console.log(currency);
                  currencyValue.innerHTML=  currency;
                  }
               }

              else {

                 currencyValue.innerHTML= "enter a number";
 }

 };
};
            
});