from PIL import Image, ImageDraw, ImageFont
import math
import textwrap


class slide_maker:
    def __init__(self):
        print("?")
        self.nom = "generator"
        self.taille_image = [1200,630]
        self.fnt = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 65)
        self.FOREGROUND = (255, 255, 255)


        #self.create_support()
        self.generate_all()
        
  
    def check_image(self,image = None):
        
        if image == None:
            image = self.create_support()
        return image
    
    def decorate (self, image = None):
        
        ##############################################
        img = Image.new('RGBA', (100, 100), (255, 0, 0, 0))

        draw = ImageDraw.Draw(img)
        draw.ellipse((25, 25, 75, 75), fill=(255, 0, 0))

        img.save('test.gif', 'GIF', transparency=0)
        #############
        image = self.check_image(image)
        
        #cadre = Image.new('RGBA', (image.size[0], image.size[1]), (255, 0, 0, 255))
        cadre = Image.new('RGBA', image.size, (255, 0, 0, 0))
        
        #draw cadre
        draw = ImageDraw.Draw(cadre)
        #draw.line([(image.size[0]/10,image.size[1]/10),(image.size[0]/10,image.size[1]-image.size[1]/10)],fill=(255,255,255,255),width=10)
        #draw.line([(image.size[0]/10,image.size[1]-image.size[1]/10),(image.size[0]-image.size[0]/10,image.size[1]-image.size[1]/10)],fill=(255,255,255,255),width=10)
        #draw.line([(image.size[0]-image.size[0]/10,image.size[1]-image.size[1]/10),(image.size[0]-image.size[0]/10,image.size[1]/10)],fill=(255,255,255,255),width=10)
        #draw.line([(image.size[0]-image.size[0]/10,image.size[1]/10),(image.size[0]/10,image.size[1]/10)],fill=(255,255,255,255),width=10)
        point1 = (image.size[0]/10,image.size[1]/10)
        point2 = (image.size[0]/10,image.size[1]-image.size[1]/10)
        point3 = (image.size[0]-image.size[0]/10,image.size[1]-image.size[1]/10)
        point4 = (image.size[0]-image.size[0]/10,image.size[1]/10)
        
        line_points = [point1,point2, point3,point4, point1,point2 ]
        
        draw.line(line_points,fill=(255,255,255,255),width=10, joint='curve')
        #
        #
        #MyDraw.line(line_points, width=40, fill=BLUE, joint='curve')
        
        #logo
        size_logo=(60,60)
        # image.size[0]/2
        # image.size[1]-image.size[1]/10
        transparent_area=( int(image.size[0]/2-size_logo[0]/2),int(image.size[1]-image.size[1]/10-size_logo[1]/2) ,int(image.size[0]/2+size_logo[0]/2) ,int(image.size[1]-image.size[1]/10+size_logo[1]/2 ))
        rect_pos=( int(image.size[0]/2-size_logo[0]/2),int(image.size[1]-image.size[1]/10-size_logo[1]/2))
        
        mask = Image.new('L', image.size, color = 255)
        
        draw2=ImageDraw.Draw(mask)
        draw2.rectangle(transparent_area, fill = 0)
        
        
        rect = Image.new("RGBA", size_logo, (255, 255, 255, 0))
        cadre.paste(rect, rect_pos)
        #cadre.putalpha(mask)
        #cadre.paste(mask, (0, 0), mask)
        #cadre.paste(cadre,box=transparent_area, cadre)
        image.paste(cadre, (0, 0), cadre)
        #image = image.paste(cadre,(image.size[0],image.size[1]))
        #
        #self.apply_filigrane(image = image)
        #image.save("masked_sample2.png")
        return image
        
    def draw_background(self, image =None,image_bg=False):
        
        #circular gradient
        innerColor = [80, 80, 255] #Color at the center
        outerColor = [0, 0, 80] #Color at the corners
        
        image = self.check_image(image)

            
        if image_bg:
            image = image.paste(image_bg,(image.size[0],image.size[1]))
            
        for y in range(image.size[1]):
            for x in range(image.size[0]):
        
                #Find the distance to the center
                distanceToCenter = math.sqrt((x - image.size[0]/2) ** 2 + (y - image.size[1]/2) ** 2)
        
                #Make it on a scale from 0 to 1
                distanceToCenter = float(distanceToCenter) / (math.sqrt(2) * image.size[0]/2)
        
                #Calculate r, g, and b values
                r = outerColor[0] * distanceToCenter + innerColor[0] * (1 - distanceToCenter)
                g = outerColor[1] * distanceToCenter + innerColor[1] * (1 - distanceToCenter)
                b = outerColor[2] * distanceToCenter + innerColor[2] * (1 - distanceToCenter)
                #Place the pixel        
                image.putpixel((x, y), (int(r), int(g), int(b)))
        #self.decorate(image)
        return image
    
    def generate_all(self):
        list = [[{"type":"facebook"},{"groupe":"www.facebook"},{"text":"siiiiinhgniiiiiice"}],[{"type":"facebook"},{"groupe":"www.facebook"},{"text":"siiiiiiiiingiice"}]]
        
        for element in list:
            #print(element)
            print(element[0])
            image = self.create_support(support = element[0]["type"])
            imagebg =self.draw_background(image = image)
            imagedeco = self.decorate(image = imagebg)
            imagefili = self.apply_filigrane(image = imagedeco)
            self.put_text(image = imagefili, text = element[2]["text"])#????????????
        print("ok ")
        pass
    
    def apply_filigrane(self, image = None):
        
        image = self.check_image(image)
        
        filigrane = Image.open("app/data/images/test_logo3.png").convert("RGBA")
        size_filigrane = (120,120)
        fil_pos=( int(image.size[0]/2-size_filigrane[0]/2),int(image.size[1]-image.size[1]/10-size_filigrane[1]/2))
        
        resized_filigrane = filigrane.resize(size_filigrane)
        
        image.alpha_composite(resized_filigrane, fil_pos)
        #image.save("masked_sample2.png")
        #self.put_text(image = image)
        return image
    
    def put_text(self,image = None,text = "pas de tehhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhx h h u  uu u uih iuh h uh ih j jk jh jh ffe  fzef efefz fez fezfeezffzefzefzefzefffezf feezefeffezefefezjhj j jh kh j hj jh  j  gh g jy g yu gyugyg yugt"):
        image = self.check_image(image)
        
        wrapper = textwrap.TextWrapper(width=50) 
         
        lines =  wrapper.wrap(text) 
        print(lines)
        
        #on decoupe notre texte en lignes selon une largeur (retrouver en variable de classe)
        w = 100
        y_text = 100
        Image_draw =ImageDraw.Draw(image)
        for line in lines:
            width, height = self.fnt.getsize(line)
            Image_draw.text(((w - width) / 2, y_text), line, font=self.fnt, fill=self.FOREGROUND)
            y_text += height
            
        image.save("masked_sample2.png")
        return image
                
    def get_informations(self,image):
        
        
        width, height = image.size
        pass
    
    def convert_to_png(self):
        #Image.open("sample1.jpg").save("sample1.png")
        pass
    
    def create_support(self, support= "facebook",**kwargs):
        #https://deux.io/tailles-images-facebook-etc/
        #mettre l option apres pour faire des banniere-profil-...
        if support =="facebook":
            taille_support=[720,720]
        elif  support =="twitter":
            taille_support=[880,440]
        elif support =="instagram":
            taille_support=[1080,1080]
        elif support =="custom":
            taille_support=[kwargs["dimension_x"],kwargs["dimension_y"]]
        else:
            taille_support=[720,720]
            # check si le support n existe pas déja 
        image_support = Image.new("RGBA",taille_support)
        
        return image_support
    
    def operations(self):
        #http://www.tangentex.com/TraitementImages.htm
        pass