"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from GetBelleWomenIage import app
from GetBelleWomenIage.ImgClass.GetUserImg import GetJX3UserImg
from GetBelleWomenIage.ImgClass.GetYongGirlImg import GetYongYellowImg
import json
from GetBelleWomenIage.ImgClass.GetJX3DayFunction import GetJx3EveryDay
from GetBelleWomenIage.ImgClass.GetYellowCarNumber import GetYellowNumber

# @app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return GetJX3UserImg().JxeImageQuery()

@app.route('/yongGrilDongman')
def contact():
    """Renders the contact page."""
    return GetYongYellowImg().GetMaxAndMinPageUrl()


@app.route('/everyday')
def about():
    """Renders the about page."""
    return GetJx3EveryDay().GetEveryDay()
@app.route("/yellowImg")
def yellowImg():
    return GetYellowNumber().GetPageUrl()