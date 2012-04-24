# Authors: Andrea D'Este <andrea.deste@redomino.com>
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

from zope.interface import Interface
from zope.interface import implements       
                                                    
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider                    
from Products.CMFCore.utils import getToolByName  
from zope.component import getMultiAdapter
from zope import schema                    
from zope.formlib import form            
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
                 
from redomino.social import _
                                                    
from zope.i18nmessageid import MessageFactory  
__ = MessageFactory("plone")       
                                         
class ISocialPortlet(IPortletDataProvider):
    """A portlet                         
                                           
    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the     
    same.    
    """                                                                       
                                                                              
#    portlet_title = schema.TextLine(title=__(u'Title'),                       
#                                  description=_(u'...'),                      
#                                  required=True,                              
#                                  default=u'')                                
                                                                              
class Assignment(base.Assignment):                                            
    """Portlet assignment.                                                    
                                                                              
    This is what is actually managed through the portlets UI and associated   
    with columns.                                                             
    """                                                                       
                                                                              
    implements(ISocialPortlet)                                              
#    portlet_title = u""                                                       
#                                                                              
#                                                                              
#    def __init__(self, portlet_title=u''):
#        self.portlet_title = portlet_title

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return _(u"Social Portlet")


class Renderer(base.Renderer):
    """Portlet renderer """
    render = ViewPageTemplateFile('socialportlet.pt')

    def __init__(self, context, request, view, manager, data):
        base.Renderer.__init__(self, context, request, view, manager, data)
        self.membership = getToolByName(self.context, 'portal_membership')
        self.portal_state = getMultiAdapter((context, request), name=u'plone_portal_state')
        urltool = getToolByName(context, "portal_url")
        self.portal  = urltool.getPortalObject()
        
        pp = getToolByName(context, 'portal_properties')
        self.sheet = getattr(pp, 'sc_social_likes_properties', None)


        self.enabled_portal_types = self.sheet.getProperty("enabled_portal_types", [])
        self.typebutton = self.sheet.getProperty("typebutton", "")
        self.twitter_enabled = self.sheet.getProperty("twitter_enabled", True)
        self.twittvia = self.sheet.getProperty("twittvia", "")
        self.fb_enabled = self.sheet.getProperty("fb_enabled", True)
        self.fbaction = self.sheet.getProperty("fbaction", "")
        self.fbadmins = self.sheet.getProperty("fbadmins", "")
        self.gp_enabled = self.sheet.getProperty("gp_enabled", True)
        self.linkedin_enabled = self.sheet.getProperty("linkedin_enabled", True)
        self.pinterest_enabled = self.sheet.getProperty("pinterest_enabled", True)

    @property
    def title(self):
        """return title of feed for portlet"""
        return getattr(self.data, 'portlet_title', '')

    def isAnon(self):
        """ return True if member is Anonymous"""
        if not self.portal_state.anonymous():
            return False
        return True

    @property
    def available(self):
        context = self.context
        enabled_portal_types = self.enabled_portal_types
        return context.portal_type in enabled_portal_types

    def classes(self):
        return "portlet portletSocialPortlet %s" % self.typebutton

class AddForm(base.NullAddForm):
    """Portlet add form. """

    def create(self):
        return Assignment()
