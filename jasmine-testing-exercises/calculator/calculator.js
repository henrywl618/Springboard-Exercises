

window.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById("calc-form");
  if (form) {
    setupIntialValues();
    form.addEventListener("submit", function(e) {
      e.preventDefault();
      update();
    });
  }
});

function getCurrentUIValues() {
  return {
    amount: +(document.getElementById("loan-amount").value),
    years: +(document.getElementById("loan-years").value),
    rate: +(document.getElementById("loan-rate").value),
  }
}

// Get the inputs from the DOM.
// Put some default values in the inputs
// Call a function to calculate the current monthly payment
function setupIntialValues() {
  document.getElementById("loan-amount").value = 100000;
  document.getElementById("loan-years").value = 30;
  document.getElementById("loan-rate").value = 8;
  update();
}

// Get the current values from the UI
// Update the monthly payment
function update() {
  const payment = calculateMonthlyPayment(getCurrentUIValues());
  document.getElementById("monthly-payment").innerText = payment;

}

// Given an object of values (a value has amount, years and rate ),
// calculate the monthly payment.  The output should be a string
// that always has 2 decimal places.
function calculateMonthlyPayment(values) {
  const P = values.amount;
  const i = values.rate/100/12;
  const n = values.years*12;

  let monthlyPayment = (P*i)/(1-Math.pow((1+i),-n));
  monthlyPayment = roundToTwoDec(monthlyPayment); //round to 2 decimal places
  return monthlyPayment;

}

// Given a string representing the monthly payment value,
// update the UI to show the value.
function updateMonthly(monthly) {
}

// Given a number, return a number with 2 decimal places
function roundToTwoDec(num){
  if(Number(num)){ //if parameter is a number
    return Number(num.toFixed(2));
  }
};