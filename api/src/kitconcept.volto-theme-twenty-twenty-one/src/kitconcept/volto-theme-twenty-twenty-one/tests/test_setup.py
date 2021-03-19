# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.CMFCore.utils import getToolByName
from kitconcept.volto-theme-twenty-twenty-one.testing import KITCONCEPT_volto-theme-twenty-twenty-one_INTEGRATION_TESTING  # noqa
from plone import api

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that kitconcept.volto-theme-twenty-twenty-one is properly installed."""

    layer = KITCONCEPT_volto-theme-twenty-twenty-one_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if kitconcept.volto-theme-twenty-twenty-one is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            "kitconcept.volto-theme-twenty-twenty-one"))

    # def test_plone_restapi_installed(self):
    #     self.assertTrue(
    #         self.installer.isProductInstalled(
    #             "plone.restapi"
    #         )
    #     )

    def test_browserlayer(self):
        """Test that IKitconceptvolto-theme-twenty-twenty-oneLayer is registered.""" # noqa
        from kitconcept.volto-theme-twenty-twenty-one.interfaces import (
            IKitconceptvolto-theme-twenty-twenty-oneLayer)
        from plone.browserlayer import utils
        self.assertIn(IKitconceptvolto-theme-twenty-twenty-oneLayer, utils.registered_layers()) # noqa


class TestUninstall(unittest.TestCase):

    layer = KITCONCEPT_volto-theme-twenty-twenty-one_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

        self.installer.uninstallProducts(["kitconcept.volto-theme-twenty-twenty-one"]) # noqa

    def test_product_uninstalled(self):
        """Test if kitconcept.volto-theme-twenty-twenty-one is cleanly uninstalled.""" # noqa
        self.assertFalse(self.installer.isProductInstalled(
            "kitconcept.volto-theme-twenty-twenty-one"))

    def test_browserlayer_removed(self):
        """Test that IKitconceptvolto-theme-twenty-twenty-oneLayer is removed.""" # noqa
        from kitconcept.volto-theme-twenty-twenty-one.interfaces import IKitconceptvolto-theme-twenty-twenty-oneLayer # noqa
        from plone.browserlayer import utils
        self.assertNotIn(IKitconceptvolto-theme-twenty-twenty-oneLayer, utils.registered_layers()) # noqa
