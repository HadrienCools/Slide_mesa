from translate import Translator


class text_manager:
    def __init__(self):
        pass
    
    def translate_statements(self,list=[]):
        props = ["dazd  dd azdd","azazdaza"]
        trad_list =[]
        translator= Translator(from_lang="fr",to_lang="en")
        for prop in props:
            translation = translator.translate(prop)
            trad_list.append(translation)   
        return trad_list        
        #print(trad_list)
        #pass
