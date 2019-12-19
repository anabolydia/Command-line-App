import click

import requests

# the APIkey you got from newsApi.org
API_KEY = '89c73c0b1b0f42639844b29ad695ef0b'


@click.group()
def main():
    """
    NewsApp is a command line Application that consumes the newsAPI
    that gives a user a list of 4 news sources from which a user chooses one,
    Then from your choice it returns a list of the top 10 headlines,
    The news headline has a title, description and a url in case the user needs to follow up
    The user also needs to have a valid news api created from http://www.newsapi.org
    """
    pass


@main.command()

def listsources():
    """ Lists 4 news sources from the newsAPI """
    main_url = " https://newsapi.org/v2/sources?apiKey=89c73c0b1b0f42639844b29ad695ef0b"

    # fetching data in json format
    open_source = requests.get(main_url).json()

    # getting all articles in a string sources
    source = open_source["sources"]

    # empty list which will
    # contain all trending news sources
    results = []

    for s in source:
        results.append(s["id"])

    for i in results[0:4]:
        print(i)


@main.command()
def topheadlines():
    """ Enter your choice from the list of news sources """
    news_source = click.prompt("Please enter your choice from the news_list")

    main_url = "https://newsapi.org/v2/top-headlines?apiKey=&sources=89c73c0b1b0f42639844b29ad695ef0b" + news_source

    # fetching data in json format
    open_headline = requests.get(main_url).json()

    # getting all headlines in a string articles
    article = open_headline['articles']

    # empty list which will
    # contain all trending newsSources
    output = []

    for articles in article:
        click.echo('\n')
        click.echo(click.style('TITLE: ' + articles['title'], fg='green'))
        click.echo(click.wrap_text(articles['description']))
        click.echo(click.style('DOMAIN: ' + articles['url'], fg='blue'))

    for i in output[:11]:
        print(i)

    if __name__ == '__main__':
        main()