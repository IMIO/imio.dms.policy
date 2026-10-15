from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import imio.dms.policy


class ImioDmsPolicyLayer(PloneSandboxLayer):
    """Loads the policy ZCML, as the server.dmsmail instance."""

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=imio.dms.policy)


IMIO_DMS_POLICY_FIXTURE = ImioDmsPolicyLayer()

IMIO_DMS_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(IMIO_DMS_POLICY_FIXTURE,), name="ImioDmsPolicyLayer:IntegrationTesting"
)
