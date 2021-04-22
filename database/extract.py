import requests
import json


class Extract:
    """ Extract data from OpenFoodFacts. """

    def __init__(self):
        self.URL = "https://fr.openfoodfacts.org/cgi/search.pl"
        self.HEADERS = {"User-Agent": "OC-P5 - GNU/Windows - Version 0.1"}
        self.PARAMS = {
            "search_simple": 1,
            "action": "process",
            "json": 1,
            "tagtype_0": "countries",
            "tag_contains_0": "contains",
            "tag_0": "france",
            "page_size": 500,
            "page": 1,
            "sort_by": "unique_scans_n",
        }

    def extract(self):
        """ I extract product from OpenFoodFacts """
        try:
            request = requests.get(
                url=self.URL, params=self.PARAMS, headers=self.HEADERS
            )
            products = request.json()

            with open("static/database/off_data_extract.json", "w") as f:
                json.dump(products, f)

            return "REUSSITE de l'Extraction"

        except Exception as error:
            return "ECHEC : les produits ne sont pas téléchargés.", f"Type de l'erreur : {error}"


if __name__ == "__main__":
    extract = Extract()

    # === Tests of methods ===
    # extract.extract()
