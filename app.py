from urllib.request import Request, urlopen
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello():
   s=''
   if request.method == 'POST':
      f = request.form['site']
      file = open('reg.txt', 'r')
      s = file.readlines()
      if f not in s:
         file.close()
         file = open('reg.txt', 'a')
         file.writelines(str(f)+'\n')
         file.close()
      s = open('reg.txt', 'r').readlines()
      return render_template('hello.html', site=s)
   else:
      file = open('reg.txt', 'r')
      s = file.readlines()
      return render_template('hello.html', site=s)



if __name__ == '__main__':
    app.run()