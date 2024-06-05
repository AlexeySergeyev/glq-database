# Path: lenses/tests.py
import unittest
from django.test import RequestFactory
from django.test import TestCase
from django.contrib import admin
from lenses.models import GLObject
from lenses.admin import GlObjectAdmin
from lenses.views import main, index, search, links, contacts, detail

class GLObjectTestCase(TestCase):
    """
    Test case for the GLObject model.
    """

    def setUp(self):
        """
        Set up the test case by creating a GLObject instance.
        """
        self.globject = GLObject.objects.create(
            gl_name='Test Object',
            gl_alpha=10.12345,
            gl_delta=20.54321,
            l_redshift=0.5,
            q_redshift=0.3,
            ang_sep=0.2,
            time_delay=1.5,
            gl_url='http://example.com',
            gl_image='image.jpg'
        )

    def test_c_count(self):
        """
        Test the c_count method of GLObject.
        """
        self.assertEqual(self.globject.c_count(), 0)

    def test_max_sep(self):
        """
        Test the max_sep method of GLObject.
        """
        self.assertEqual(self.globject.max_sep(), '0.00')

    def test_gl_ra(self):
        """
        Test the gl_ra method of GLObject.
        """
        self.assertEqual(self.globject.gl_ra(), '00:40:49.63')

    def test_gl_dec(self):
        """
        Test the gl_dec method of GLObject.
        """
        self.assertEqual(self.globject.gl_dec(), '+20:32:35.56')

    def test_max_mag(self):
        """
        Test the max_mag method of GLObject.
        """
        self.assertEqual(self.globject.max_mag(), 0.0)

    def test_min_mag(self):
        """
        Test the min_mag method of GLObject.
        """
        self.assertEqual(self.globject.min_mag(), 0.0)

    def test_gal_mag(self):
        """
        Test the gal_mag method of GLObject.
        """
        self.assertEqual(self.globject.gal_mag(), 0.0)

    def test_str(self):
        """
        Test the __str__ method of GLObject.
        """
        self.assertEqual(str(self.globject), 'Test Object')

    def test_meta_ordering(self):
        """
        Test the ordering of GLObject's meta class.
        """
        self.assertEqual(GLObject._meta.ordering, ['gl_alpha'])

class GlObjectAdminTests(unittest.TestCase):
    """
    Test case for the GlObjectAdmin class.
    """

    def setUp(self):
        """
        Set up the test case by creating a GlObjectAdmin instance.
        """
        self.admin = GlObjectAdmin(GLObject, admin.site)

    def test_list_display(self):
        """
        Test the list_display attribute of GlObjectAdmin.
        """
        expected_list_display = ('gl_name', 'gl_ra', 'gl_dec')
        self.assertEqual(self.admin.list_display, expected_list_display)

    def test_model(self):
        """
        Test the model attribute of GlObjectAdmin.
        """
        self.assertEqual(self.admin.model, GLObject)

    def test_list_per_page(self):
        """
        Test the list_per_page attribute of GlObjectAdmin.
        """
        self.assertEqual(self.admin.list_per_page, 20)

    def test_inlines(self):
        """
        Test the inlines attribute of GlObjectAdmin.
        """
        expected_inlines = [GlComponentInline]
        self.assertEqual(self.admin.inlines, expected_inlines)

    def test_ordering(self):
        """
        Test the ordering attribute of GlObjectAdmin.
        """
        expected_ordering = ('gl_alpha',)
        self.assertEqual(self.admin.ordering, expected_ordering)

class IndexViewTests(unittest.TestCase):
    """
    Test case for the index views.
    """

    def setUp(self):
        """
        Set up the test case by creating a RequestFactory instance.
        """
        self.factory = RequestFactory()

    def test_main_view(self):
        """
        Test the main view.
        """
        request = self.factory.get('/')
        response = main(request)
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        """
        Test the index view.
        """
        request = self.factory.get('/table/')
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        """
        Test the search view.
        """
        request = self.factory.get('/search/')
        response = search(request)
        self.assertEqual(response.status_code, 200)

    def test_links_view(self):
        """
        Test the links view.
        """
        request = self.factory.get('/links/')
        response = links(request)
        self.assertEqual(response.status_code, 200)

    def test_contacts_view(self):
        """
        Test the contacts view.
        """
        request = self.factory.get('/contacts/')
        response = contacts(request)
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        """
        Test the detail view.
        """
        globject_id = 1  # Replace with an existing GLObject ID
        request = self.factory.get(f'/{globject_id}/')
        response = detail(request, globject_id=globject_id)
        self.assertEqual(response.status_code, 200)

    def test_index_view_pagination(self):
        """
        Test the pagination of the index view.
        """
        request = self.factory.get('/index/')
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lenses/index.html')
        self.assertIn('latest_gls_list', response.context)
        self.assertIsInstance(response.context['latest_gls_list'], Paginator)

if __name__ == '__main__':
    unittest.main()
