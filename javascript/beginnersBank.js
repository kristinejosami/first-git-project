var name = "Kristine"
var pass = "kristine123"

function returnInfo() {
  var money = 10000;
  var nameForm = document.getElementById('nameForm').value;
  var passForm = document.getElementById('passForm').value;
  var moneyForm = document.getElementById('moneyForm').value;
  var amount = money-moneyForm

  if (name != nameForm){
    alert('Wrong name! Please try again!');
  } else if (pass != passForm){
    alert('Wrong password! Please try again!');
  } else if (moneyForm > money){
    alert('Insufficient Funds!');
  }else{
    document.getElementById('newBal').innerHTML="You have succesfully made a withdrawal Kristine. Your new balance is: "+amount;
  }
}
