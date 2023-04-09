html_document = """

<!DOCTYPE html>                
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1 id="header">

        Python kursu(Yusuf Ozen)

        </h1>

    <div class="grup 1">

    

        <h2>

            programlama
        </h2>

        <ul>

            <li> menu 1 </li>
            <li> menu 2 </li>
            <li> menu 3 </li>

        </ul>

    </div>


    <div class="grup 2">

    

        <h2>

            moduller
        </h2>

        <ul>

            <li> menu 1 </li>
            <li> menu 2 </li>
            <li> menu 3 </li>

        </ul>

    </div>


    <img src="" alt="">
</body>
</html>


"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(html_document, 'html.parser')       # hangi parseri kullanacagini soyledik.


result = soup.prettify()        # html dokumanini duzenleme islemi yapar prettify.
result = soup.title               # html  sayfasındaki title i alır.
result = soup.head                # html  sayfasındaki head kısmını  alır.
result = soup.body                # html  sayfasındaki body kısmını  alır.
result = soup.title.name          # sadece ismi alır.
result = soup.title.string        # sadece web sayfasının ismini yazdırır.
result = soup.h1                  # sadece h1 etiketini yazdırır.
result = soup.h2.name
result = soup.h2.string
result = soup.h1.string
result = soup.find_all('h2')      # sayfadaki  butun h2 etiketlerini getirir.
result = soup.find_all('h2')[0]   # h2 deki 0.elemanı alır.
result = soup.div                 # sayfadaki div leri yazdırır.
result = soup.find_all('div')
result = soup.find_all('div')[1].ul.find_all('li')       # div in 1 elemanının ul sinin li lerini bulur.

result = soup.div.findChildren()





print(result)
