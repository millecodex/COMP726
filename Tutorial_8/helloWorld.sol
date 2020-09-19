/* basic contract structure:
 * https://solidity.readthedocs.io/en/v0.7.1/structure-of-a-contract.html
 */
pragma solidity ^0.7.1;

contract helloWorld{
//
int balance;
int principle = 100;
uint rate = 5;
//global variables are more $$$
uint comp;
int timePeriods2;

    /* Remix button colours:
     * blue buttons are for pure/view; 
     * these are only callable (getter) functions and do NOT change state
     * orange are non-payable (cannot accept ether) but DO change the state
     * also red are payable (next week)
     */
    function hello() public pure returns(string memory){
        return 'helloWorld';
    }
    
    //look at the gas cost here -> 21850 every time its called!
    //see the ether balance leftover in the account
    function getBalance() public view returns(int){
        return balance;
    }
    
    /*function calcInterest() public returns(int interest){
        interest = principle*rate/100;
        balance = principle + interest;
        return interest;
    }*/
    //compound interest means that at time t+1 the interest
    //is calculated on balance + interest at time time
    // balance = principle*(1 - rate^timePeriods)
    // so for 1 year of compounded monthly @5%:
    // balance = 100*(1+5/100)^12
    /*function compInterest() public returns(uint comp){
        //base2 = 1+rate/100;
        //timePeriods2 = 12;
        //compInterest = base2^timePeriods2;
        //use local variables
        uint base = 1+rate/100;
        uint timePeriods = 124;
        comp = base**timePeriods;
        return comp;
    }*/
    
    function compInterest() public {
        //base2 = 1+rate/100;
        //timePeriods2 = 12;
        //compInterest = base2^timePeriods2;
        //use local variables
        uint base = 1+rate;
        uint timePeriods = 12;
        comp = base**timePeriods;
    }
    
    function getCompInterest() public view returns(uint){
        return comp;
    }
    
}
