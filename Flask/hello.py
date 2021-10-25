from flask import Flask, render_template, redirect, url_for
import datetime
import sys
if sys.version_info < (3,0):  # nghĩa là đây là cho phiên bản Python 2.x
    reload(sys)
    sys.setdefaultencoding('utf-8')

homnai = datetime.date.today()
homnay = datetime.date.today()

app = Flask(__name__,  static_folder = "D:\\Năm Cuối\\Python nâng cao\\Thực hành\\PythonNC\\bai1\\templates\\thumuchinh\\")

@app.route('/index')
@app.route('/index/<name>')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/abc')
def xuat_ra_web_mau():
    languages = [ {'STT':1, 'ten': "Python"}, {'STT':2, 'ten': "Java"} , {'STT':3, 'ten': "C++"}]
    languages.append({'STT':4, 'ten': ".NET" })
    languages.append({'STT':5, 'ten': "Matlab" })
    
    return render_template('abc.html', nnlt = languages)


@app.route("/")   # <-- khai báo trang hello  /
def hello():
    tentruong = ' Dai hoc Van Lang!'
    lienket = '<a href="https://www.vanlanguni.edu.vn">' +tentruong+' </a> <br>'
    chuoi = lienket
    import datetime
    nam = datetime.date.today().year
    chuoi = chuoi + ' <b>Xin <i>chao</i> Tan sinh vien nam ' + str(nam) + '!</b> '
    return chuoi

@app.route('/monhoc')
def learn():
 return "Day la trang mon hoc!"

@app.route('/monhoc/<tenmon>')
def subjects(tenmon):
    chuoi = "Đây là trang môn học "
    monhoc = str(tenmon).upper()
    if monhoc == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi+" "+monhoc
    return chuoi

@app.route('/sinhvien/')
def students():
    chuoi = "Đây là trang các khóa học !"
    return chuoi

@app.route('/sinhvien/<int:namhoc>')
def school_year(namhoc): 
    chuoi = "Đây là năm học "
    nam = str(namhoc).upper()
    if nam == "":
        chuoi = chuoi + "!"
    else:
        chuoi = chuoi + " " + nam
    return chuoi
# Hàm main:
if __name__ == "__main__":
    app.run(port = 5050)    # cổng mặc định là 5000
