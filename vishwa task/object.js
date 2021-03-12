let input = {
	orderLines: [
		{ designNo: 'abc', size: 'S', quantity: 20 },
		{ designNo: 'abc', size: 'M', quantity: 25 },
		{ designNo: 'abc', size: 'L', quantity: 10 },
		{ designNo: 'xyz', size: 'S', quantity: 15 },
		{ designNo: 'xyz', size: 'M', quantity: 25 },
		{ designNo: 'xyz', size: 'L', quantity: 10 },
		{ designNo: '123', size: '30', quantity: 7 },
		{ designNo: '123', size: '32', quantity: 9 },
		{ designNo: 'abc', size: 'S', quantity: 2 },
	],
};
//  console.log(input.orderLines["designNO"]);
// let orderLines = {
    


// }

// orderLines["abc"] =  {s : 22};

console.log(input.orderLines[0])
for(let i=0; i<input.orderLines.length; i++){
   if(input.orderLines[i].designNo == "abc") {
        
		console.log(input.orderLines[i].designNo);
		
       
	
	}
   }




