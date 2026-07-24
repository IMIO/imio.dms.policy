# -*- coding: utf-8 -*-
"""Env-gated dev tweak to collective.collabora, kept out of that pristine upstream.

Localhost dev bypass (COLLABORA_DEV_MODE only): collective.collabora refuses a
``plone_server_url`` on localhost/127.0.0.1, because a containerized Collabora
would then reach itself. Our dev container runs with ``network_mode: host``
(docker/docker-compose.yaml), so localhost IS the host's Plone and the guard is
a false positive. Production never sets COLLABORA_DEV_MODE, so the upstream
protection stays intact there.

The always-on "field shadings by default" behaviour is NOT here anymore: it is
a viewlet in imio.dms.mail (CollaboraFieldShadingsViewlet), registered under a
``zcml:condition`` on collective.collabora.
"""
from logging import getLogger

import os


logger = getLogger(__name__)


def apply():
    if not os.environ.get("COLLABORA_DEV_MODE"):
        return
    try:
        from collective.collabora.browser.edit import CollaboraEditView
    except ImportError:
        logger.debug("collective.collabora not available; skipping dev patch.")
        return
    _allow_localhost_dev(CollaboraEditView)


def _allow_localhost_dev(CollaboraEditView):
    from future.utils import bytes_to_native_str as n
    from plone import api
    from plone.memoize.view import memoize

    def plone_server_url(self):
        """Same as upstream, minus the localhost guard (dev-only)."""
        return (
            api.portal.get_registry_record(
                n(b"collective.collabora.plone_server_url"), default=None
            )
            or self.portal_url
        )

    CollaboraEditView.plone_server_url = property(memoize(plone_server_url))
    logger.warning(
        "COLLABORA_DEV_MODE set: allowing localhost plone_server_url "
        "(dev only, network_mode: host)."
    )
