import numpy as np
import cv2

cap = cv2.VideoCapture(0) #inisialisasi gambar menggunakan kamera bawaan dari PC

while(True): #untuk looping imshow, sehingga camera akan menangkap objek video secara realtime.
    ret, frame = cap.read() #untuk menangkap gambar dengan format berwarna /BGR
    bright = cv2.addWeighted(frame,2.0, np.zeros(frame.shape, frame.dtype), 1, 25) #mengubah kecerahan gambar menjadi gambar bright
    cv2.imshow('webcam',bright) #untuk menampilkan gambar yang tellah diubah tingkat kecerahannya.
    if cv2.waitKey(1) & 0xFF == ord('c'): #perintah untuk keluar dari program dengan menekan huruf "c"
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()