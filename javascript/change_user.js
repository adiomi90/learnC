myButton = document.querySelector("button");
myheading = document.querySelector("h1");

function setUserName(){
    const myName = prompt("Please enter")
    localStorage.setItem("name", myName)
    myheading.textContent = "INk babay is cool, ${myName}"
}