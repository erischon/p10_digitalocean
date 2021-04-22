from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_hp_look_great(self):

        # Lily a entendu parlé d'une application web qui permet de trouver des substituts alimentaires. Elle va y jeter un oeil en utilisant son navigateur web.
        self.browser.get('http://localhost:8000')

        # Elle voit qu'elle est au bon endroit en voyant le titre de la page.
        self.assertIn('The Substitute', self.browser.title)

        # Elle est satisfaite en lisant le slogan qui lui parle vraiment.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('DU GRAS OUI, MAIS DE QUALITÉ !', header_text)

        # Comme elle est curieuse, Lily commence par regarder tous les choix qui s'offrent à elle :

        # En haut de la page il y a un menu.
        navbar = self.browser.find_element_by_id('mainNav')

        # A gauche de ce menu elle voit le logo et le nom du site.
        logo = navbar.find_element_by_tag_name('img')
        self.assertIn('logo_pur_beurre.png', logo.get_attribute('src'))
        brand = navbar.find_element_by_class_name('navbar-brand').text
        self.assertIn('Pur Beurre', brand)

        # Au milieu elle voit un formulaire de recherche.
        form = navbar.find_element_by_id('product_search_form')

        # A droite elle voit un lien pour "Créer Mon Compte".
        link_mon_compte = navbar.find_element_by_id('link_mon_compte').text
        self.assertIn('Créer Mon Compte', link_mon_compte)

        # Et un autre pour se connecter
        link_login = navbar.find_element_by_id('link_login').text
        self.assertIn('Me connecter', link_login)

        # Dans la page, sous le titre et le sous-titre, elle découvre un formulaire de recherche.
        main_form = self.browser.find_element_by_id('main_product_search_form')

        # Plus bas elle lit l'histoire de Colette et de Rémy, les créateurs.
        about = self.browser.find_element_by_id('about')

        # Sous cette partie elle tombe sur les coordonnées de contact : un numéro de téléphone et un email.
        contact = self.browser.find_element_by_id('contact')
        self.assertIn('06 77 55 11 99', contact.find_element_by_id('phone_number').text)
        self.assertIn('contact@purbeurre.com', contact.find_element_by_id('contact_email').text)

        # Pour finir en bas de la page elle trouve les mentions légales ainsi qu'un lien vers la partie contact (qui est juste au-dessus en faite).
        footer = self.browser.find_element_by_id('footer')
        self.assertIn('Mentions légales', footer.find_element_by_id('link_mentions_legales').text)
        self.assertIn('Contact', footer.find_element_by_id('link_contact').text)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
