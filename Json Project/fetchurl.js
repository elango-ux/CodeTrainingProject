//fetch url
 const apiUrl = "http://data.fixer.io/api/latest?access_key=751ab0478e8aa1a09e75d8910e322ef1";
 console.log(apiUrl);
 fetch(apiUrl, {method:"GET" 
}).then(response => {
  return response.json();
   
}).then((information) => {
    console.log(information);
});


