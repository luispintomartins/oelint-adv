try:
    from .cls_rule import Rule
    from .cls_item import *
except (SystemError, ImportError):
    from cls_rule import Rule
    from cls_item import *

class VarNativeFilename(Rule):
    def __init__(self):
        super().__init__(id = "oelint.var.nativefilename", 
                         severity="warning",
                         message="native-recipe-files should include '-native' in file name")

    def check(self, _file, stash):
        res = []
        items = [x for x in \
                stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER, attribute=Variable.ATTR_VAR, attributeValue="inherit") \
                if x.VarValue.find("native") != -1]
        if not any(items):
            if _file.find("-native") == -1:
                res += self.finding(_file, 0)
        return res