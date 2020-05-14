import wikipedia as wiki

def get_summary(name):
    try:
        wiki.set_lang("ru")
        post = wiki.page(name)
        return "{0}\nБольше подробностей по ссылке - {1}".format(post.summary, post.url)
    except Exception:
        return "Страница не найдена"
