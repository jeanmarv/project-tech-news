from tech_news.database import find_news


# Requisito 10
def top_5_news():
    top_five = []
    results = find_news()
    sorted_data = sorted(
        results, key=lambda data: data["comments_count"], reverse=True
    )[:5]

    for itens in sorted_data:
        top_five.append((itens["title"], itens["url"]))

    return top_five


# Requisito 11
def top_5_categories():
    get_news = find_news()
    sum_categories = {}
    category_result = []

    for itens in get_news:
        if itens['category'] in sum_categories:
            sum_categories[itens['category']] += 1
        else:
            sum_categories[itens["category"]] = 0

    sort_categories = sorted(
        sum_categories.items(), key=lambda x: (-x[1], x[0]))

    for itens in sort_categories:
        category_result.append(itens[0])

    return category_result
