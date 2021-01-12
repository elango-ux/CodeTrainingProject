

 



let   set = setInterval(function(){
let selectelement = document.querySelectorAll(".row");
for(let i=0;i<selectelement.length;i++){
   selectelement[i].setAttribute("class","child");
   break;
   
   for(let j=0;j<selectelement.length;j ++){
     selectelement[j].setAttribute("class","child1");
    
    }
 }
},4000);
