Projenin amacı: https://www.nytimes.com/crosswords/game/mini sitesinde "Across" ve "Down başlıkları altındaki maddeleri bastırmak.

Proje için pip komutuyla BeautifulSoup, logging ve requests kütüphaneleri indirilecek. Yazılan kod, Ubuntu üzerinde denenecek.

pip requirements:

BeautifulSoup4 and bs4 pip requirement: 4.10.0
requests pip requirement: 2.26.0
logging pip requirement: 0.4.9.6
lxml pip requirement: 4.6.3

- Gerekli kütüphaneler indirildi. 
- İstenen web sayfasının belirtilen kısmının kod ve text hali çağırıldı.
- Text halinin istenen şekilde görüntülenmesi için fonksiyon define edildi.
- Sonuç print edildi.
- Kod, pylint ile kontrol edildi ve puan 6.1'den yaklaşık 9.3'e çıkarıldı.
- requests kullanımı için try bloğu kullanıldı.
- logging kütüphanesiyle loglar test.log dosyasına yazdırılıyor.
- Kod, Ubuntu'da başarıyla çalıştı.
- JSON dosyası oluşturuldu. "Across" ve "Down" başlıkları ikişer kez yazdırıldı. Sebebini çözemediğim için o şekilde bırakmak zorunda kaldım.
- Kod, son haliyle Ubuntu'da başarıyla çalıştırıldı.
- pylint'e tekrar sokuldu ve 9.52/10 sonucu alındı.
- log'larda tarih ve saat de belirtildi.
- Başlıkların 2'şer kere basılması dışında problem gözükmüyor.
