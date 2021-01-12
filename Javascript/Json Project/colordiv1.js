let  selectdiv1 = document.querySelector(".child1");
let selectdiv2 =document.querySelector(".child2");
let selectdiv3= document.querySelector(".child3");
let selectdiv4= document.querySelector(".child4");
let selectdiv5= document.querySelector(".child5");
let selectdiv6=document.querySelector(".child6");
let selectdiv7=document.querySelector(".child7");
let selectdiv8=document.querySelector(".child8");



selectdiv1.onclick =function(){
selectdiv1.classList.remove("child");
 selectdiv1.classList.add("cols");
selectdiv2.classList.remove("child");
 selectdiv2.classList.add("cols");
}
selectdiv3.onclick=function(){
selectdiv1.classList.remove("cols");//remove class name
selectdiv1.classList.add("child");//add class name
    selectdiv2.classList.remove("cols");
    selectdiv2.classList.add("child");
    selectdiv3.classList.remove("child");
    selectdiv3.classList.add("cols");
    selectdiv4.classList.remove("cols");
    selectdiv4.classList.add("cols");}
    selectdiv5.onclick= function(){
        selectdiv3.classList.remove("cols");
        selectdiv3.classList.add("child");
        selectdiv4.classList.remove("cols");
        selectdiv4.classList.add("child");
        selectdiv5.classList.remove("child");
        selectdiv5.classList.add("cols");
         selectdiv6.classList.remove("child");
         selectdiv6.classList.add("cols");
}
selectdiv7.onclick=function(){


    selectdiv5.classList.remove("cols");
    selectdiv5.classList.add("child");
     selectdiv6.classList.remove("cols");
     selectdiv6.classList.add("child");
     selectdiv7.classList.remove("child");
     selectdiv7.classList.add("cols");
     selectdiv8.classList.remove("child");
     selectdiv8.classList.add("cols");
}

