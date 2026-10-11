# -*- coding: utf-8 -*-
"""configure.zcml includes every package of the iA.Docs instance."""
from collective.transmogrifier.interfaces import ISectionBlueprint
from imio.dms.policy.testing import IMIO_DMS_POLICY_INTEGRATION_TESTING
from zc.z3monitor.interfaces import IZ3MonitorPlugin
from zope.component import getGlobalSiteManager
from zope.component import queryUtility
from zope.processlifetime import IDatabaseOpenedWithRoot
from ZServer.medusa.http_server import http_request

import collective.usernamelogger
import five.z2monitor
import unittest


class TestConfigure(unittest.TestCase):

    layer = IMIO_DMS_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]

    def assertProfile(self, profile_id):
        profile_ids = [info["id"] for info in self.portal.portal_setup.listProfileInfo()]
        self.assertIn(profile_id, profile_ids)

    def assertMonitorPlugins(self, *names):
        for name in names:
            self.assertIsNotNone(queryUtility(IZ3MonitorPlugin, name), name)

    def test_collective_iconifieddocumentactions(self):
        self.assertProfile("collective.iconifieddocumentactions:default")

    def test_imio_dms_mail(self):
        self.assertProfile("imio.dms.mail:default")

    def test_collective_contact_importexport(self):
        self.assertProfile("collective.contact.importexport:default")

    def test_five_z2monitor(self):
        # the monitor server starts when the database opens (bind address in the product-config)
        handlers = [
            reg.handler
            for reg in getGlobalSiteManager().registeredHandlers()
            if tuple(reg.required) == (IDatabaseOpenedWithRoot,)
        ]
        self.assertIn(five.z2monitor.initialize, handlers)

    def test_ftw_labels(self):
        self.assertProfile("ftw.labels:default")

    def test_imio_transmogrifier_contact(self):
        self.assertIsNotNone(
            queryUtility(ISectionBlueprint, "imio.transmogrifier.contact.plonegrouporganizationpath")
        )

    def test_imio_transmogrifier_iadocs(self):
        self.assertIsNotNone(queryUtility(ISectionBlueprint, "imio.transmogrifier.iadocs.a_service_update"))

    def test_products_znagios(self):
        self.assertMonitorPlugins("uptime", "dbsize", "objectcount", "errorcount", "stats")

    def test_zc_z3monitor(self):
        self.assertMonitorPlugins("monitor", "dbinfo")

    def test_collective_monitor(self):
        self.assertMonitorPlugins("health_ok", "health_db_connected", "count_users", "last_login_time")

    def test_collective_usernamelogger(self):
        # the ZServer access log (Z2.log) records the user name of the __ac cookie
        self.assertIs(http_request.__dict__["log"], collective.usernamelogger.log)
