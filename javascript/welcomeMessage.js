var hour = new Date().gethours(welcome());

function welcome(){
  if (hour >= 6 && hour <=12) {
    document.getElementById('welcomeMessage').innerHTML='Good Morning!';
    document.getElementById('image').src="C:Users/kristine josami/Desktop/MyWebsite/HTML/morning.jpeg";
    document.body.style.backgroundColor='orange';
  } else if (hour >=13 && hour <=17) {
    document.getElementById('welcomeMessage').innerHTML='Good Afternoon!';
    document.getElementById('image').src="C:Users/kristine josami/Desktop/MyWebsite/HTML/afternoon.jpeg";
    document.body.style.backgroundColor='yellow';
  } else if (hour >=18 && hour <=24) {
    document.getElementById('welcomeMessage').innerHTML='Good Evening!';
    document.getElementById('image').src="C:Users/kristine josami/Desktop/MyWebsite/HTML/evening.jpeg";
    document.body.style.backgroundColor='blue';
  } else {
    document.getElementById('welcomeMessage').innerHTML='Good Dawn!';
    document.getElementById('image').src="C:Users/kristine josami/Desktop/MyWebsite/HTML/dawn.jpeg";
    document.body.style.backgroundColor='gray';
  }
}
