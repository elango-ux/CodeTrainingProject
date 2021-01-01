let jasonData = {

    "header":[ "fruits","vegetable","birds","animals"],
    "values":[                                      
                [ "mango","carrot","hen","cow"],
                ["orange","beans","crow","dog"],
                [ "banana","pumkin","eagle","cat"],
                ["peach", "beetroot","vultures","lion"]
            ]
};

let tableCreate =  document.createElement("Table");
 console.log(tableCreate);
document.querySelector(".div1").append(tableCreate);
// create empty header
let header =  tableCreate.createTHead();
//create row  
let row = header.insertRow(0);
let tbody = document.createElement("TBODY");
tableCreate.append(tbody);
console.log(tbody);

//loop  through  array of array  ie  values of object contain array of array
for(let i = 0; i<jasonData.header.length; i++){
    
    //CREATE CELL
    let cell = row.insertCell(i);//insert 4cell 
    cell.innerHTML= jasonData.header[i];
    let tbodyrow = tbody.insertRow(i);//insertrow in tbody
       for(let j= 0; j <jasonData.values.length;j++){
      
     let tbodyCell = tbodyrow.insertCell(j);
          tbodyCell.innerHTML = jasonData.values[i][j];
      console.log(jasonData.values[i][j]);
    
    }
}


     

    


  
    
     







     