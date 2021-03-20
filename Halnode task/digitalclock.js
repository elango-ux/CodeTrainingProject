
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
        
       function fontFamily(){
  
        let  onchangeEvent = document.querySelector(".input")
        onchangeEvent.onchange= function(){
          let sel1 = document.querySelector(".input");
          console.log(sel1);
          let strUser1 = sel1.options[sel1.selectedIndex].value;
         console.log(strUser1);
         document.body.style.fontFamily = strUser1;
}

        }
        fontFamily();
        function fontSize(){
        let  onchangeEvent = document.querySelector(".backgroundcolor")
        onchangeEvent.onchange= function(){
          let sel1 = document.querySelector(".backgroundcolor");
          console.log(sel1);
          let strUser1 = sel1.options[sel1.selectedIndex].value;
         console.log(strUser1);
          let body = document.querySelector(".container");
          body.style.fontSize = strUser1; 
          console.log(body);
        }
      }
        fontSize();


        function backgroundColor(){

                
          document.body.style.backgroundColor = "yellow";
        document.querySelector(".btn").onclick = function(){
         
        let bodyColor = document.querySelector(".body1");
          let color = [ "red", "orange", "green"];
         const colorIndex = parseInt(Math.random()*color.length);
         document.body.style.backgroundColor = color[colorIndex]
         
        }

        }
           backgroundColor()
       function colorPicker() {
        let colorinput =  document.querySelector(".colorpicker");
        let textbox =  document.querySelector(".textbox");
        colorinput.addEventListener('input',()=>{
       let colorValue = colorinput.value;
       console.log(colorValue);
       let  textbox1  = textbox.value = colorValue;
       console.log(textbox1);
       document.body.style.backgroundColor = colorValue;
       
       
       
        });

 




       }
       colorPicker();