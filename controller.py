from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup as bs
import data
import utils

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='hello jinja')

# 네이버 금융 페이지 1~33페이지까지 보면서 종목 이름과 코드 리턴.
# 코스피!!


@app.route('/crawingAllKospi')
def crawingAllKospiNameAndCode():
    res = utils.crawingAllKospiNameAndCode()
    data.makeTableWithNameColumn('KospiNameAndCode', ['code', 'name'])
    dbFormat = utils.makeDBFormat(res)
    data.insertNameAndCode("KospiNameAndCode", dbFormat)
    return "CrawingAllKospiNameAndCode Finish!"


@app.route('/crawingAllKosdaq')
def crawingAllKosdaqNameAndCode():
    res = utils.crawingAllKosdaqNameAndCode()
    data.makeTableWithNameColumn("KosdaqNameAndCode", ['code', 'name'])
    dbFormat = utils.makeDBFormat(res)
    data.insertNameAndCode("KosdaqNameAndCode", dbFormat)
    return "CrawingAllKosdaqNameAndCode Finish!"
