describe("Helpers test (with setup and tear-down)", function(){

    it('should sum up all the payments for the shift', function(){
        
    });

    it('should calculate the tip percentage', function(){
        expect(calculateTipPercent(100,20)).toEqual(20);
        expect(calculateTipPercent(200,20)).toEqual(10);
        expect(calculateTipPercent(1,.25)).toEqual(25);
    });
    

});