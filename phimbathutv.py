from getvideofromweb import PhimBatHu


if __name__=='__main__':
    pbh = PhimBatHu()

    url = "https://phimbathutv.com/phim/luat-su-bat-bai-ligalhai-9500/"
    main_content = pbh.getMainContentFromUrl(url)
    info = pbh.getInfoMovie(main_content)
    data = pbh.getDataForFindSourceVideo(main_content, url)
    content = pbh.getContentFromData(data)
    source_video = pbh.getSourceVideoFromContent(content)

    print(source_video)
    # print(source_video)