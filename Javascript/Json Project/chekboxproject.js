let jsonData = [
   {
    "task":"did you brush",
    "isCompleted":true
    },
    {
    "task":"did you walk",
     isCompleted:false
    },
    {
       "task": "did you work",
       "isCompleted":true
   },
    {
    "task": "did you study",
    "isCompleted":true
    }
];
    // let x;
for(let i=0;i<jsonData.length;i++){
//create checkbox
        let selectDiv = document.querySelector(".checkboxjs"); 
          var createCheckBox = document.createElement("INPUT");
        createCheckBox.setAttribute("type", "checkbox");
        createCheckBox.setAttribute("class", "select"+i);
        
        selectDiv.append(createCheckBox);
    
    for(let obj in jsonData[i]){
     // createlabel
     
     if(jsonData[i][obj]  !== true &&   jsonData[i][obj] !=false){
     var createlabel = document.createElement('label');
     let createTextNode=document.createTextNode(jsonData[i][obj]);
      createlabel.append(createTextNode);
    selectDiv.append(createlabel);
     }
}
}

//make checkbox 1and 4  true
let checkCheckbox1= document.querySelector(".select0").checked=true;
    let  checkCheckbox2= document.querySelector(".select3").checked=true;
    
    document.querySelector(".textboxid1").onclick = function(){

// select all checkbox inside div
 let selectdiv=  document.querySelector(".checkboxjs");
     let allcheckbox=selectdiv.querySelectorAll('input[type="checkbox"]');
        
     //uncheck all checked box
     for(let j= 0; j<jsonData.length;j++){
          
            if(allcheckbox[j].checked==true){

                allcheckbox[j].checked=false;

            }}


    }
     document.querySelector(".textboxid2").onclick = function(){
       let   selectdiv3 =   document.querySelector(".checkboxjs");
    let checkall =  selectdiv3.querySelectorAll('input[type="checkbox"]');
    for(let k=0; k<jsonData.length;k++){
    checkall[k].checked=true
   }
}
                 



           
        
        
    
    
    