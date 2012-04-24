from sc.social.like.browser.viewlets import SocialMetadataViewlet as OriginalSocialMetadataViewlet

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class SocialMetadataViewlet(OriginalSocialMetadataViewlet):
    """Viewlet used to insert metadata into page header
    """
    render = ViewPageTemplateFile("metadata.pt")

    def __init__(self, context, request, view, manager):
        super(SocialMetadataViewlet, self).__init__(context, request, view, manager)
        if self.sheet:
            self.linkedin_enabled = self.sheet.getProperty("linkedin_enabled", True)
            self.pinterest_enabled = self.sheet.getProperty("pinterest_enabled", True)

