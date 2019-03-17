setInterval(getRPM, 100);
setInterval(getSpeed, 100);

// async series?

function getRPM() {
  fetch('http://127.0.0.1:5000/rpm/')
      .then(data => {
            return data.text()
      })
      .then(myText => {
        document.getElementById("rpm").innerHTML = myText
      })
      .catch(error => {
        //document.getElementById("rpm").innerHTML = "error: " + error
      })
}

function getSpeed() {
  fetch('http://127.0.0.1:5000/speed/')
      .then(data => {
            return data.text()
      })
      .then(myText => {
        document.getElementById("speed").innerHTML = myText
      })
      .catch(error => {
        //document.getElementById("speed").innerHTML = "error: " + error
      })
}
