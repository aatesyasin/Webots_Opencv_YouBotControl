## Webots_Opencv_YouBotControl
# Webots Ortamında El ile Robot Kontolü 
Projede, opencv temelli mediapipe modülü ile algılanan parmakların algoritmik sıralanmasıyla Kuka youBot adlı robotun Webots ortamında kontolü yapılmakdatır.

## Hangi Parmak Kombinasyonu Hangi Hareket.
1. Serçe Parmak ve Baş Parmak; robotun ileri hareketi.
2. Sadece Serçe Parmak; robotun geri hareketi.
3. Serçe Parmak,Yüzük Parmak ve Baş Parmak; robotun Sola hareketi.
4. Serçe Parmak ve Yüzük Parmak; robotun Sağa hareketi.
5. Baş Parmak hariç diğer dört parmak; robotun Sağa dönüş hareketi.
6. Bütün Parmaklar; robotun Sola dönüş hareketi.


## Hareketler
#### İleri Ve Geri Hareketi
![alt text](https://github.com/aatesyasin/Webots_Opencv_YouBotControl/blob/main/VideoPar%C3%A7ac%C4%B1klar%C4%B1/gitHub_%C4%B0leriGeri.gif)
#### Sola Ve Sağa Hareketi
![alt text](https://github.com/aatesyasin/Webots_Opencv_YouBotControl/blob/main/VideoPar%C3%A7ac%C4%B1klar%C4%B1/gitHub_SolSag.gif)
#### Sola ve Sağa Dönüş Hareketi
![alt text](https://github.com/aatesyasin/Webots_Opencv_YouBotControl/blob/main/VideoPar%C3%A7ac%C4%B1klar%C4%B1/gitHub_Donusler.gif)


## Kullanılan Python Sürüm Ve Modülleri
### WindowsContrellerUDP.py
1. Python 3.6
2. opencv
3. mediapipe
4. numpy
5. time
6. Webots> controller/robot
 
