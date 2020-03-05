from tethys_sdk.base import TethysAppBase, url_map_maker


class About(TethysAppBase):
    """
    Tethys app class for About.
    """

    name = 'About'
    index = 'about:home'
    icon = 'about/images/icon.gif'
    package = 'about'
    root_url = 'about'
    color = '#8e44ad'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

     def url_maps(self):
	        """
	        Add controllers
	        """
	        UrlMap = url_map_maker(self.root_url)

	        url_maps = (
	            UrlMap(
	                name='home',
	                url='about',
	                controller='about.controllers.home'
	            )
	        )


        return url_maps
