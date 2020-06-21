from tkinter import *

class ValidatedEntry(Entry):
    def __init__(self,master = None, validation = lambda x: True, **kw):
        super().__init__(master=master, **kw)
        self.validation = validation

    def validate(self, mode = None):
        return self.validation(self.get(), mode)

class ValidatedStringVar(StringVar):
    def __init__(self, master=None, value=None, name=None, validation = lambda x: True):
        super().__init__(master=master, value=value, name=name)
        self.validation = validation
        
    def validate(self, mode = None):
        return self.validation(self.get(), mode)
    
class ValidatedListBox(Listbox):
    def __init__(self, master=None, cnf={}, validation = lambda x: True, **kw):
        super().__init__(master = master)
        self.validation = validation
    
    def validate(self, mode = None):
        if self.curselection():
            selection = self.get(self.curselection())
        else:
            selection = None
        return self.validation(selection, mode)
        
    