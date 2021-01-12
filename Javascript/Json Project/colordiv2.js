//it select add class name child


let child = document.querySelectorAll(".child");
//it select parent  div   class name container  


let container = document.querySelector(".container");
//it  on click  all div class name of child
for(let i=0;i<child.length;i++){
  child[i].onclick = function(){
     
    
    // it help to get index of all div on click  so  to make condition
    let parent = child[i].parentNode; //it  help to get  indec of  child
  let  index= Array.prototype.indexOf.call(parent.children, child[i]);//it help  to get index of child
  
  console.log(index);
    
  if(index == 0){
    
    //remove all blue color by  removing  class name cols
    let  select= document.querySelectorAll(".cols");
     for(let i=0;i<select.length;i++){
      select[i].classList.remove("cols");
     }
  // add  blue color   add class name cols 
    for(let i=0;i<child.length;i+=4){
  child[i].classList.add("cols");
    
}
  }
  else if(index == 1){
     //remove all blue color by  removing  class name cols
    let  select= document.querySelectorAll(".cols");
        for(let i=0;i<select.length;i++){
              select[i].classList.remove("cols");
        }
             
        // add  blue color   add class name cols
        
        for(let i=1;i<child.length;i+=4){
                child[i].classList.add("cols");

    }
      
  }
  else if(   index ==  2)  { 
 
  //remove all blue color by removing  class name  cols
  let  select= document.querySelectorAll(".cols");
        for(let i=0;i<select.length;i++){
              select[i].classList.remove("cols");
        }

// add  blue color   add class name cols 
for(let i=2;i<child.length;i+=4){
  child[i].classList.add("cols");

}

  }

else if(index==3){

//remove all blue color by removing class name cols
let  select= document.querySelectorAll(".cols");
for(let i=0;i<select.length;i++){
      select[i].classList.remove("cols");
}
//add blue color by adding class name cols    
for(let i=3;i<child.length;i+=4){
  child[i].classList.add("cols");

}


}




// ?doubt how to   eliminate all   for loop 


















  }
}
