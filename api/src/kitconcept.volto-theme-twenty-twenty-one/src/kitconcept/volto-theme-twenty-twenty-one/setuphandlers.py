# -*- coding: utf-8 -*-
from kitconcept.contentcreator.creator import create_item_runner
from kitconcept.contentcreator.creator import load_json
from plone import api
from plone.app.portlets.utils import assignment_mapping_from_key
from plone.portlets.constants import CONTEXT_CATEGORY
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces import INonInstallable
from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.component import queryUtility
from zope.component.interfaces import IFactory
from zope.container.interfaces import INameChooser
from zope.interface import implementer
from plone.app.multilingual.browser.setup import SetupMultilingualSite

import os


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            "kitconcept.volto-theme-twenty-twenty-one:uninstall"
        ]


def change_content_type_title(portal, old_name, new_name):
    """
        change_content_type_title(portal, 'News Item', 'Meldung')
    """
    portal_types = getToolByName(portal, "portal_types")
    news_item_fti = getattr(portal_types, old_name)
    news_item_fti.title = new_name


def disable_content_type(portal, fti_id):
    portal_types = getToolByName(portal, "portal_types")
    document_fti = getattr(portal_types, fti_id)
    document_fti.global_allow = False


def enable_content_type(portal, fti_id):
    portal_types = getToolByName(portal, "portal_types")
    document_fti = getattr(portal_types, fti_id)
    document_fti.global_allow = True


def copy_content_type(portal, name, newid, newname):
    """Create a new content type by copying an existing one
    """
    portal_types = getToolByName(portal, "portal_types")
    tmp_obj = portal_types.manage_copyObjects([name])
    tmp_obj = portal_types.manage_pasteObjects(tmp_obj)
    tmp_id = tmp_obj[0]["new_id"]
    new_type_fti = getattr(portal_types, tmp_id)
    new_type_fti.title = newname
    portal_types.manage_renameObjects([tmp_id], [newid])


def post_install(context):
    """Post install script"""

    portal = api.portal.get()

    # indexes (dropdown navigation / leadimage)
    # wanted_indexes = (
    #     ('exclude_from_nav', 'BooleanIndex'),
    # )
    # add_catalog_indexes(context, wanted=wanted_indexes)

    # Remove front-page from nav
    if "front-page" in portal:
        portal["front-page"].exclude_from_nav = True
        portal["front-page"].reindexObject()

    # Setup the plone.app.multilingual data
    # sms = SetupMultilingualSite(portal)
    # sms.setupSite(portal)


def import_content(context):
    """Import example content"""

    portal = api.portal.get()

    # users
    api.user.create(
        email="stollenwerk@kitconcept.com",
        username="timo",
        password="welcome",
        roles=("Manager",),
        properties=None,
    )

    users = []
    for user in users:
        api.user.create(
            email="no-reply@example.com",
            username=user,
            password="welcome2exzellenz",
            roles=("Site Administrator",),
            properties=None,
        )

    # enable content non-globally addable types just for initial content
    # creation
    TEMP_ENABLE_CONTENT_TYPES = []
    for content_type in TEMP_ENABLE_CONTENT_TYPES:
        enable_content_type(portal, content_type)

    # content
    # content_structure = load_json("content.json", __file__)

    create_item_runner(
        api.portal.get(),
        content_structure,
        default_lang="de",
        default_wf_state="external",
        base_image_path=os.path.join(os.path.dirname(__file__), "example"),
    )

    # Delete Plone content
    if "Members" in portal.objectIds():
        api.content.delete(obj=portal["Members"])
    if "news" in portal.objectIds():
        api.content.delete(obj=portal["news"])
    if "events" in portal.objectIds():
        api.content.delete(obj=portal["events"])
    # if 'front-page' in portal.objectIds():
    #     api.content.delete(obj=portal['front-page'])

    # Set permissions for a folder
    # portal['interner-bereich'].manage_setLocalRoles('Authenticated Users', ['Reader', ]) # noqa

    # disable again content non-globally addable types just for initial content
    # creation
    for content_type in TEMP_ENABLE_CONTENT_TYPES:
        disable_content_type(portal, content_type)


def testing_content(context):
    """Content for the testing gs profile
    """
    portal = api.portal.get()

    # enable content non-globally addable types just for initial content
    # creation
    TEMP_ENABLE_CONTENT_TYPES = []
    for content_type in TEMP_ENABLE_CONTENT_TYPES:
        enable_content_type(portal, content_type)

    objects = [
        # portal.de,
        # portal.en,
        # api.content.create(
        #     container=portal.de, type="Blog", id="aktuelles", title="HU Unterwegs"
        # ),
        # api.content.create(
        #     container=portal.de, type="Fragen", id="fragen", title="Fragen"
        # ),
        # api.content.create(
        #     container=portal.de, type="Menschen", id="menschen", title="Menschen"
        # ),
        # api.content.create(container=portal.en, type="Blog", id="news", title="News"),
        # api.content.create(
        #     container=portal.en, type="Fragen", id="questions", title="Questions"
        # ),
        # api.content.create(
        #     container=portal.en, type="Menschen", id="people", title="People"
        # ),
    ]
    for obj in objects:
        api.content.transition(obj=obj, transition="publish_externally")


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def add_catalog_indexes(context, wanted=None):
    """Method to add our wanted indexes to the portal_catalog.
    """
    catalog = api.portal.get_tool("portal_catalog")
    indexes = catalog.indexes()
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
    if len(indexables) > 0:
        catalog.manage_reindexIndex(ids=indexables)


def setupNavigationPortlet(
    context,
    name="",
    root=None,
    includeTop=False,
    currentFolderOnly=False,
    bottomLevel=0,
    topLevel=0,
):
    """
        setupNavigationPortlet(portal['vereinigungen']['fachliche-vereinigungen']['sektion-materie-und-kosmos']['gravitation-und-relativitaetstheorie']) # noqa
    """
    from plone.app.portlets.portlets.navigation import (
        Assignment as NavAssignment,
    )  # noqa

    target_manager = queryUtility(
        IPortletManager, name="plone.leftcolumn", context=context
    )
    target_manager_assignments = getMultiAdapter(
        (context, target_manager), IPortletAssignmentMapping
    )

    navtree = NavAssignment(
        includeTop=includeTop,
        currentFolderOnly=currentFolderOnly,
        bottomLevel=bottomLevel,
        topLevel=topLevel,
    )

    if "navigation" not in target_manager_assignments.keys():
        target_manager_assignments["navigation"] = navtree


def setupPortletAt(portal, portlet_type, manager, path, name="", **kw):
    """
        setupPortletAt(portal, 'portlets.Events', 'plone.rightcolumn', '/vereinigungen/fachliche-vereinigungen/sektion-kondensierte-materie/halbleiterphysik') # noqa
    """
    portlet_factory = getUtility(IFactory, name=portlet_type)
    assignment = portlet_factory(**kw)
    mapping = assignment_mapping_from_key(
        portal, manager, CONTEXT_CATEGORY, path, create=True
    )

    if not name:
        chooser = INameChooser(mapping)
        name = chooser.chooseName(None, assignment)

    mapping[name] = assignment
