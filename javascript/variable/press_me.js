/* const buttonA = document.querySelector("#buttonA");
const headingA = document.querySelector("#headingA");


buttonA.onclick = () => {
    const myName = prompt("What's your name?");
    alert('Hello ${myName}, nice to meet you!!');
    headingA.textContent = 'Welcome to the page {myName}';

 */

const buttonA = document.querySelector("#button_A");
const headingA = document.querySelector("#heading_A");

buttonA.onclick = () => {
  const name = prompt("What is your name?");
  alert(`Hello ${name}, nice to see you!`);
  headingA.textContent = `Welcome ${name}`;
};
