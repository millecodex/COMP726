/* basic contract structure:
 * https://solidity.readthedocs.io/en/v0.7.1/structure-of-a-contract.html
 */
pragma solidity ^0.7.1;

contract helloWorld{
//global variables here; these are more $$$
uint value;

    /* Remix button colours:
     * blue buttons are for pure/view; 
     * these are only callable (getter) functions and do NOT change state
     * orange are non-payable (cannot accept ether) but DO change the state
     * also red are payable (next week)
     */
    function hello() public pure returns(string memory){
        //this function call should be free; check gas
        return 'hello there amigo';
    }
    
    //this function will do some calculation
    //note the button colour
    //remix will tell you exactly how much gas (21045)
    function helloGas() public returns(uint){
        return value++;
    }
    
    //we have 10 VM accounts here, lets look at a balance
    /*globally available variables: https://solidity.readthedocs.io/en/v0.7.1/units-and-global-variables.html
     * msg.sender
     * msg.value
     * tx.gasprice
     * block.number
       etc.*/ 
    function getBalance() public view returns(uint){
        //this is the contract balance, not the user account balance
        return address(this).balance;
    }
    //How to output a user's (address) balance?
    function getAccountBalance() public view returns(uint){
    //code here
    }
}
