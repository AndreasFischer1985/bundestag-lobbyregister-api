"""
    Bundestag: Lobbyregister

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.3
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.bundestag_lobbyregister.model.address_country import AddressCountry

from deutschland import bundestag_lobbyregister

globals()["AddressCountry"] = AddressCountry
from deutschland.bundestag_lobbyregister.model.address import Address


class TestAddress(unittest.TestCase):
    """Address unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddress(self):
        """Test Address"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Address()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
