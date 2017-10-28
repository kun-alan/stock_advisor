import os

from bottle import template

from stock_watcher import processor as watcher_processor
# from stock_recommender import processor as recommender_processor


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
                'text': 'Evt',
                'processor': watcher_processor.event,
                'type': 'card-3'
            },
            'history': {
                'text': 'Hst',
                'processor': watcher_processor.history,
                'type': 'card-3',
            },
        },
    },
    'recommender': {
        'text': 'Recommender',
        'subtabs': {
            'card': {
                'text': 'Card',
                'processor': watcher_processor.event,
                'type': 'card-3'
            },
            'table': {
                'text': 'Table',
                'processor': watcher_processor.event,
                'type': 'table-3',
            },
        },
    },
}


def process_tab(selected_tab, selected_subtab):

    tabs_to_render = []
    subtabs_to_render = []

    processor = None
    for tab, tab_dict in tabs.items():
        tab_to_render = {
            'href': tab,
            'text': tab_dict['text'],
        }

        if tab == selected_tab:
            tab_to_render['active'] = ' is-active'

            for subtab, subtab_dict in tab_dict['subtabs'].items():
                subtab_to_render = {
                    'href': '/{}/{}'.format(tab, subtab),
                    'text': subtab_dict['text'],
                }
                if subtab == selected_subtab:
                    subtab_to_render['active'] = ' is-active'
                    processor = subtab_dict['processor']
                else:
                    subtab_to_render['active'] = ''
                subtabs_to_render.append(subtab_to_render)

        else:
            tab_to_render['active'] = ''

        tabs_to_render.append(tab_to_render)

    rendered_tabs = render_tabs(
        dicts_to_kwargs_objs(tabs_to_render),
        dicts_to_kwargs_objs(subtabs_to_render)
    )
    rendered_payload = render_payload(processor)

    return rendered_tabs, rendered_payload


def render_tabs(tabs_to_render, subtabs_to_render):
    return template(
        os.path.dirname(__file__) + '/templates/tabs.tpl',
        tabs=tabs_to_render,
        subtabs=subtabs_to_render
    )


def render_payload(processor):
    payload_data = dicts_to_kwargs_objs(processor())
    template_file = 'stock_cards.tpl'

    return template(
        os.path.dirname(__file__) + '/templates/' + template_file,
        data=payload_data,
    )
