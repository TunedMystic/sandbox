from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Company


class CompanyViewTestCases(TestCase):
    def setUp(self):
        Company.objects.bulk_create([
            Company(
                name='FinTech',
                description='Finance Technology as a Service',
                website='fintech.com'
            ),
            Company(
                name='Tweetr',
                description='Microblogging for ppl',
                website='tweetr.com'
            ),
        ])

    def test_company_list(self):
        url = reverse('company-list')
        response = self.client.get(url)

        # Check the status code of the Company List View.
        self.assertEqual(response.status_code, 200)

        # Check the contents of the template context.
        companies_count = response.context['companies'].count()
        self.assertEqual(companies_count, 5)
