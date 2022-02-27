import numpy as np

def jarakTitikKeGaris(p1, p2, p3): #fungsi untuk mencari panjang jarak sebuah titik ke garis
    #menerima input 3 buah titik dengan p1 dan p2 merupakan ujung-ujung garis, dan p3 adalah titik
    p1 = np.asarray(p1)
    p2 = np.asarray(p2)
    p3 = np.asarray(p3)

    jarak = np.cross(p2-p1,p3-p1)/np.linalg.norm(p2-p1)

    return jarak

def divideAndConquer(bucket, kiri, kanan, batas, ans): #fungsi menentukan titik yang akan menjadi convexhull, fungsi divideAndConquer ini berjalan secara rekursif
    dotKiri = bucket[kiri]
    dotKanan = bucket[kanan]

    mid = -1 #akan menjadi titik terjauh dari 2 garis
    jarakTerjauh = 0

    p1 = (dotKiri[0], dotKiri[1])
    p2 = (dotKanan[0], dotKanan[1])

    for i in range(len(bucket)) :
        p3 = (bucket[i][0], bucket[i][1])
        jarak = jarakTitikKeGaris(p1, p2, p3)

        if jarak * batas >= 0 and abs(jarak) > jarakTerjauh : #batas digunakan agar pencarian titik terjauh selalu mengarah "keluar" garis
            mid = i
            jarakTerjauh = abs(jarak)
    
    if mid == -1 : #apabila tidak terdapat titik lagi yang dapat dicari
        newLine = [kiri, kanan]
        if newLine not in ans :
            ans.append(newLine)
        return ans
    #rekursif menggunakan titik terjauh dari 2 garis yang kemudian memotong garis menjadi 3 titik (kiri,tengah,kanan)
    ans = divideAndConquer(bucket, kiri, mid, batas, ans)
    ans = divideAndConquer(bucket, mid, kanan, batas, ans)

    return ans

def ConvexHull(bucket) :
    idxXkiri = 0
    idxXkanan = 0
    ans = [] 
    
    for i in range(len(bucket)) : #sebagi inisiasi untuk memotong data menjadi 2 bagian dengan mecari 2 titik terjauh secara horizontal (atas dan bawah)
        if bucket[i][0] < bucket[idxXkiri][0] :
            idxXkiri = i
        if bucket[i][0] > bucket[idxXkanan][0] :
            idxXkanan = i
    
    # -1 dan 1 akan menjadi batasan pencarian agar pencarian selalu mengarah "keluar" garis
    ans = divideAndConquer(bucket, idxXkiri, idxXkanan, 1, ans) # 1 untuk mecari di bagian atas data yang sudah dibagi 2
    ans = divideAndConquer(bucket, idxXkiri, idxXkanan, -1, ans) # -1 untuk mecari di bagian bawah data yang sudah dibagi 2

    return ans