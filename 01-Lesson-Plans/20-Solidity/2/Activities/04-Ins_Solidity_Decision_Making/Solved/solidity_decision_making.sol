pragma solidity ^0.5.0;

contract IfElse {
    uint y;

    function exampleIfElse(uint x) public {
        if (x < 10) {
            y = 0;
        }
        else if (x < 20) {
            y = 1;
        }
        else {
            y = 2;
        }
    }
}

contract IfElse {
    uint y=5;

    // view means function is read only, does not write any data to blockchain
    // view functions are free to invoke
    function isSame(uint x) public view returns (bool) {
        if (y == x){
            return true;
        }else {
            return false;
        }
    }

    function isGreater(uint x) public view returns (bool) {
        if (x > y){
            return true;
        }else {
            return false;
        }
    }


    function isGreaterOrEqual(uint x) public view returns (bool) {
        if (x >= y){
            return true;
        }else {
            return false;
        }
    }

    function isNot(uint x) public view returns (bool) {
        if (x != y){
            return true;
        } else {
            return false;
        }
    }

    function isSameLessOrGreater(uint x) public view returns (string memory) {
        if (x == y){
            return "equal";
        } else if (x > y){
            return "x > y";
        } else {
            return "x < y";
        }
    }

}