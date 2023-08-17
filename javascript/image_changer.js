const myImage = document.querySelector("img");

myImage.onclick = () => {
  const mySrc = myImage.getAttribute("src");
  if (mySrc === "img\ink1.jpg") {
    myImage.setAttribute("src", "img\ink2.jpg");
  } else {
    myImage.setAttribute("src", "img\ink1.jpg");
  }
};
