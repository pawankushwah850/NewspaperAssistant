class newspaperAssistant:

    def __init__(self):
        try:
            """ pip install pyttsx3, import computer voice  as your os default"""
            import pyttsx3 as ptx 
            self.voice=ptx.init()

            """ voice set peoperty , control voice fulency 0-200 """
            self.voice.setProperty('voice',80) 
        except:
            print("pyttsx3 module not to be imported, or not found.. check installation or path")
            exit('Finshed...')
        try:
            """Installation
                url=https://newsapi.org/docs/client-libraries/python


                $ pip install newsapi-python
                Usage
                from newsapi import NewsApiClient

                # Init
                newsapi = NewsApiClient(api_key='f52131563404483193a31f7f3622f203')"""

            from newsapi import NewsApiClient
            self.api = NewsApiClient(api_key='f52131563404483193a31f7f3622f203') #here your api key, you get after login in https://newsapi.org/docs/client-libraries/python
        except:
            print('News API module not imported , or not found.. check installation or path')
            exit('Finshed..')
        try :
            import datetime
        except:
            print('datetime module not imported , or not found.. check installation or path')
            exit('Finshed...')
            
        self.time=datetime.datetime.now()
        
        """ accoring to time she wish you"""

        if 12> int(self.time.strftime("%H")): 

            """ say is function in pyttsx3 , who convert text to speech"""
            self.voice.say('Good morning sir , my self pikachu , i am your newspaper assistance.')

            """ after running take thus function to compelte perfectly"""
            self.voice.runAndWait()
        else:
            self.voice.say('Good Afternoon sir , my self pikachu , i am your newspaper assistance.')
            self.voice.runAndWait()

    def searchNews(self):
        try:
            import json 
        except:
            print("json module not to be imported, or not found.. check installation or path")
            exit('Finshed...')
        try:
            import time
        except:
            print("time module not to be imported, or not found.. check installation or path")
            exit('Finshed...')

        try:
            self.headline=self.api.get_top_headlines(q=None, qintitle=None, sources=None, language='en', country="in", category='general', page_size=None, page=None)
            
            """{
                "status": "error", or ok
                "code": "apiKeyMissing",
                "message": "Your API key is missing. Append this to the URL with the apiKey param, or use the x-api-key HTTP header."
                }"""


            if self.headline['status']=="ok":

                data=self.headline['articles']

                total_result=int(self.headline['totalResults'])

                self.voice.say(f"{total_result} News, Listen carefully ....")
                time.sleep(2)

                counter=1
                for i in  data:
                    self.voice.say(f"News number {counter}")
                    time.sleep(2)
                    self.voice.say(f"According to {i['author']}")
                    self.voice.say(f"Title is {i['title']}")
                    self.voice.say(f"Description is {i['description']}")
                    self.voice.runAndWait()
                    counter+=1
            else:
                print("something went wrong")
        except ValueError :
            print(self.headline['message'])
            exit()
        
        self.voice.say('thanking you to listing news')

if __name__=="__main__":
    """calling class"""
    pikachu=newspaperAssistant()
    pikachu.searchNews()