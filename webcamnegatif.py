import numpy as np
import cv2

cap = cv2.VideoCapture(0) #inisialisasi gambar menggunakan kamera bawaan dari PC

while(True): #untuk looping imshow sehingga akan memunculkan gambar/video
    
    ret, frame = cap.read() #menampilkan gambar berwarna

    Abu_abu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #mengubah gambar sebelum warna menjadi gambar negatif

    cv2.imshow('frame',Abu_abu) #mengubah gamar menjadi sekala negarif
    if cv2.waitKey(1) & 0xFF == ord('c'): #perintah untuk keluar dari program dengan menekan huruf "c"
    
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()