#!/usr/bin/env python
import os

from flask import Flask, render_template

from stock_advisor.web_portal import tabs


app = Flask(__name__)


@app.route('/')
def index():
    return home_page('watcher', 'event_cards')


@app.route('/<selected_tab>/<selected_subtab>')
def subtab(selected_tab, selected_subtab):
    return home_page(selected_tab, selected_subtab)


def home_page(selected_tab, selected_subtab):
    rendered_tabs, rendered_payload = tabs.process_tab(
        selected_tab, selected_subtab)

    return render_template(
        'index.html',
        tabs=rendered_tabs,
        payload=rendered_payload,
    )
