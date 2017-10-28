import os

from flask import render_template

from stock_watcher import processor as watcher_processor
from stock_recommender import processor as recommender_processor


class KwargsObj():
    def __init__(self, **kwargs):
        self.__dict__ = kwargs


def dicts_to_kwargs_objs(dicts):
    return [KwargsObj(**data) for data in dicts]


tabs = {
    'watcher': {
        'text': 'Watcher',
        'subtabs': {
            'event_cards': {
                'text': 'Event',
                'processor': watcher_processor.event,
                'template': 'watcher_cards'
            },
            'history': {
                'text': 'History',
                'processor': watcher_processor.history,
                'template': 'watcher_cards'
            },
        },
    },
    'recommender': {
        'text': 'Recommender',
        'subtabs': {
            'card': {
                'text': 'Bollinger',
                'processor': recommender_processor.bollinger,
                'template': 'recommender_table'
            },
            'table': {
                'text': 'Volatility',
                'processor': recommender_processor.volatility,
                'template': 'recommender_table'
            },
        },
    },
}


def process_tab(selected_tab, selected_subtab):

    tabs_to_render = []
    subtabs_to_render = []

    processor = None
    template = None
    for tab, tab_dict in tabs.items():
        tab_to_render = {
            'id': tab,
            'text': tab_dict['text'],
            'current': ' ',
        }

        subtabs_to_render = []

        for subtab, subtab_dict in tab_dict['subtabs'].items():
            if tab == selected_tab and subtab == selected_subtab:
                processor = subtab_dict['processor']
                template = subtab_dict['template']
                tab_to_render['current'] = subtab_dict['text']

            subtab_to_render = {
                'href': '/{}/{}'.format(tab, subtab),
                'text': subtab_dict['text'],
            }
            subtabs_to_render.append(subtab_to_render)

        tab_to_render['subtabs'] = subtabs_to_render
        tabs_to_render.append(tab_to_render)

    return render_tabs(tabs_to_render), render_payload(processor, template)


def render_tabs(tabs_to_render):
    return render_template(
        'tabs.html',
        tabs=tabs_to_render,
    )


def render_payload(processor, template):
    return render_template(
        template + '.html',
        data=processor(),
    )
