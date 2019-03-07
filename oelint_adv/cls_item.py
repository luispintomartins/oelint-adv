class Item():
    ATTR_LINE = "Line"
    ATTR_RAW = "Raw"
    ATTR_ORIGIN = "Origin"
    CLASSIFIER = "Item"

    def __init__(self, origin, line, infileline, rawtext):
        self.Line = line
        self.Raw = rawtext
        self.Links = []
        self.Origin = origin
        self.InFileLine = infileline
    
    def AddLink(self, _file):
        self.Links.append(_file)

    def GetAttributes(self):
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}

    def GetRawCleaned(self):
        res = self.Raw
        chars = "\t\n\r"
        for c in chars:
            res = res.replace(c, " ")
        return res

    def __repr__(self):
        return "{} -- {}\n".format(self.__class__.__name__, self.GetAttributes())


class Variable(Item):
    ATTR_VAR = "VarName"
    ATTR_VARVAL = "VarValue"
    CLASSIFIER = "Variable"

    def __init__(self, origin, line, infileline, rawtext, name, value):
        super().__init__(origin, line, infileline, rawtext)
        self.VarName = name
        self.VarValue = value
    
    def IsAppend(self):
        return self.Raw.find("+=") != -1


class Comment(Item):
    CLASSIFIER = "Comment"
    def __init__(self, origin, line, infileline, rawtext):
        super().__init__(origin, line, infileline, rawtext)

class Include(Item):
    CLASSIFIER = "Include"
    ATTR_INCNAME = "IncName"
    def __init__(self, origin, line, infileline, rawtext, incname):
        super().__init__(origin, line, infileline, rawtext)
        self.IncName = incname

class Function(Item):
    ATTR_FUNCNAME = "FuncName"
    ATTR_FUNCBODY = "FuncBody"
    CLASSIFIER = "Function"

    def __init__(self, origin, line, infileline, rawtext, name, body):
        super().__init__(origin, line, infileline, rawtext)
        self.FuncName = name[:name.find("{")].replace("(", "").replace(")", "").strip()
        self.FuncBody = body


class PythonBlock(Item):
    ATTR_FUNCNAME = "FuncName"
    CLASSIFIER = "PythonBlock"
    def __init__(self, origin, line, infileline, rawtext, name):
        super().__init__(origin, line, infileline, rawtext)
        self.FuncName = name