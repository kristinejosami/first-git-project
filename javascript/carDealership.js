var carAvailables = ['BMW','Ford','Ferrari','Aston Martin'];
var para= '';

for (i=0; i<carAvailables.length; i++){
  para += carAvailables[i] + '<br>';
}
document.getElementById('myCars').innerHTML=para;
