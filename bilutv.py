from getvideofromweb import BiluTV


if __name__=='__main__':
    bltv = BiluTV()

    url = "https://bilutv.org/phim-hai-sinh-menh-tap-1-14353.209765.html"
    # main_content = bltv.getMainContentFromUrl(url)
    # info = bltv.getInfoMovie(main_content)
    data = {
        'mo': 14353,
        'ep': 209765,
        'sv': 3
    }
    content = bltv.getContentFromUrl("POST", url, data)
    data = bltv.getDataForFindSourceVideo(content)
    # content = bltv.getContentFromData(data)
    # source_video = bltv.getSourceVideoFromContent(content)
    #
    # print(source_video)
    # print(source_video)