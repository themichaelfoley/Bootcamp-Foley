pragma solidity ^0.5.0;

contract LatestTrade {
    string coin = "BTC";
    uint256 price;
    bool isBuyOrder;
    address auth_user = msg.sender;

    function updateTrade(string memory newCoin, uint256 newPrice, bool isBuy) public {
        coin = newCoin;
        price = newPrice;
        isBuyOrder = isBuy; // Is this a buy or a sell order?
    }
}

//setter function 
function updateCoin(string memory newCoin) public {
    require(msg.sender==auth_user, "Unauthorized");
    coin = newCoin
}

//getter function
function getCoin public view returns (string memory) {
    require(msg.sender==auth_user, "Unauthorized")
    return coin;
}