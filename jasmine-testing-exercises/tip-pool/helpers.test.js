describe("Helpers test (with setup and tear-down)", function(){
    beforeEach(()=>{
        allPayments = {
            payment1: {billAmt: '100', tipAmt: '20', tipPercent: 20},
            payment2: {billAmt: '200', tipAmt: '10', tipPercent: 5},
        };
    });

    it('should sums total from allPayments objects', function(){
        expect(sumPaymentTotal('tipPercent')).toEqual(25);
        expect(sumPaymentTotal('billAmt')).toEqual(300);
        expect(sumPaymentTotal('tipAmt')).toEqual(30);
    });

    it('should calculate the tip percentage', function(){
        expect(calculateTipPercent(100,20)).toEqual(20);
        expect(calculateTipPercent(200,20)).toEqual(10);
        expect(calculateTipPercent(1,.25)).toEqual(25);
    });

    it('should append a newly created td element with a given value to a given tr', function(){
        const newTr = document.createElement('tr');
        appendTd(newTr, '$100');
        expect(newTr.children.length).toBe(1);
        expect(newTr.children[0].innerText).toBe('$100');
    });

    it('should generate a new td with innerText = X and append it to a given tr', function(){
        let newTr = document.createElement('tr');
        appendDeleteBtn(newTr);
        expect(newTr.children.length).toEqual(1);
        expect(newTr.firstChild.innerHTML).toEqual('X');
    });
    
    afterEach(()=>{
        allPayments = {};
    });

});