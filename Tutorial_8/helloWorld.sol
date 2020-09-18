pragma solidity ^0.6.6;

contract helloWorld {
    //variable declarations
    uint jeff = 1000000;
    
    //should not consume gas
    function hello() public pure returns(string memory){
        return 'hello there amigo';
    }
    
    //should consume some gas
    function getJeff() public returns(uint){
        return jeff++;
    }
    
    //task for today
    function calculateX
}