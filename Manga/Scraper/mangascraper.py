import os
import bs4
import requests
from PIL import Image
import time
from PyPDF2 import PdfMerger
import shutil
 
def scraper():
    print ('Enter an URL : ')
    url = input()
    url = str(url)

    print('Enter a Filename : ')
    filename = input()
    filename = str(filename)
    
    page = 1
    os.makedirs('Manga')
    while True:
        print(f'Import Gambar Chapter {page}...')
        os.makedirs(f'Manga/{page}')
        web = requests.get(url)
        time.sleep(5)
        images = bs4.BeautifulSoup(web.content, 'lxml').find('div', attrs={'id':'chimg-auh'}).find_all('img')
        pic_num = 1 
        for image in images:
            img = image['src']
            img_data = requests.get(img).content
            with open(f'Manga/{page}/pic{pic_num}.png', 'wb') as handler:
                handler.write(img_data)
            pic_num +=1
        try :    
            url = bs4.BeautifulSoup(web.content, 'lxml').find('a', text='Chapter Selanjutnya »')['href']
            print(f'Chapter {page} Selesai')
            page+=1
        except:
            print('Scraper Selesai')
            break
    os.makedirs('Manga/PDF')
    for page in os.listdir('Manga'):
        if page != 'PDF':    
            print(f'Convert Chapter {page} Ke Dalam Bentuk PDF...')
            images = []
            im_1 = Image.open(f'Manga/{page}/pic1.png')
            
            for file in sorted([int(file.split('.')[0][3:]) for file in os.listdir(f'Manga/{page}')]):
                try:
                    path = f'Manga/{page}/pic{file}.png'
                    images.append(Image.open(path).convert('RGB'))
                except: pass
                
            im_1.save(f'Manga/PDF/{page}.pdf', save_all=True, append_images=images)
            print(f'PDF Chapter {page} Siap')
    
    print ('Menggabungkan PDF...')
    merger = PdfMerger()
    for pdf in [f'Manga/PDF/{file}' for file in os.listdir('Manga/PDF')]:
        merger.append(pdf)
    merger.write(f'{filename}.pdf')
    merger.close()
    
    shutil.rmtree('Manga')
    print ('Selesai')

if __name__ == '__main__':
    scraper()