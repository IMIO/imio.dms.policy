"""configure.zcml includes every package of the iA.Docs instance."""

from collective.transmogrifier.interfaces import ISectionBlueprint
from imio.dms.policy.testing import IMIO_DMS_POLICY_INTEGRATION_TESTING
from zope.component import queryUtility

import unittest


class TestConfigure(unittest.TestCase):

    layer = IMIO_DMS_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]

    def assertProfile(self, profile_id):
        profile_ids = [info["id"] for info in self.portal.portal_setup.listProfileInfo()]
        self.assertIn(profile_id, profile_ids)

    def test_imio_dms_mail(self):
        self.assertProfile("imio.dms.mail:default")

    def test_collective_contact_importexport(self):
        self.assertProfile("collective.contact.importexport:default")

    def test_collective_labels(self):
        # personal labels (ftw.labels on Plone 4), included by imio.dms.mail
        self.assertProfile("collective.labels:default")

    def test_imio_transmogrifier_contact(self):
        self.assertIsNotNone(queryUtility(ISectionBlueprint, "imio.transmogrifier.contact.plonegrouporganizationpath"))

    def test_imio_transmogrifier_iadocs(self):
        self.assertIsNotNone(queryUtility(ISectionBlueprint, "imio.transmogrifier.iadocs.a_service_update"))
