from GetVideoFromWeb import GetVideoFromWeb as MainWeb
from GetVideoFromWeb import PhimBatHu


if __name__=='__main__':
    pbh = PhimBatHu()

    url = "https://phimbathutv.com/phim/vuong-hau-cuoi-cung-9486/"
    main_content = pbh.getMainContentFromUrl(url)
    info = pbh.getInfoMovie(main_content)
    data = pbh.getDataForFindSourceVideo(main_content, url)
    content = pbh.getContentFromData(data)
    source_video = pbh.getSourceVideoFromContent(content)

    print(info)
    print(source_video)