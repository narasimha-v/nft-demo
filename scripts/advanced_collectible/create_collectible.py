from brownie import AdvancedCollectible, config, network  # type: ignore
from scripts.helpful_scripts import fund_with_link, get_account, get_contract


def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("Collectible created!")
