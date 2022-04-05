from brownie import UniswapV2Factory, Token1, Token2, accounts, network, config
from scripts.helpful_scripts import get_account


def deploy():
    account = get_account()
    uniswap_v2_factory = UniswapV2Factory.deploy(account.address, {"from": account})
    return uniswap_v2_factory


def create_pair():
    account = get_account()
    uniswap_v2_factory = UniswapV2Factory[-1]
    if network.show_active() == "mainnet":
        token1_add = config["networks"][network.show_active()]["token1"]
        token2_add = config["networks"][network.show_active()]["token2"]
    else:
        token1 = Token1.deploy({"from": account})
        token2 = Token2.deploy({"from": account})
        token1_add = token1.address
        token2_add = token2.address

    uniswap_v2_factory.createPair(token1_add, token2_add)


def main():
    deploy()
    create_pair()
