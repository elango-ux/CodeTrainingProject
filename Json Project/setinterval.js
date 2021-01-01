
let  x= document.querySelector(".animate");
x.onclick = function() {
  

    var pos = 0;
    var id = setInterval(frame, 1);
    function frame() {
      if (pos == 250) {
        clearInterval(id);
      } else {
        pos++;
        x.style.top = pos + 'px';
        x.style.left = pos + 'px';
      }


    }


}


  