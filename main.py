from flask import Flask, redirect, render_template, request
from threading import Thread
from flask_assets import Environment, Bundle
from flask_mobility import Mobility
app = Flask(__name__)
Mobility(app)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)
from constants import Links, BOTH
links = Links()
mkstr = lambda itrbl : ', '.join([str(each) for each in itrbl])


@app.route('/')
def home():
    print(f"Request from {mkstr(request.access_route)} on {request.user_agent.browser}")
    return render_template("index.html")

@app.route('/tectonix', methods=BOTH, strict_slashes=False)
def home2():
    print(f"Request from {request.user_agent.browser}")
    return render_template("index.html")

@app.route('/realm/' , methods=BOTH, strict_slashes=False)
def realm():
    redirect(links.windows_store)
    return redirect(links.windows_store)

@app.route('/join', methods=BOTH, strict_slashes=False)
def join(): return redirect(links.official)

@app.route('/mc/', methods=BOTH, strict_slashes=False)
def getMC():
    if request.user_agent.browser == "safari":
      return redirect(links.ios)
    elif request.MOBILE:
      return redirect(links.android)
    else:
      return redirect(links.win_store)

@app.route('/ioscraft', methods=BOTH, strict_slashes=False)
def getioslink(): return redirect(links.ios)

@app.route('/ios', methods=BOTH, strict_slashes=False)
def ios_url(): return redirect(links.ios)

@app.route('/discord', methods=BOTH, strict_slashes=False)
def get_discord():
    return redirect(links.discord)

def run():
  app.run(host='0.0.0.0')

if __name__ == '__main__':
    run()

def keep_alive():
    t = Thread(target=run)
    t.start()