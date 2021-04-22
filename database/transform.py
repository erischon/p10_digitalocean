import json


class Transform:
    def __init__(self):
        """ """
        self.fields = (
            "product_name_fr",
            "code",
            "categories",
            "nutriscore_grade",
            "url",
            "brands",
            "stores",
            "image_small_url",
        )
        self.data_clean = {}
        self.open_json()

    def open_json(self):
        """ I open the extract json. """
        with open("static/database/off_data_extract.json", encoding="utf-8") as json_file:
            self.data_extract = json.load(json_file)

    def transform_basic(self):
        """ I take the fields I want from the extract json. """
        for n in range(len(self.data_extract["products"])):

            self.data_clean[
                self.data_extract["products"][n][self.fields[1]].lower()
            ] = {}

            for field in self.fields:
                try:
                    if field != self.fields[1]:
                        self.data_clean[
                            self.data_extract["products"][n][self.fields[1]].lower(
                            )
                        ][field] = self.data_extract["products"][n][field].lower()
                except KeyError:
                    self.data_clean[
                        self.data_extract["products"][n][self.fields[1]].lower(
                        )
                    ][field] = 'X'

        self.transform_field(self.data_clean)

        return "REUSSITE"

    def transform_field(self, data_clean):
        """ I try to clean the data. """
        for code in data_clean:
            # Categories
            list_values = data_clean[code]["categories"].split(",")
            list_values = [value.strip(" ") for value in list_values]
            data_clean[code]["categories"] = list_values

            # Brands
            list_values = data_clean[code]["brands"].split(",")
            list_values = [value.strip(" ") for value in list_values]
            data_clean[code]["brands"] = list_values

            # Stores
            list_values = data_clean[code]["stores"].split(",")
            list_values = [value.strip(" ") for value in list_values]
            data_clean[code]["stores"] = list_values

        self.create_json(data_clean)

    def create_json(self, data_clean):
        """ I create the transform json. """
        with open("static/database/off_data_transform.json", "w") as fp:
            json.dump(data_clean, fp)
        return


if __name__ == "__main__":
    transform = Transform()

    transform.transform_basic()
