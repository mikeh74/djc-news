from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import NewsPluginModel, News, NewsCategory
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin  # register the plugin
class NewsPluginPublisher(CMSPluginBase):

    model = NewsPluginModel  # model where plugin data are saved
    module = _("News")
    name = _("News Plugin")  # name of the plugin in the interface
    render_template = "news/news_plugin.html"

    def render(self, context, instance, placeholder):
        # model = self.model

        news_list = News.objects.filter(category=instance.category.id).order_by('-pub_date')[:instance.items_to_show]

        context.update({'instance': instance, 'news_list': news_list})
        return context