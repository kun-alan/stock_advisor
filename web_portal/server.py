#!/usr/bin/env python
import os

from bottle import run, route, request, template, static_file

from stock_advisor.web_portal import tabs


@route('/static/<filepath:path>')
def server_static(filepath):
    static_path = os.path.dirname(__file__) + '/static/'
    return static_file(filepath, root=static_path)


@route('/', method='GET')
def index():
    return home_page('watcher', 'event_cards')


@route('/selected_tab>/<selected_subtab>', method='GET')
def index(selected_tab, selected_subtab):
    return home_page(selected_tab, selected_subtab)


def home_page(selected_tab, selected_subtab):
    rendered_tabs, rendered_payload = tabs.process_tab(
        selected_tab, selected_subtab)

    return template(
        os.path.dirname(__file__) + '/templates/index.tpl',
        tabs=rendered_tabs,
        payload=rendered_payload,
    )


if __name__=='__main__':
    run(host='localhost', port=8000, debug=True)
