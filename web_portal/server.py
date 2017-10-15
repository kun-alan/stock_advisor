#!/usr/bin/env python
import os

from bottle import run, route, request, template, static_file


@route('/static/<filepath:path>')
def server_static(filepath):
    static_path = os.path.dirname(__file__) + '/static/'
    return static_file(filepath, root=static_path)


@route('/', method='GET')
def get():
    return template(
        os.path.dirname(__file__) + '/templates/index.tpl'
    )


if __name__=='__main__':
    run(host='localhost', port=8000, debug=True)
