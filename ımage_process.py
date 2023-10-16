import cv2 as cv
import numpy as np

"""öncelikle resmi işlemek için çağırmamız gerek resmin bulunduğu dosya konumunu açıyoruz."""
path = "images/"

# imread
"""resmi okumak için cv.imread() fonksiyonunu kullanıyoruz. bu arkadaş resmi bir numpy
arrayine dönüştürür.
# img = cv.imread(path + "1-strawberry-png-images.png")

# namewindow
bu fonksiyon oluşmuş arrayi bir pencere formatında tutar. i̇kinci parametresi
resmi widthxheight tipini nasıl olmasını belirler
# cv.namedwindow("opencv_test", cv.window_autosize)

# imshow
bu fonksiyon numpy arraye dönüşmüş pencerede tutulan resmi ekranda göstermemizi sağlar.
# cv.imshow("opencv_test", img)
# cv.waitkey(0)
aynı zamanda cv.waitkey() isimli fonksiyon resmin ekranda delay yani beklemesini sağlar.
0 parametresi sürekli çalışmasını sağlar ve sonlandırmak için ctrl + c yapmamız yeterlidir.

# gray ımage  cvtcolor
bu fonksiyon iki parametre alır ilki numpy arrayi ikinicisi ise dönüştürülmek istenen format
burda rgb2gray ifadesi rgb den gray ımage donusumu sağlar.
# gray = cv.cvtcolor(img, cv.color_bgr2gray)

# cv.namedwindow("cv_gray", cv.window_normal)
# cv.imshow("cv_gray", gray)
# cv.waitkey(0)

# imwrite
bu fonksiyon işlem yapılmış resmi kaydetmemizi sağlar. birinci parametre kaydetme ismi ikinci
paramtre kaydedilecek resim.
# cv.imwrite(path + "gray_img.png", gray)

# gray imageleri okuma
yapmamız gerek sadece sonuna okunacak dosyasının gri olduğunu belirtmek
# img2 = cv.imread(path + "gray_img.png", cv.imread_grayscale)


# resim oluşturma
img = cv.imread(path + "opencv.jpg")
cv.namedwindow("image_create", cv.window_autosize)
cv.imshow("image_create", img)
cv.waitkey(1)

n1 = np.copy(img)
n2 = img
n2[100:200, 200:300, :] = 145
# 0-255 arası 0 a yakınlık siyahı 255 e yakınlık beyazı aradaki kalan sayılar grilik miktarını belirler
cv.imshow("iamge_create", n2)
cv.waitkey(1)

n3 = np.zeros(n2.shape, n2.dtype)
cv.imshow("n3", n3)
cv.waitkey(1)

n4 = np.zeros([150, 260])
cv.imshow("n4", n4)
cv.waitkey(1)

rect = np.ones((550, 778, 3))
black = (0, 0, 0)
red = (0, 0, 255)
green = (0, 255, 0)

cv.rectangle(rect, (480, 250), (100, 450), black, 8)
cv.rectangle(rect, (580, 150), (200, 350), black, 8)
cv.line(img, (100, 450), (200, 350), black, 8)
cv.line(img, (480, 250), (500, 150), black, 8)
cv.line(img, (100, 250), (200, 150), black, 8)
cv.line(img, (480, 450), (580, 350), black, 8)

start_point = (150, 100)
font_thickness = 2
font_size = 1
font = cv.font_hershey_duplex

cv.puttext(rect, "cici bebe biskuvileri", start_point, font, font_size, black, font_thickness)
cv.imshow('dikdortgen', rect)
cv.waitkey(0)"""
