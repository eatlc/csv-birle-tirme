import pandas as pd
import numpy as np
import statistics
import os


#Aşağıdaki iki fonksiyon csv'lerin yeni featurelerinin hesaplanması ve
#takip durumlarının belirtmek için son sütuna 1 veya 0 labelının eklenmesi amacıyla yazılmışıtır.

#LABİRENTİ TAKİP EDEN VERİLER BU FONKSİYONA GÖNDERİLİR
def todata1(df_0):
    # mean
    mean_x = statistics.mean(df_0['gazePointX'])
    mean_y = statistics.mean(df_0['gazePointY'])
    # median
    median_x = statistics.median(df_0['gazePointX'])
    median_y = statistics.median(df_0['gazePointY'])
    # std
    std_x = statistics.stdev(df_0['gazePointX'])
    std_y = statistics.stdev(df_0['gazePointY'])
    # quantile %25
    q25_x = np.percentile(df_0['gazePointX'], 25)
    q25_y = np.percentile(df_0['gazePointY'], 25)
    # quantiles %50
    q50_x = np.percentile(df_0['gazePointX'], 50)
    q50_y = np.percentile(df_0['gazePointY'], 50)
    # quantiles %75
    q75_x = np.percentile(df_0['gazePointX'], 75)
    q75_y = np.percentile(df_0['gazePointY'], 75)
    # min
    min_x = min(df_0['gazePointX'])
    min_y = min(df_0['gazePointY'])
    # max
    max_x = max(df_0['gazePointX'])
    max_y = max(df_0['gazePointY'])

    # Hesaplanan verilerin (feature'ların) tek satırda toplanması
    data = {'meanX': [mean_x], 'meanY': [mean_y], 'medianX': [median_x], 'medianY': [median_y],
            'stdX': [std_x], 'stdY': [std_y], 'quantiles25X': [q25_x], 'quantiles25Y': [q25_y],
            'quantiles50X': [q50_x], 'quantiles50Y': [q50_y], 'quantiles75X': [q75_x], 'quantiles75Y': [q75_y],
            'minX': [min_x], 'minY': [min_y], 'maxX': [max_x], 'maxY': [max_y], 'label': 1}

    return data

#LABİRENTİ TAKİP ETMEYEN VERİLER BU FONKSİYONA GÖNDERİLİR
def todata0(df_0):
        # mean
        mean_x = statistics.mean(df_0['gazePointX'])
        mean_y = statistics.mean(df_0['gazePointY'])
        # median
        median_x = statistics.median(df_0['gazePointX'])
        median_y = statistics.median(df_0['gazePointY'])
        # std
        std_x = statistics.stdev(df_0['gazePointX'])
        std_y = statistics.stdev(df_0['gazePointY'])
        # quantile %25
        q25_x = np.percentile(df_0['gazePointX'], 25)
        q25_y = np.percentile(df_0['gazePointY'], 25)
        # quantiles %50
        q50_x = np.percentile(df_0['gazePointX'], 50)
        q50_y = np.percentile(df_0['gazePointY'], 50)
        # quantiles %75
        q75_x = np.percentile(df_0['gazePointX'], 75)
        q75_y = np.percentile(df_0['gazePointY'], 75)
        # min
        min_x = min(df_0['gazePointX'])
        min_y = min(df_0['gazePointY'])
        # max
        max_x = max(df_0['gazePointX'])
        max_y = max(df_0['gazePointY'])

        # Hesaplanan verilerin (feature'ların) tek satırda toplanması
        data = {'meanX': [mean_x], 'meanY': [mean_y], 'medianX': [median_x], 'medianY': [median_y],
                'stdX': [std_x], 'stdY': [std_y], 'quantiles25X': [q25_x], 'quantiles25Y': [q25_y],
                'quantiles50X': [q50_x], 'quantiles50Y': [q50_y], 'quantiles75X': [q75_x], 'quantiles75Y': [q75_y],
                'minX': [min_x], 'minY': [min_y], 'maxX': [max_x], 'maxY': [max_y], 'label': 0}

        return data


#LABİRENT TAKİBİNİ YAPAN CSV'LERİN OKUNMASI
#Başlangıçta boş bir dataFrame oluşturuluyor.
df_son_1 = pd.DataFrame()

directory = os.fsencode(r"D:\optoel_staj\takipedilen") #Klasör yolunun yazılması
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if df_son_1.empty:
        df = pd.read_csv(r"D:\optoel_staj\takipedilen\\" + filename)
        data = todata1(df)
        df_son_1 = pd.DataFrame(data)
    else:
        df = pd.read_csv(r"D:\optoel_staj\takipedilen\\" + filename)
        data = todata1(df)
        df_new = pd.DataFrame.from_records(data)
        df_son_1 = pd.concat([df_son_1, df_new], ignore_index=True)



#LABİRENT TAKİBİNİ YAPMAYAN CSV'LERİN OKUNMASI
#Başlangıçta boş bir dataFrame oluşturuluyor.
df_son_2 = pd.DataFrame()

directory = os.fsencode(r"D:\optoel_staj\takipedilmeyen") #Klasör yolunun yazılması
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if df_son_2.empty:
        df = pd.read_csv(r"D:\optoel_staj\takipedilmeyen\\" + filename)
        data = todata0(df)
        df_son_2 = pd.DataFrame(data)
    else:
        df = pd.read_csv(r"D:\optoel_staj\takipedilmeyen\\" + filename)
        data = todata0(df)
        df_new = pd.DataFrame.from_records(data)
        df_son_2 = pd.concat([df_son_2, df_new], ignore_index=True)


#LABİRENT TAKİBİNİ YAPAN VE YAPMAYAN CSV'LERİN BİRLEŞTİRİLMESİ
df_son = pd.concat([df_son_1, df_son_2], ignore_index=True)
#BİRLEŞTİRİLEN CSV'LERİN KAYDEDİLMESİ
df_son.to_csv(r"D:\optoel_staj\csvSon.csv")