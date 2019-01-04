# -*- coding: utf-8 -*-
# third party modules
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('bp_index', __name__)

@bp.route('/')
def index():
    """To the index page."""
    return render_template('index.html')


