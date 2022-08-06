pragma solidity ^0.5.0;

contract BankAccount {
    address payable accountOwner = 0xc3879B456DAA348a16B6524CBC558d2CC984722c;

    function withdraw(uint amount, address payable recipient) public {
        require(recipient == accountOwner, "You don’t own this account!");
        return recipient.transfer(amount);
    }

    function deposit() public payable {}

    function() external payable {}
}


//Dan's version
pragma solidity ^0.5.0;

contract BankAccount {

    address payable public accountOwner = msg.sender; // whoever launched this contract

    function withdraw(uint amount, address payable recipient) public{
        require(msg.sender == accountOwner, "YOU SHALL NOT PASS");
        return recipient.transfer(amount);
    }

    function deposit() public payable {}
    function () external payable {}

    function balance() external view returns (uint) {
        return address(this).balance;
    }
}