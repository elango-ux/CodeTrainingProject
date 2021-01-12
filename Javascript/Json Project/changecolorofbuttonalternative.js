let  backgroundcolordiv =  document.querySelector(".green");
  backgroundcolordiv.style.background ="green";


 let  button1    =  document.querySelector(".button1");
     button1.style.marginTop ="20px";
     button1.style.marginLeft="20px" 
     
     button1.onclick= function(){
   
    backgroundcolordiv.style.background="red";
}

  let button2 = document.querySelector(".button2");
   
  button2.onclick= function(){
     
    backgroundcolordiv.style.background="yellow";

  }