from django.test import TestCase
from .models import Product


# Create your tests here.
class ProductTests(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Product model
    """

    def test_product_title(self):
        test_title = Product(title='A product')
        self.assertEqual(str(test_title), 'A product')

    def test_product_showcase(self):
        test_product = Product.objects.create(
            title="A product",
            price=99.99,
            size="L",
            description="A description.",
        )

        response = self.client.get(f"/products/product_showcase/{test_product.id}")
        self.assertEqual(response.status_code, 200)
