from objectExtractionRunningTime import ObjectExtractionTimeComparison
from Tkinter import *
from tkFileDialog import asksaveasfilename
from tkMessageBox import askquestion, showinfo


class TestBenchMixin:
    def infobox(self,title,text,*args):
        return showinfo(title,text)

    def errorbox(self,text):
        return showerror('Error!',text)
    
    def questionbox(self,title,text):
        return askquestion(title,text)
    
    def selectsaveas(self,filename="",dirname="."):
        return asksaveasfilename(initialfile=filename,initialdir=dirname)
    
    def objectExtractionTimeComparison():
        TimeComparison = ObjectExtractionTimeComparison()
        TimeComparison.run()

class BenchmarkButton(Button):
    def __init__(self,parent,**config):
        Button.__init__(self,parent,config)
    
class BenchmarkLabel(Label):
    def __init__(self,parent,**config):
        Label.__init__(self,parent,config)

class BenchmarkFrame(TestBenchMixin,Frame):
  
    def __init__(self, parent=None):
        Frame.__init__(self, parent)   
        self.pack(fill=BOTH, expand=True)
         
        self.parent = parent
        self.parent.title("ilastik Benchmarking GUI")
        
        self.buttontextdict = {
            'Start' : self.objectExtractionTimeComparison,
            'Stop' : lambda: self.questionbox('Warning','Are you sure to stop ongoing tests?'),
            'Save' : self.selectsaveas
        }

        self.init_frames()
        self.add_widgets()

    def init_frames(self):
        self.buttonframe = Frame(self)
        self.testareaframe = Frame(self)
        self.canvasframe = Frame(self,height=200,relief=RAISED,borderwidth=2)
        self.statusframe=Frame(self,height=10,relief=RAISED,borderwidth=4)
        

        self.buttonframe.pack(fill=X)
        self.testareaframe.pack(fill=X)
        self.canvasframe.pack(fill=BOTH)
        self.statusframe.pack()


    def add_widgets(self):
        
        for (key,value) in self.buttontextdict.items():
            BenchmarkButton(self.buttonframe,text=key,command=value).pack(side=LEFT,expand=YES)
        

        Checkbutton(self.testareaframe,comamand=None,text="Object Extraction BM").pack(side=LEFT,expand=YES,padx=5,pady=5)
        BenchmarkLabel(self.testareaframe, text="0/5").pack(side=LEFT,expand=YES,padx=5)
        BenchmarkLabel(self.testareaframe, text="0%",width=20,relief=RAISED,borderwidth=1).pack(side=LEFT,expand=YES,padx=5)
        
        statusbox = BenchmarkLabel(self.statusframe,text="Waiting for user input").pack(side=LEFT,expand=NO,padx=5)

if __name__ == '__main__':
    root = Tk()
    #root.geometry("300x300+300+300")
    app = BenchmarkFrame(root)
    root.mainloop()


