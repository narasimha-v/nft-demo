from brownie import SimpleCollectible  # type: ignore
from scripts.helpful_scripts import get_account, SAMPLE_TOKEN_URI, OPENSEA_URL


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(SAMPLE_TOKEN_URI, {"from": account})
    tx.wait(1)
    print(
        f"You can view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}"
    )
    return simple_collectible


def main():
    deploy_and_create()
