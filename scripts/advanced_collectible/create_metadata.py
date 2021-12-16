from pathlib import Path

import requests
from brownie import AdvancedCollectible, network  # type: ignore
from metadata.sample_metadata import metadata_template
from scripts.helpful_scripts import get_breed


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = " http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(f"{ipfs_url}{endpoint}", files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"Created {number_of_advanced_collectibles} collectibles.")
    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        print(metadata_file_name)
        collectible_metadata = metadata_template
        if (Path(metadata_file_name)).exists():
            print(f"{metadata_file_name} already exists! Delete to override")
        else:
            print(f"Creating metadata file {metadata_file_name}")
        collectible_metadata["name"] = breed
        collectible_metadata["description"] = f"An adrorable {breed} pup!"
        img_path = f"./img/{breed.lower().replace('_', '-')}.png"
        image_uri = upload_to_ipfs(img_path)
        collectible_metadata["image_uri"] = image_uri
        print(collectible_metadata)
