#urllib.error的容错
import urllib.error                                                           
import urllib.request                                                         
import ssl                                                                    
context = ssl._create_unverified_context()                                    
                                                                              
                                                                              
#构造一个请求对象                                                                     
req = urllib.request.Request('https://www.wahaha.com/fdfds')                  
#URLError是HTTPError的父类                                                        
try:                                                                          
    req1 = urllib.request.urlopen(req,context=context,timeout=0.1)            
    print('成功')                                                               
except urllib.error.HTTPError as err:                                         
    print(err.code)                                                           
    print(err.reason)                                                         
except urllib.error.URLError as err:                                          
    print(err.reason)                                                         
