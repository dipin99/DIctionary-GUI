import tkinter as tk
import requests
import json


root= tk.Tk()
root.title("DICTIONARY")
root.iconbitmap(r'dict.ico')
canvas= tk.Canvas(root,height=400,width=300)
canvas.pack()


def getMeaning():
    x= entry.get()
    print(x)
    app_id  = "Your API Key"
    app_key  = "Your API ID"
    language = "en-gb"
    word_id = x
    strictMatch = 'false'
    fields="definitions"
    url = 'https://od-api.oxforddictionaries.com/api/v2' + language + '/' + word_id.lower() + '?fields=' + fields + '&strictMatch=' + strictMatch;

    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    dicti=r.json()
    #print(json.dumps(r.json(),indent=4))
    if(x=="Enter a word"):
        label['text']="Please enter a word"
    else:
        label['text']= format_response(dicti)
    

def format_response(dicti):
    try:
        name=dicti['results']
        p=name[0]
        x=p['id']
        a=p["lexicalEntries"]
        e=a[0]
        b=e["entries"]
        f=b[0]
        c=f["senses"]
        g=c[0]
        d=g["definitions"]
        h=d[0]
    #i=g["subsenses"]
   # j=i[0]
   # k=j["definitions"]
   # l=k[0]
        finalstr= 'Word: %s\n\nDefinition: %s\n'%(x,h)
    except: finalstr="The definition could not be retrieved"
   # print(finalstr)
    return finalstr

frame1= tk.Frame(root,bg='#80c1ff')
frame1.place(relx=0.05,rely=0.05,relheight=0.15,relwidth=0.9)

entry=tk.Entry(frame1,bg="white",font=('Courier',15))
entry.place(relx=0.025,rely=0.15,relheight=0.7,relwidth=0.6)
entry.insert(0,"Enter a word")
def some_callback(event): # note that you must include the event as an arg, even if you don't use it.
    entry.delete(0, "end")
    return None
entry.bind("<Button-1>", some_callback)

dict_button= tk.Button(frame1,text="Search",font=('Courier',15),command=lambda:getMeaning())
dict_button.place(relx=0.65,rely=0.15,relheight=0.7,relwidth=0.325)



frame2= tk.Frame(root,bg='#80c1ff')
frame2.place(relx=0.05,rely=0.25,relheight=0.7,relwidth=0.9)

label= tk.Label(frame2,bg='white',wraplength=250,justify='center',pady=50)
label.place(relheight=0.7,relwidth=1)

root.mainloop()

