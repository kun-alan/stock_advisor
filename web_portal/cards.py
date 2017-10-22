import os

from bottle import template


class KwargsObj():
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


def fake_cards():
    return [
        KwargsObj(
            symbol='X', price='27.80', change='+0.34',
            percent_change='+2.34', color_class='color-plus'),
        KwargsObj(
            symbol='CLX', price='127.80', change='-0.54',
            percent_change='-0.54', color_class='color-minus'),
        KwargsObj(
            symbol='KLIC', price='21.80', change='-0.64',
            percent_change='-0.34', color_class='color-minus'),
        KwargsObj(
            symbol='CELG', price='121.80', change='0.00',
            percent_change='0.00', color_class='color-even'),
        KwargsObj(
            symbol='PG', price='75.40', change='0.00',
            percent_change='0.00', color_class='color-even'),
    ]


def render_stock_cards(cards):
    return [
        template(
            os.path.dirname(__file__) + '/templates/stock_card.tpl',
            card=card,
        )
        for card in cards
    ]
