class Codec:
    def __init__(self): 
        self.d = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        short_url="http://tinyurl.com/"+str(len(self.d))
        self.d[short_url]=longUrl
        return short_url
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.d[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))