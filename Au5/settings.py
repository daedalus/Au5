# Scrapy settings for labanca project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Au5'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['Au5.spiders']
NEWSPIDER_MODULE = 'Au5.spiders'
USER_AGENT = f'{BOT_NAME}/{BOT_VERSION}'

