
let childContainer = document.querySelectorAll(".child");                
childContainer[0].onclick= function()
       {
               let selectcols = document.querySelectorAll(".cols");
       for(let i=0; i<selectcols.length; i++){
              selectcols[i].classList.remove("cols");//remove classLIst

       }
       childContainer[0].className += " cols";
       childContainer [4].className += " cols";
              
              
              
              
       }
       
       childContainer [1].onclick= function(){
              let selectcols1= document.querySelectorAll(".cols");
              for(let i=0; i< selectcols1.length; i++){
                     selectcols1[i].classList.remove("cols");//remove class name
              }
              childContainer [1].className += " cols";//add class name
              childContainer[5].className += " cols";//add class name
    
              childContainer[2].onclick=function(){
   let  selectcols2= document.querySelectorAll(".cols");
       for(let j=0; j< selectcols2.length; j++){
              selectcols2[j].classList.remove("cols");

       }
       childContainer [2].className += " cols" 
       childContainer [6].className += " cols"



  }
 childContainer[3].onclick =function(){
       
       
         
  let  selectcols3 =document.querySelectorAll(".cols");
          
      
       for(let i = 0;i< selectcols3.length; i++){
              selectcols3[i].classList.remove("cols")
 }
  childContainer[3].className += " cols" 
         childContainer[7].className += " cols"
       


}

   
  

 }






        











   
 




          









       