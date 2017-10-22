import os

from bottle import template

from stock_advisor.web_portal import cards


def process_tab(selected_tab):
    tabs = [
        cards.KwargsObj(
            text='Watcher',
            href='watcher',
            processor=process_watcher
        ),
        cards.KwargsObj(
            text='Recommender',
            href='recommender',
            processor=process_recommender
        ),
    ]

    process_and_render_cards = None
    for tab in tabs:
        if tab.href == selected_tab:
            tab.active = ' is-active'
            process_and_render_cards = tab.processor
        else:
            tab.active = ''

    return render_tabs(tabs), process_and_render_cards()


def process_watcher():
    fake_cards = cards.fake_cards()
    return cards.render_stock_cards(fake_cards)


def process_recommender():
    fake_cards = cards.fake_cards()
    fake_cards = fake_cards[-1:] + fake_cards[:-1]
    return cards.render_stock_cards(fake_cards)


def render_tabs(tabs):
    return [
        template(
            os.path.dirname(__file__) + '/templates/tab.tpl',
            tab=tab
        )
        for tab in tabs
    ]
