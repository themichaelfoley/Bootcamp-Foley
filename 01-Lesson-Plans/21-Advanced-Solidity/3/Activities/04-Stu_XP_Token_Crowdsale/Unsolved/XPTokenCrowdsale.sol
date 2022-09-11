/*
XP-Token Crowdsale
*/

// @TODO: Add the pragma statement
pragma solidity ^0.5.0;
// @TODO: Add the import statement for the `XPTokenMintable.sol` file
// @TODO: Add the import statements for the OpenZeppelin `Crowdsale` contract.
// @TODO: Add the import statements for the OpenZeppelin `MintedCrowdsale` contract.
import "./XPTokenMintable.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";

contract XP_TokenCrowdsale is Crowdsale, MintedCrowdsale {

    // @TODO: Create a `constructor` function that includes three attributes: `rate`, `wallet` and `token`.
    constructor(
        uint rate,
        address payable wallet,
        XP_Token token
    )

    // @TODO: Create the public `Crowdsale` constructor that takes in the same three attributes: `rate`, `wallet`, and `token`.

        Crowdsale(rate, wallet, token)
        public
    {
        // constructor body can stay empty
    }
}
    // @TODO



contract XP_TokenCrowdsaleDeployer {
    address public XP_token_address;
    address public XP_crowdsale_address;

    // @TODO: Add public addresses to keep track of the token_address and arcade_sale_address

    constructor(
        string memory name,
        string memory symbol,
        address payable wallet // this address will receive all Ether raised by the sale
    )
        public
    {
        // @TODO: create the XP_Token and its address
        // Your code here!
        XP_Token token = new XP_Token(name, symbol, 0);
        XP_token_address = address(token);

        // @TODO: create the XP_TokenCrowdsale and its address
        // Your code here!
        XP_TokenCrowdsale XP_crowdsale = new XP_TokenCrowdsale(1, wallet, token);
        XP_crowdsale_address = address(XP_crowdsale);

        // @TODO: make the XP_TokenCrowdsale contract a minter, then have the XP_TokenCrowdsaleDeployer renounce its minter role
        // Your code here!
        token.addMinter(XP_crowdsale_address);
        token.renounceMinter();
    }
}
