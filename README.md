# Fruits Classification CNN [Open Apps](https://fruits-classification073-cnn.herokuapp.com/)

### Deskripsi
Pada proyek ini akan mengklasifikasikan buah dengan menggunakan data citra buah yang diambil dari platform Kaggle ([_Dataset_](https://www.kaggle.com/chrisfilo/fruit-recognition/)). Proyek ini menggunakan model Convolutional Neural Network (CNN) dengan optimizer adam untuk mencari nilai akurasi pada setiap buah serta secara kesuluruhan buah yang ada.
Jenis-jenis buah yang disediakan pada dataset sebagai berikut:
- Apple
- Banana
- Carambola
- Guava
- Kiwi
- Mango
- Orange
- Peach
- Pear
- Persimmon
- Pitaya
- Plum
- Pomegranate
- Tomatoes
- Muskmelon

### Batasan 
Pada proyek ini hanya berfokus pada buah Apple, Carambola, Plum, dan Tomatoes yang nantinya akan dibangun sebuah model dengan jumlah data 11573.

## Dataset yang digunakan
Data Fruits Classification CNN diambil dari dataset Kaggle yang berisi data citra sebanyak 44406. Namun pada proyek ini hanya menggunakan 11573 data citra saja.
Jumlah data citra pada tiap jenis buah yang digunakan:

| Fruit     | Jumlah |
| --------- | ------ |
| Apple     | 5024   |
| Carambola | 2080   |
| Plum      | 2298   |
| Tomatoes  | 2171   |

### Preprocessing
1. Resize gambar menjadi  150x150 Pixel
2. Normalisasi Gambar
3. Splitting data
   - Data training (80%): 9257
   - Data testing (10%): 1156
   - Data validation (10%): 1160
4. Data Augmentation
   - rescale = 1./255,
   - shear_range = 0.2
   - zoom_range = 0.2

### Arsitektur Model
1. Menggunakan 3 Feature Extraction Layer 
   - Convolution
   - Pooling
2. Flattening
3. Full Connection

### Modelling
1. Model CNN yang telah dibuat kemudian di optimizer menggunakan Adam
2. Hasil Training Model
   - Params: 
     * steps_per_epoch = 10
     * epochs= 120
   - Best Score Accuracy: 0.9810

### Evaluate Model
Confussion Matrix:


Accuracy:
| Label     | Accuracy |
| --------- | -------- |
| Apple     | 97.02    |
| Carambola | 100.00   |
| Plum      | 100.00   |
| Tomatoes  | 97.25    |
| Total     | 98.00    |

Classification Report:
| Fruit        | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| Apple        | 0.99      | 0.97   | 0.98     | 503     |
| Carambola    | 1.00      | 1.00   | 1.00     | 208     |
| Plum         | 1.00      | 1.00   | 1.00     | 231     |
| Tomatoes     | 0.93      | 0.97   | 0.95     | 218     |
|              |           |        |          |         |
| accuracy     |           |        | 0.98     | 1160    |
| macro avg    | 0.98      | 0.99   | 0.98     | 1160    |
| weighted avg | 0.98      | 0.98   | 0.98     | 1160    |


