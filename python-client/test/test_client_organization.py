"""
    Bundestag: Lobbyregister

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.3
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.bundestag_lobbyregister.model.address import Address
from deutschland.bundestag_lobbyregister.model.legal_form import LegalForm
from deutschland.bundestag_lobbyregister.model.legal_representative import (
    LegalRepresentative,
)

from deutschland import bundestag_lobbyregister

globals()["Address"] = Address
globals()["LegalForm"] = LegalForm
globals()["LegalRepresentative"] = LegalRepresentative
from deutschland.bundestag_lobbyregister.model.client_organization import (
    ClientOrganization,
)


class TestClientOrganization(unittest.TestCase):
    """ClientOrganization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClientOrganization(self):
        """Test ClientOrganization"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClientOrganization()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()