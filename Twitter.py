#coding: utf-8
import tweepy #tweepy k�t�phanesini kullanacagimiz i�in k�t�phaneyi import ediyoruz
import os #Led yakmak ve mp3 �aldirdigimiz dosyalari �alistirmak i�in kullanacagiz
import time #tweet apinin veri �ekme asimina d�smemek i�in 2 sn de bir tweetleri �ekmek i�in kullanacagiz
import threading
consumer_key="3Ucmmo6X01pNGjCiGsiHu89Db" #Twitter apinizin consumer keyiniz
consumer_secret="onI2Y971461ADTqAi3I68eiGNOkfQrIlGWNKActyUqhs1WAWHh" #Twitter apinizin consumer_secret keyiniz
access_token="198904370-hTkTGd8qY0XJEnaiCJBHvzaKJp6g1lK8HPeXpI1Z"#Apinizin tokeni
access_token_secret="jsmRWHcBLeSJ1RRQYf1Y4x9zXp23obS88GjponidSK6t6"#Apinin token secreti

giris = tweepy.OAuthHandler(consumer_key, consumer_secret)
giris.set_access_token(access_token, access_token_secret)

api = tweepy.API(giris)

def isikyakRed():
	os.system('python Red.py')
def isikyakGreen():
	os.system('python Green.py')
def isikyakYellow():
	os.system('python Yellow.py')
def isikyakBlue():
	os.system('python Blue.py')

def kopmalikmusic():
	os.system('python kopmalik.py')

def romantikmusic():
	os.system('python romantik.py')

def rapmusic():
	os.system('python rap.py')

def thrashmetalmusic():
	os.system('python thrashmetal.py')
sayac=1

while sayac==1: #Saya� 1 oldugu s�recek bu islemi yap diyoruz ve asagidaki kodlara ge�iyor
    
	#try:
		twitler = api.home_timeline()   #Her seferinde tweete bakarken zaman t�nelinizdeki g�ncel tweeti �ekiyor
    		twit=twitler[0].text #Zaman t�nelinizdeki son tweeti twit adindaki degiskene atiyor
    		print("tweet cekiliyor",twit)   #Bunu kontrol i�in kullandim g�ncel tweeti g�rebiliyor mu diye
   		time.sleep(2)                   #Bu islemleri yaptiktan sonra 2 sn boyunca bekliyor
   		if twit.find("#romantik") != -1:                #Bu kisimda eger son atilan tweet Calistir ise asagidaki islemleri yapmaya basla
       			 t = threading.Thread(name = 'isikyakRed', target=isikyakRed)
			 w = threading.Thread(name = 'romantikmusic', target=romantikmusic)
			 t.start()
			 w.start()
			 break
		if twit.find("#rap") != -1:#Bu kisimda eger son atilan tweet Calistir ise asagidaki islemleri yapmaya basla
       			 t = threading.Thread(name = 'isikyakGreen', target=isikyakGreen)
			 w = threading.Thread(name = 'rapmusic', target=rapmusic)
			 t.start()
			 w.start()
			 break
		if twit.find("#kopmalik") != -1:#Bu kisimda eger son atilan tweet Calistir ise asagidaki islemleri yapmaya basla
       			 t = threading.Thread(name = 'isikyakYellow', target=isikyakYellow)
			 w = threading.Thread(name = 'kopmalikmusic', target=kopmalikmusic)
			 t.start()
			 w.start()
			 break
		if twit.find("#thrashmetal") != -1:#Bu kisimda eger son atilan tweet Calistir ise asagidaki islemleri yapmaya basla
       			 t = threading.Thread(name = 'isikyakBlue', target=isikyakBlue)
			 w = threading.Thread(name = 'thrashmetalmusic', target=thrashmetalmusic)
			 t.start()
			 w.start()
			 break
        #except tweepy.TweepError :
	#	print("hgfie")
	#	time.sleep(60 * 15)
	#	print("busraa")
		#continue
	#except StopIteration:
	#	break

