class CaseInsensitiveDict(dict):
    """A dictionary where the key is not case sensitive
    
    Example
    -------
    cid = CaseInsensitiveDict()
    cid["Hello"] = 1234
    print(cid["Hello"]) # 1234
    print(cid["HELLO"]) # 1234
    print(cid["hello"]) # 1234
    """
    def __init__(self, d = dict()):
        self._s = dict((k.lower(), k) for k in d)
        newd = {k.lower() : v for k, v in d.items()}
        super().__init__(newd)
        
    def __setitem__(self, key, value):
        self._s[key.lower()] = key
        super(CaseInsensitiveDict, self).__setitem__(key.lower(), value)

    def __getitem__(self, key):
        return super(CaseInsensitiveDict, self).__getitem__(key.lower())
    
    def __contains__(self, key):
        return dict.__contains__(self, key.lower())
    
    def keys(self):
        return self._s.values()