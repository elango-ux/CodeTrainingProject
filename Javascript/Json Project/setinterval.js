let  select =  document.querySelector(".child");//add div
let htmlObject1 = document.querySelector(".example");
let htmlObject2= document.querySelector(".child5");// add first div
let htmlObject3 = document.querySelector(".child6");
let htmlObject4 = document.querySelector(".child7");
let htmlObject5 = document.querySelector(".child8");
let htmlObject6 = document.querySelector(".child9");
let htmlObject7 = document.querySelector(".child10");
function setinterval(){
    select.className = "child1";//remove first div
    htmlObject1.className="child";//add second div
}
 setTimeout(setinterval , 2000);

 function setinterval1(){
          htmlObject1.className = "child1"//remove 2nd div
          htmlObject2.className = "child";// add 3rd div
 }
   setTimeout(setinterval1,4000);
   function setinterval2(){
              htmlObject2.className ="child1";//remove  3rd div
              htmlObject3.className="child";// add 4th div
            }
  setTimeout(setinterval2,6000);
           
  
  function setinterval3(){
   
   htmlObject3.className="child1";// remove 4th div
    htmlObject4.className="child";//add fifth div


}
setTimeout(setinterval3,8000);
  function setinterval4(){
   htmlObject4.className="child1";//remove fifth div
    htmlObject5.className="child";// add 6th div

}
setTimeout(setinterval4,10000);
  
function setinterval5(){

    htmlObject5.className="child1";//remove six th div
    htmlObject6.className="child";// add 7th div
   
}
setTimeout(setinterval5,12000);


function setinterval6(){
htmlObject6.className="child1";// remove 7th div
htmlObject7.className="child";// add 8th div

}
setTimeout(setinterval6,14000);
function setinterval7(){
     htmlObject7.className="child1";// remove 8th div
    select.setAttribute("class","child"); 
    setTimeout(setinterval , 2000);
    setTimeout(setinterval1,4000);
    setTimeout(setinterval2,6000);
    setTimeout(setinterval3,8000);
    setTimeout(setinterval4,10000);
    setTimeout(setinterval5,12000);
    setTimeout(setinterval6,14000);
    setTimeout(setinterval7,16000);
}
   setTimeout(setinterval7,16000);
   