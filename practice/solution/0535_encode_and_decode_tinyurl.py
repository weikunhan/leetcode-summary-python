import random

class Codec:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """    
        
        self.encoder_value_dict = {}
        self.decoder_value_dict = {}
        self.code_value = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        
        if not longUrl in self.encoder_value_dict:
            encoder_value = ''
            
            for _ in range(6):
                encoder_value += random.choice(self.code_value)
                
            self.encoder_value_dict[longUrl] = encoder_value
            self.decoder_value_dict[encoder_value] = longUrl
            
        temp_value = 'http://tinyurl.com/' + self.encoder_value_dict[longUrl]
        
        return temp_value

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        
        temp_value = self.decoder_value_dict[shortUrl.split('/')[-1]]
        
        return temp_value
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))