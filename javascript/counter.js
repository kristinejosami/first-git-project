var x = 0;
var xTwo = "Count : ";
var colorArray = ['#f9f57f','#f9f56b','#f9f459','#f9f345','#f9f334','#fcf41b','#fff600']

function addOne(){
  x += 1;
  document.getElementById('hi').innerHTML= xTwo+x;
  document.body.style.backgroundColor=colorArray[x-1];
}
function addTwo(){
  x -= 1;
  document.getElementById('hi').innerHTML= xTwo+x;
  document.body.style.backgroundColor=colorArray[x+1];
}
