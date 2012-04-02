# Authors: Davide Moro <davide.moro@redomino.com>
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published
# by the Free Software Foundation.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.

from sc.social.like.controlpanel.likes import BaseControlPanelAdapter
from sc.social.like.controlpanel.likes import ProvidersControlPanel as OriginalProvidersControlPanel
from sc.social.like.controlpanel.likes import IProvidersSchema, ITwitterSchema, IFbSchema, IGpSchema, MultiSelectWidget
from sc.social.like.controlpanel.likes import baseset, twitterset, fbset, gpset

from zope.interface import Interface
from zope.schema import Bool
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from plone.fieldsets.fieldsets import FormFieldsets
from plone.app.controlpanel.form import ControlPanelForm
from sc.social.like import LikeMessageFactory as _
from zope.component import adapts
from zope.interface import implements

class ILinkedinSchema(Interface):
    """ Linkedin configurations """

    linkedin_enabled = Bool(
        title=_(u"Enable Linkedin button"),
        default=True,
        required=False,
        )

class LinkedinControlPanelAdapter(BaseControlPanelAdapter):
    """ Linkedin control panel adapter """
    adapts(IPloneSiteRoot)
    implements(ILinkedinSchema)

    linkedin_enabled = ProxyFieldProperty(ILinkedinSchema['linkedin_enabled'])

linkedinset = FormFieldsets(ILinkedinSchema)
linkedinset.id = 'linkedinset'
linkedinset.label = _(u'Linkedin settings')

class IPinterestSchema(Interface):
    """ Pinterest configurations """

    pinterest_enabled = Bool(
        title=_(u"Enable Pinterest button"),
        default=True,
        required=False,
        )

class PinterestControlPanelAdapter(BaseControlPanelAdapter):
    """ Pinterest control panel adapter """
    adapts(IPloneSiteRoot)
    implements(IPinterestSchema)

    pinterest_enabled = ProxyFieldProperty(IPinterestSchema['pinterest_enabled'])

pinterestset = FormFieldsets(IPinterestSchema)
pinterestset.id = 'pinterestset'
pinterestset.label = _(u'Pinterest settings')

class ProvidersControlPanel(OriginalProvidersControlPanel):
    """ """
    form_fields = FormFieldsets(baseset, twitterset, fbset, gpset, linkedinset, pinterestset)

    form_fields['enabled_portal_types'].custom_widget = MultiSelectWidget


