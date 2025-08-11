# 📁 Proje Yapısı - Fake News Analysis

## 🗂️ Klasör Organizasyonu

```
fake-or-real-news-analysis/
├── 📁 notebooks/                     # Jupyter notebook'ları
│   ├── data_exploration.ipynb        # Veri keşfi ve detaylı tablolar
│   ├── comprehensive_analysis.ipynb  # Kapsamlı görselleştirmeler
│   ├── visualizations.ipynb         # Gelişmiş görselleştirmeler
│   ├── advanced_analysis.ipynb      # İleri düzey analiz ve NLP
│   ├── data_analysis.ipynb          # Veri analizi ve istatistikler
│   └── model_development.ipynb      # Model geliştirme ve ML
├── 📁 data/                          # Veri setleri
│   ├── Fake.csv                     # Sahte haber verisi (62MB)
│   └── True.csv                     # Gerçek haber verisi (53MB)
├── 📁 outputs/                       # Çıktı dosyaları
│   ├── 📁 plots/                    # Kaydedilen grafikler (PNG)
│   ├── 📁 models/                   # Eğitilmiş modeller
│   └── 📁 reports/                  # Raporlar ve dokümantasyon
├── 📁 src/                          # Kaynak kod dosyaları
├── requirements.txt                 # Python bağımlılıkları
└── project_structure.md            # Bu dosya
```

## 📊 Notebook'ların İçeriği

### 1. **data_exploration.ipynb**
- 🔍 Temel veri keşfi
- 📊 Detaylı istatistik tabloları
- 📈 Temel görselleştirmeler
- 🎯 Veri kalitesi analizi

### 2. **comprehensive_analysis.ipynb**
- 📊 Kapsamlı görselleştirmeler
- 📅 Tarih bazında analizler
- 🔥 Korelasyon analizleri
- 📈 Trend analizleri

### 3. **visualizations.ipynb**
- 🎨 Gelişmiş görselleştirmeler
- 📊 İnteraktif grafikler
- 🔍 Detaylı karşılaştırmalar
- 📈 Çoklu metrik analizleri

### 4. **advanced_analysis.ipynb**
- 🔬 NLP analizleri
- 📊 TF-IDF analizleri
- 🔤 Kelime frekans analizleri
- 🎯 Metin madenciliği

### 5. **data_analysis.ipynb**
- 📊 İstatistiksel testler
- 📈 Hipotez testleri
- 🔍 Dağılım analizleri
- 📊 Karşılaştırmalı istatistikler

### 6. **model_development.ipynb**
- 🤖 Makine öğrenmesi modelleri
- 📊 Model performans değerlendirmesi
- 💾 Model kaydetme
- 🎯 Özellik mühendisliği

## 🎨 Grafik Kaydetme Sistemi

Her notebook'ta üretilen tüm grafikler otomatik olarak `outputs/plots/` klasörüne PNG formatında kaydedilir:

- **Yüksek kalite**: 300 DPI
- **Format**: PNG
- **Dosya adlandırma**: Sıralı numaralandırma (01_, 02_, vb.)
- **Boyut optimizasyonu**: `bbox_inches='tight'`

## 📋 Özellikler

✅ **Düzenli klasör yapısı**
✅ **Otomatik grafik kaydetme**
✅ **Güncellenmiş dosya yolları**
✅ **Modüler notebook yapısı**
✅ **Kapsamlı dokümantasyon**
✅ **Yüksek kaliteli görselleştirmeler**

## 🚀 Kullanım

1. `notebooks/` klasöründeki notebook'ları sırayla çalıştırın
2. Grafikler otomatik olarak `outputs/plots/` klasörüne kaydedilir
3. Modeller `outputs/models/` klasörüne kaydedilir
4. Raporlar `outputs/reports/` klasöründe bulunur

## 📊 Veri Seti Bilgileri

- **Toplam**: 44,898 haber
- **Sahte**: 23,481 haber
- **Gerçek**: 21,417 haber
- **Boyut**: ~115MB
- **Sütunlar**: title, text, subject, date, label, type
