from flask import Flask, request

from flask import jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

newsLink=[]


@app.route('/')
def hello_world():
    return 'Hello World!'



@app.route("/hello")
def newHello():
    return "{'HH':'VV'}"




@app.route('/catch')
def catchCtbu():
    response = requests.get('http://news2014.ctbu.edu.cn/zyxw.htm')
    response.encoding = 'utf-8'
    bs = BeautifulSoup(response.text, 'lxml')
    node = bs.select(".global_tx_list4a")
    link = node[0].find_all("a")
    title_len = len(link)
    mytitle=[]
    for i in range(title_len):
      mytitle.append(link[i].text)
    for i in link:
      if str(i.get('href'))[:4] == 'info':
       newsLink.append('http://news2014.ctbu.edu.cn/'+i.get('href'))

    return jsonify({'name':mytitle})



@app.route('/showdetail/<index>')
def showDetailNews(index):
    url=newsLink[index]
    response1 = requests.get(url)
    # print(response.encoding)
    response1 = requests.get(url)
    response1.encoding = 'utf-8'
    bs1 = BeautifulSoup(response1.text, 'lxml')
    node1 = bs1.select(".article_body")
    link1 = node1[0].find_all("p")
    body_len = len(link1)
    body_text=[]
    for i in range(body_len):
        body_text.append(link1[i].text)
    return jsonify({'name':body_text})




@app.route('/json/<name>/<words>',methods=['GET'])
def hello(name,words):
    return jsonify({'name':name,'words':words})


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0')

