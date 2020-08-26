from bs4 import BeautifulSoup
import urllib.request
import mysql.connector

dominio = ['random_url/','random_url_two','random_url_three']
dominio2 = ['random_url/','random_url_two','random_url_three']


mydb= mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="news_python"
	)

videos_=0
id_=86
conta=187
text = 91
print(conta)
for x in dominio:
	id_=id_+1
	text = text+1
	print(x)
	friendly_url = x

	req = urllib.request.Request("https://randomdomain.com" + x, headers={"User-Agent": "Chrome"})
	res = urllib.request.urlopen(req)


	html = BeautifulSoup(res.read(),"html5lib")


	# METADATA
	descripcionMetadata= html.find("meta", {"name": "description"})
	canonicalMetadata= html.find("link", {"rel": "canonical"})


	# CONTENIDO
	contenido= html.find_all("div", {"class": "panel-body"})
	content = ' <br>'.join(str(ii) for ii in contenido)

	# H1
	h = html.h1
	if not h:
		h = html.h3
		h1 = h.text
	else: 
		h1 = h.text

	# TITLE
	titulo = html.title
	title = titulo.text

	# cursor1 = mydb.cursor()
	# sql="INSERT INTO news (id,title, canonical, description, friendly_url, metatitle, origen) VALUES (%s,%s,%s,%s,%s,%s,%s)"
	# val = (id_, str(title),str(canonicalMetadata), str(descripcionMetadata),  str(friendly_url), str(h1), "randomdomain.com")
	# cursor1.execute(sql,  val)
	# mydb.commit()

	#VIDEO
	video= html.find_all("iframe")
	_videos_src=[]

	for videos in video:
		src_video = videos.get('src')
		_videos_src.append(src_video)

	# IMAGENES
	imagenes= html('img')

	_imagenes_alt=[]
	_imagenes_src=[]

	for imagen in imagenes:
		src_img = imagen.get('src')
		_imagenes_src.append(src_img)
		alt_img = imagen.get('alt')
		_imagenes_alt.append(alt_img)

	
	if "WordPress" in _imagenes_alt:
		_imagenes_alt.remove("WordPress")
	if "https://randomdomain.com/wp-content/uploads//2020/04/logo-eye-peq-e1586463775577.png" in _imagenes_src:
		_imagenes_src.remove("https://randomdomain.com/wp-content/uploads//2020/04/logo-eye-peq-e1586463775577.png")
	if "https://secure.gravatar.com/avatar/85ce68a32b33a5442281f2408abcb1d6?s=96&d=mm&r=g" in _imagenes_src:
		_imagenes_src.remove("https://secure.gravatar.com/avatar/85ce68a32b33a5442281f2408abcb1d6?s=96&d=mm&r=g")
		



	_imagen = [_imagenes_src,_imagenes_alt]
	

	cursor3 = mydb.cursor()
	sql3="INSERT INTO news_text (id,news_id , text) VALUES (%s,%s,%s)"
	val3 = (text,id_, str(content))
	cursor3.execute(sql3, val3)
	mydb.commit()

for x in dominio2:
	id_=id_+1
	text=text+1
	print(x)
	friendly_url = x

	req = urllib.request.Request("https://randomdomain.com" + x, headers={"User-Agent": "Chrome"})
	res = urllib.request.urlopen(req)


	html = BeautifulSoup(res.read(),"html5lib")


	# METADATA
	descripcionMetadata= html.find("meta", {"name": "description"})
	canonicalMetadata= html.find("link", {"rel": "canonical"})


	# CONTENIDO
	contenido= html.find_all("div", {"class": "panel-body"})
	content = ' <br>'.join(str(ii) for ii in contenido)

	# H1
	h = html.h1
	if not h:
		h = html.h3
		h1 = h.text
	else: 
		h1 = h.text

	# TITLE
	titulo = html.title
	title = titulo.text


	#VIDEO
	video= html.find_all("iframe")
	_videos_src=[]

	for videos in video:
		src_video = videos.get('src')
		_videos_src.append(src_video)

	# IMAGENES
	imagenes= html('img')

	_imagenes_alt=[]
	_imagenes_src=[]

	for imagen in imagenes:
		src_img = imagen.get('src')
		_imagenes_src.append(src_img)
		alt_img = imagen.get('alt')
		_imagenes_alt.append(alt_img)

	
	if "WordPress" in _imagenes_alt:
		_imagenes_alt.remove("WordPress")
	if "https://randomdomain.com/wp-content/uploads//2020/04/logo-eye-peq-e1586463775577.png" in _imagenes_src:
		_imagenes_src.remove("https://randomdomain.com/wp-content/uploads//2020/04/logo-eye-peq-e1586463775577.png")
	if "https://secure.gravatar.com/avatar/85ce68a32b33a5442281f2408abcb1d6?s=96&d=mm&r=g" in _imagenes_src:
		_imagenes_src.remove("https://secure.gravatar.com/avatar/85ce68a32b33a5442281f2408abcb1d6?s=96&d=mm&r=g")



	_imagen = [_imagenes_src,_imagenes_alt]
	

	cursor3 = mydb.cursor()
	sql3="INSERT INTO news_text (id,news_id , text) VALUES (%s,%s,%s)"
	val3 = (text,id_, str(content))
	cursor3.execute(sql3, val3)
	mydb.commit()	