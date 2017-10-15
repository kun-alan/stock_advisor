#!/usr/bin/env python
import os

from bottle import run, route, request, template, static_file


@route('/static/<filepath:path>')
def server_static(filepath):
    static_path = os.path.dirname(__file__) + '/static/'
    return static_file(filepath, root=static_path)


@route('/', method='GET')
def index():
    return home_page('recommender')


@route('/recommender', method='GET')
def index():
    return home_page('recommender')


@route('/watcher', method='GET')
def index():
    return home_page('watcher')


def home_page(tab):
    return template(
        os.path.dirname(__file__) + '/templates/index.tpl',
        tab=tab
    )


if __name__=='__main__':
    run(host='localhost', port=8000, debug=True)
