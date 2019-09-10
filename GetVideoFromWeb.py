import urllib3
import certifi
import re
from lxml import html
from bs4 import BeautifulSoup
import json


class GetVideoFromWeb:
    # Get video from website
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())

    def getContentFromUrl(self, method, url, data={}):
        req = self.http.request(method, url, fields=data)

        return req.data

    def getDataByRegex(self, content, req=r'deep_link/(.*?)\?url'):
        arr = re.findall(req, str(content))

        if len(arr) > 0:
            return arr

        return []

    def buildHtmlFromContent(self, content):
        soup = BeautifulSoup(content, "lxml")

        return soup

    def buildXpathFromContent(self, content):
        root = html.fromstring(content)

        return root

    def buildJsonFromContent(self, content):
        data = json.loads(content)

        return data


class PhimBatHu(GetVideoFromWeb):
    def getSourceVideoFromContent(self, content):
        arr_file = self.getDataByRegex(content, r'\"file\": \"(.*?)\"')
        len_file = len(arr_file)

        if len_file == 0:
            return ''

        if len_file == 1 and arr_file[0].endswith(".m3u8"):
            # doing later
            return ''

        if len_file == 1:
            return arr_file[0]

        return arr_file[1]

    def getDataForFindSourceVideo(self, url):
        next_episode = ''
        episode_id = ''
        content = self.getContentFromUrl("GET", url)

        film_id = self.getFilmId(url)
        episode = self.getEpisodeID(content)
        if len(episode) > 0:
            next_episode = episode[1]
            episode_id = episode[0]

        print(film_id)
        print(episode_id)
        print(next_episode)

    def getEpisodeID(self, content):
        root = self.buildXpathFromContent(content)

        li = root.xpath("//*[@id=\"body-wrapper\"]/div/div/div[2]/div[6]/div[1]/div[2]/ul/li")

        id = li[len(li) - 1].xpath("a/@id")
        next_id = li[len(li) - 1].xpath("a/text()")

        if len(id) > 0:
            return [id[0], next_id[0].replace("-End", "")]

        return []

    def getFilmId(self, url):
        arr = url.split("/")
        string_text = arr[len(arr) - 2]

        arr = string_text.split("-")

        return arr[len(arr) - 1]
