**Projenin amacı: https://www.nytimes.com/crosswords/game/mini sitesinde "Across" ve "Down başlıkları altındaki maddeleri bastırmak.**

Proje için pip komutuyla BeautifulSoup, logging ve requests kütüphaneleri indirilecek. Yazılan kod, Ubuntu üzerinde denenecek.

**pip requirements:**

* BeautifulSoup4 and bs4 pip requirement: 4.10.0 
* requests pip requirement: 2.26.0 
* logging pip requirement: 0.4.9.6 
* lxml pip requirement: 4.6.3

**Sırasıyla projenin gelişim aşamaları:**

1. Gerekli kütüphaneler indirildi. 
1. İstenen web sayfasının belirtilen kısmının kod ve text hali çağırıldı.
    1. Text halinin istenen şekilde görüntülenmesi için fonksiyon define edildi.
1. Sonuç print edildi.
1. Kod, pylint ile kontrol edildi ve puan 6.1'den yaklaşık 9.3'e çıkarıldı.
1. requests kullanımı için try bloğu kullanıldı.
1. logging kütüphanesiyle loglar test.log dosyasına yazdırılıyor.
1. Kod, Ubuntu'da başarıyla çalıştı.

**Daha sonraki aşamalar:**

1. pylint'e tekrar sokuldu ve 9.52/10 sonucu alındı.
1. log'larda tarih ve saat de belirtildi.
1. Başlıkların 2'şer kere basılması dışında problem gözükmüyor.
1. JSON dosyası oluşturuldu. "Across" ve "Down" başlıkları ikişer kez yazdırıldı. Sebebini çözemediğim için o şekilde bırakmak zorunda kaldım.
1. Kod, son haliyle Ubuntu'da başarıyla çalıştırıldı.
1. Başlıkların 2'şer kere basılması dışında problem gözükmüyor.
