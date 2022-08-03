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

pragma solidity ^0.5.0;

contract BankAccount{
    address payable owner = msg.sender;

    function withdraw(uint amount, address payable recipient) public {
        // require the sender of this message (person withdrawing) is same as owner!
        require(msg.sender == owner, "YOU SHALL NOT PASS");
        return recipient.transfer(amount);
    }

    function deposit() public payable {}
    function () external payable {}

    function balance() public view returns (uint){
        return address(this).balance;
    }
}