
      let input = {
		orderLines: [
			{ designNo: 'abc', size: {value:"S",slug :'s'}, quantity: 20 },
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

	    
	// let output = {
	// 	orderLines: {
	// 		abc: { S: 22, M: 25, L: 10 },
	// 		xyz: { S: 15, M: 25, L: 10 },
	// 		123: { 30: 7, 32: 9 },
	// 	},
	// };
	
	var answer = {};
	    var orderLines = input['orderLines'];
		for(let i= 0; i< orderLines.length;i++){
           
			if(answer.hasOwnProperty(orderLines[i]['designNo'])) {
                    if(answer[orderLines[i]['designNo']].hasOwnProperty(orderLines[i]['size'])) {
                       answer[orderLines[i]['designNo']][orderLines[i]['size']] +=   orderLines[i]['quantity'];     
                 

					}
					else {
                            answer[orderLines[i]['designNo']][orderLines[i]['size']] = orderLines[i]['quantity']
                 

					}
 


		   }
           else {

         answer[orderLines[i]['designNo']] = {};
			answer[orderLines[i]['designNo']][orderLines[i]['size']] = orderLines[i]['quantity']
		  
		  
          


		   }
          





		}
		console.log(answer);