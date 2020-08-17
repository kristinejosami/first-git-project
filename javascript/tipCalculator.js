function calculate(){
  var one = document.getElementById('billAmount').value;
  var two = document.getElementById('peopleAmount').value;
  var three = document.getElementById('dropdown').value;

  var four = (one*three)/two
  document.getElementById('parathree').innerHTML="Tip Amount:"+'$'+four +' per person';
}
