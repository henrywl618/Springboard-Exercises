
it('should calculate the monthly rate correctly', function () {
  // ...
  let values = {
    amount: 100000,
    years: 30,
    rate: 8,
  }
  expect(calculateMonthlyPayment(values)).toBe(733.76)
  values = {
    amount: 1200000,
    years: 30,
    rate: 8,
  }
  expect(calculateMonthlyPayment(values)).toBe(8805.17)
});


it("should return a result with 2 decimal places", function() {
  // ..
  expect(roundToTwoDec(123.568797)).toBe(123.57);
  expect(roundToTwoDec(123)).toBe(123.00);
  expect(roundToTwoDec(1456465456.1123132123)).toBe(1456465456.11);
});

/// etc

