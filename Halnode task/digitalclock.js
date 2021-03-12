
    setInterval(showTime, 1000);
    function showTime() {
      let time = new Date(); 
    let hour = time.getHours(); 
    let min = time.getMinutes(); 
    let sec = time.getSeconds(); 
    let am_pm = "AM"; 
    
    if (hour > 12) { 
        hour -= 12; 
        am_pm = "PM"; 
    } 
    if (hour == 0) { 
        hour = 12; 
        am_pm = "AM"; 
    } 
    hour = hour < 10 ? "0" + hour : hour; 
    min = min < 10 ? "0" + min : min; 
    sec = sec < 10 ? "0" + sec : sec; 
    let currentTime = hour + ":" 
    + min + ":" + sec + am_pm; 
    document.getElementById("clock") 
                .innerHTML = currentTime; 
      
     } 
        showTime(); 
        
        
        var slideIndex = 1;
        showSlides(slideIndex);
        
        // Next/previous controls
        function plusSlides(n) {
          showSlides(slideIndex += n);
        }
        function showSlides(n) {
          var i;
          var slides = document.getElementsByClassName("mySlides");
          var dots = document.getElementsByClassName("dot");
          if (n > slides.length) {slideIndex = 1}
          if (n < 1) {slideIndex = slides.length}
          for (i = 0; i < slides.length; i++) {
              slides[i].style.display = "none";
          }
          for (i = 0; i < dots.length; i++) {
               dots[i].className = dots[i].className.replace(" active", "");
          }
          slides[slideIndex-1].style.display = "block";
        
        }
      
        let select = document.querySelector(".input");
           select.onchange= function(){

            let sel1 = document.querySelector(".input");
            console.log(sel1);
            let strUser1 = sel1.options[sel1.selectedIndex].value;
            console.log(strUser1)
            //it provide  value  dependend  on  selected value of   dropdown menu 
            document.querySelector(".body1").style.fontFamily = strUser1;
            console.log(strUser1) 

}

let select1 = document.querySelector(".backgroundcolor");
           select1.onchange= function(){

            let sel2 = document.querySelector(".backgroundcolor");
            console.log(sel2);
            let strUser2 = sel2.options[sel2.selectedIndex].value;
            console.log(strUser2)
            //it provide  value  dependend  on  selected value of   dropdown menu 
            document.querySelector(".body1").style.fontSize = strUser2;
            console.log(strUser2) 
           }
  


