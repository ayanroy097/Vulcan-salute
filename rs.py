import tkinter as tk
from tkinter import ttk,messagebox
import json
from urllib.request import urlopen 


main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('I am your Father Luke')
##Get the api bytecode and parse into json
with urlopen("http://stapi.co/api/v1/rest/location/search") as re:
    source = re.read()
data = json.loads(source)

scrollbar = ttk.Scrollbar(main_application)
scrollbar.pack( side = tk.RIGHT, fill= tk.Y )

c = 0
##Creates a label for every location name returned by the api
mylist = tk.Listbox(main_application, yscrollcommand = scrollbar.set )
for i in data['locations']:
    cur_label = 'label' + str(i['name'])
    cur_label = ttk.Label(main_application, text = i['name'])
    # cur_label.grid(row= c, column = 0, sticky = tk.W, padx = 2 , pady = 2) 
    mylist.insert(tk.END, str(c+1) + ". " + cur_label.cget("text") )
    c = c+1


##Adds the scrollbar
mylist.pack( side = tk.LEFT, fill = tk.BOTH, expand = True )
scrollbar.config( command = mylist.yview )



# lchoice = tk.StringVar()
# txt = ttk.Entry(main_application,width=10, textvariable = lchoice)
# txt.pack(side = tk.RIGHT, expand =False)
# txt.grid(column=1, row=0)

# def clicked():

#     key = lchoice.get()
#     print(key)
#     cur_label.configure(text=' was asked for')

# btn = ttk.Button(main_application, text="Submit a name to know more about", command=clicked)

btn = ttk.Button(main_application, text = "Delete a location", command = lambda listbox=mylist: mylist.delete(tk.ANCHOR))  
# btn.grid(column=2, row=0)
btn.pack()

main_application.mainloop()