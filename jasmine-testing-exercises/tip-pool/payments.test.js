describe("Payments test (with setup and tear-down)", function(){

    beforeEach(function(){
        billAmtInput.value = 100;
        tipAmtInput.value = 20;
    });

    it('should, on submit, add curPayment object to allPayments, update html and reset input values', function(){
        submitPaymentInfo();
        expect(document.querySelectorAll('#paymentTable tr').length).toEqual(2);
        expect(document.querySelectorAll('#paymentTable tr')[1].children.length).toEqual(4);
    });

    it('should not add a new payment if the billinput is empty', function(){
        billAmtInput.value = '';
        submitPaymentInfo();
        expect(Object.keys(allPayments).length).toEqual(0);
    });

    it('should return an object with bill,tip and tip percentage', function(){
        expect(createCurPayment()).toEqual({
            billAmt: '100',
            tipAmt: '20',
            tipPercent: 20,
          });
    });

    it('should return undefined if the bill or tip amount input is empty', function(){
        billAmtInput.value = '';
        expect(createCurPayment()).toEqual(undefined);
        billAmtInput.value = 100;
        tipAmtInput.value = '';
        expect(createCurPayment()).toEqual(undefined);
    });

    it('should return an object if the bill amount is positive/nonempty but tip amount is 0', function(){
        tipAmtInput.value = 0;
        expect(createCurPayment()).toEqual({
            billAmt: '100',
            tipAmt: '0',
            tipPercent: 0,
          });
    });
    
    it('should create a new tr and td appended with value from given curPayment object and append tr to paymentTable', function(){
        let currentPayment = createCurPayment();
        appendPaymentTable(currentPayment);

        expect(document.querySelectorAll('#paymentTable tr').length).toEqual(2);
        expect(document.querySelectorAll('#paymentTable tr')[1].children.length).toEqual(4);
        expect(document.querySelectorAll('#paymentTable tr')[1].children[0].innerText).toEqual('$100');
        expect(document.querySelectorAll('#paymentTable tr')[1].children[1].innerText).toEqual('$20');
        expect(document.querySelectorAll('#paymentTable tr')[1].children[2].innerText).toEqual('20%');
    });
    

    afterEach(function(){
        allPayments={};
        document.getElementById('billAmt').value = '';
        document.getElementById('tipAmt').value = '';
        document.querySelector('#summaryTable tbody').innerHTML = '';
        document.querySelector('#paymentTable tbody').innerHTML = '';
        
    });
});