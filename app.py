from flask import Flask, render_template, request
from flask import send_file
from werkzeug.utils import secure_filename
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from io import BytesIO
app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('index.html')
@app.route('/get_image',methods = ['GET', 'POST'])
def get_image():
    if request.method == 'POST':
        f = request.files['file']  
        f.save(secure_filename(f.filename))
    file1 = open(f.filename,"r") 
    allWords=file1.read()
    STOP_LIST = ['न', 'तरी', 'तो', 'हें', 'तें', 'कां', 'आणि', 'जें', 'जे', 'मग', 'ते', 'मी', 
             'जो', 'परी', 'गा', 'हे', 'ऐसें', 'आतां', 'तैसें', 'परि', 'नाहीं', 'तेथ', 'हा', 
             'तया', 'असे', 'म्हणे', 'काय', 'म्हणौनि', 'कीं', 'जैसें', 'तंव', 'तूं', 'होय', 
             'जैसा', 'आहे', 'पैं', 'तैसा,जरी', 'म्हणोनि,एक', 'ऐसा', 'जी', 'ना', 'मज', 
             'एथ', 'या', 'जेथ', 'जया', 'तुज', 'तेणें', 'तैं', 'पां', 'असो', 'करी', 'ऐसी', 
             'येणें', 'जाहला,तेंचि', 'आघवें', 'होती', 'जैंकांहीं', 'होऊनि', 'एकें', 'मातें', 'ठायीं',
             'ये', 'अर्जुना', 'सकळ', 'केलें', 'जेणें', 'जाण', 'जैसी', 'होये', 'जेवीं', 'एऱ्हवीं', 
             'मीचि', 'किरीटी', 'दिसे', 'देवा', 'हो', 'तरि', 'कीजे', 'तैसे', 'आपण', 'तिये', 
             'कर्म', 'नोहे', 'इये', 'पडे', 'पार्था', 'माझें', 'तैसी', 'लागे', 'नाना', 'जंव', 'कीर',
             'आह','आज', 'असं', 'बरं', 'बर', 'कर', 'आपलं', 'आपल','तर','आण','viewpoint',
             'delhi','watch','today','will','now','फक','वर','coronaviru','going','something','want',
            'hai','know']
    # path = '/home/pooja/arvind/MyWork/SocialMediaSentimentAnalysis/SourceCode/lohit-devanagari/Lohit-Devanagari.ttf'
    stopwords = set(STOPWORDS)
    stopwords=list(stopwords)
    stopwords=set(stopwords+STOP_LIST)
    wordCloud = WordCloud(background_color="white",stopwords = stopwords).generate(allWords)
    plt.figure(figsize=(10,6))

    plt.imshow(wordCloud,interpolation = "bilinear")
    plt.axis("off")
    #plt.savefig("DocBhooshan4"+".png")
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

    # plt.show()
    # return send_file(filename, mimetype='image/gif')

if __name__ == '__main__':
    app.run(debug = True)
