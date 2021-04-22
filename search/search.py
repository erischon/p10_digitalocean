from database.models import Product, Prodcat, Nutriscore


class Search:

    def __init__(self):
        self.result_info = {}
        self.categories = []

    def find_product(self, query):
        """ I search if the product exist in the DB
        In : the user request
        Act : searching in DB
        Out : an object product
        """
        try:
            result = Product.objects.filter(prod_name__icontains=query)
        except Exception as error:
            exception = f"Il y a l'erreur suivante : {error}."
            return exception

        if not result:
            return result
        else:
            # I take the first result
            result = result[0]
            return result

    def find_substitute(self, product):
        """ I'm the algorithm.
        In : an object product
        Act : searching substitute in the same category with better nutriscore
        Out : a list of product (in a QuerySet)
        """
        nutriscore = product.nut_id.nut_id
        categorie = Prodcat.objects.filter(prod_id=product.prod_id)[0]

        product_list = Product.objects.filter(prodcat__cat_id=categorie.cat_id).filter(
            nut_id__lte=(nutriscore - 1)).order_by('nut_id', 'prod_name').values_list()[:10]

        return product_list

    def result_infos(self, queryset):
        """ I create the result
        In : List of product (in a QuerySet)
        Act : creating a list of dictionary
        Out : a list of dictionary
        """
        result_info = []

        for product in queryset:
            prod_id = product[0]
            prod_name = product[1].capitalize()
            prod_url = product[2]
            prod_image = product[3]
            nutriscore = Nutriscore.objects.get(nut_id=product[4]).nut_type

            result_info.append({'prod_id': prod_id, 'prod_name': prod_name,
                               'prod_url': prod_url, 'prod_image': prod_image, 'nutriscore': nutriscore})

        return result_info

    def product_infos(self, object):
        """ I extract the informations that I need.
        In : a product object
        Act : extracting informations
        Out : a dictionary with the informations
        """
        result = object
        product_info = {}
        prod_id = result.prod_id
        prod_name = result.prod_name
        prod_image = result.prod_image
        nutriscore = result.nut_id.nut_type
        categorie_list = Prodcat.objects.filter(prod_id=result.prod_id)
        for categorie in categorie_list:
            categorie = categorie.cat_id.cat_name
            self.categories.append(categorie)

        product_info = {'prod_id': prod_id, 'prod_name': prod_name,
                        'prod_image': prod_image, 'nutriscore': nutriscore, 'categories': self.categories}

        return product_info
