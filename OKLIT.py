# Noktaların tanımlanması
points = [(1, 2), (4, 6), (7, 8), (2, 3)]  # İstediğiniz kadar nokta ekleyebilirsiniz

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(p1, p2):
    # Öklid mesafesi formülü
    distance = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return distance

# Mesafeleri saklayacağımız liste
distances = []

# Tüm nokta çiftleri arasındaki mesafeleri hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Her çift noktayı sadece bir kez hesaplamak için
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Mesafelerin listesini ve minimum mesafeyi yazdır
print("Tüm mesafeler:", distances)
print("Minimum mesafe:", min(distances))