let picklist = {

country:[ " ","india","pakistan","china","srilanka","ppp","kkk"],     
india:[ " ", "tamilNadu","kerala","goa","madhapradesh"],
pakistan:[" ", "balochistan","punjab","sindh","khyber"],
china:["","Anhui", "Fujian", "Guangdong", "Guizhou", "Hainan"],
srilanka:["","Sabaragamuw","Southern","Uva","Western","centre"],
tamilNadu:[                                                   ]
};
let  select= document.querySelector(".country");
for(let i=0;i<picklist.country.length;i++){       
     var option = document.createElement("option");
        select.append(option);
        let  textNode = document.createTextNode(picklist.country[i]);
        option.append(textNode);
        option.setAttribute("class","option1");
}

let  onchangeEvent = document.querySelector(".country")
onchangeEvent.onchange= function(){//onchange if value  selected 
//changed  than  provide that information
         let sel1 = document.querySelector(".country");
        console.log(sel1);
        let strUser1 = sel1.options[sel1.selectedIndex].value;//it provide  value  dependend  on  selected value of   dropdown menu 
        console.log(strUser1);
   
 let  select1=   document.querySelector(".state");
        if(strUser1=="india") {
    for(let i=0;i<picklist.india.length;i++){

        let option1 = document.createElement("option");
        select1.append(option1);
        let  textNode = document.createTextNode(picklist.india[i]);
        option1.append(textNode);
}
}    
else if(strUser1 == "pakistan"){
document.querySelector(".state").innerHTML= null;
        for(let i=0 ;i< picklist.pakistan.length;i++){

        let option2 = document.createElement("option");
        select1.append(option2);
         let  textNode = document.createTextNode(picklist.pakistan[i]);
         option2.append(textNode);
        }
}   
else if(strUser1 == "china")  {
        document.querySelector(".state").innerHTML= null;
        for(let i=0;i<picklist.china.length;i++){
                 console.log(picklist.china[i]);
             
                //create  options tag attach to select tag
                var option3 = document.createElement("option");
                select1.append(option3);
                let  textNode = document.createTextNode(picklist.china[i]);
                option3.append(textNode);

}
}
else if(strUser1 == "srilanka" ){
document.querySelector(".state").innerHTML= null;
        for(let i=0;i<picklist.srilanka.length;i++){
        console.log(picklist.srilanka[i]);
               
                //create  options tag attach to select tag
                var option4 = document.createElement("option");
                select1.append(option4);
                let  textNode = document.createTextNode(picklist.srilanka[i]);
                option4.append(textNode);
        }
        
}
 };

let  changeEvent= document.querySelector(".state").onchange= function(){
        let sel2 = document.querySelector(".state");
        console.log(sel2);
        let strUser2 = sel2.options[sel2.selectedIndex].value;//it provide  value  dependend  on  selected value of   dropdown menu 
        let  select1   =   document.querySelector(".dist");
           console.log(select1);
         if(strUser2  == "tamilNadu"){










         }
     

  






};