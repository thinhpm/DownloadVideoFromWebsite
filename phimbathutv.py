from GetVideoFromWeb import GetVideoFromWeb as MainWeb
from GetVideoFromWeb import PhimBatHu as pbh


if __name__=='__main__':
    main = pbh()
    url = "https://phimbathutv.com/ajax"
    method = "POST"
    data = {
        "NextEpisode": 1,
        "EpisodeID": 131909,
        "filmID": 9518,
        "playTech": "auto"
    }

    # content = main.getContentFromUrl(method, url, data)
    # arr_file = main.getSourceVideoFromContent(content)
    main.getDataForFindSourceVideo("https://phimbathutv.com/phim/nguoi-dep-gangnam-9518/xem-phim.html")