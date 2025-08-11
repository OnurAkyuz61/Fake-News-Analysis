# -*- coding: utf-8 -*-
"""
Sahte Haber Analizi - Yardımcı Fonksiyonlar
Bu dosya analiz ve görselleştirme için yardımcı fonksiyonları içerir.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import re
from datetime import datetime

def load_and_prepare_data(fake_path='../data/Fake.csv', real_path='../data/True.csv'):
    """
    Sahte ve gerçek haber veri setlerini yükler ve hazırlar
    """
    print("📁 Veri setleri yükleniyor...")
    
    fake_news = pd.read_csv(fake_path)
    real_news = pd.read_csv(real_path)
    
    # Etiketleme
    fake_news['label'] = 0
    real_news['label'] = 1
    fake_news['type'] = 'Sahte'
    real_news['type'] = 'Gerçek'
    
    # Birleştirme
    df = pd.concat([fake_news, real_news], ignore_index=True)
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Temizleme
    df = df.dropna(subset=['title', 'text'])
    df = df[df['title'].str.strip() != '']
    df = df[df['text'].str.strip() != '']
    
    # Metin özellikleri
    df['title_length'] = df['title'].str.len()
    df['text_length'] = df['text'].str.len()
    df['word_count'] = df['text'].str.split().str.len()
    df['combined_text'] = df['title'] + ' ' + df['text']
    
    print(f"✅ Veri hazırlandı: {len(df):,} haber")
    return df

def create_wordcloud_advanced(text_data, title, color_scheme='viridis', max_words=100):
    """
    Gelişmiş kelime bulutu oluşturur
    """
    combined_text = ' '.join(text_data.astype(str))
    
    # Yaygın kelimeleri filtrele
    stop_words = set(['the', 'and', 'to', 'of', 'a', 'in', 'is', 'it', 'you', 'that', 
                     'he', 'was', 'for', 'on', 'are', 'as', 'with', 'his', 'they'])
    
    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white',
        colormap=color_scheme,
        max_words=max_words,
        relative_scaling=0.5,
        stopwords=stop_words,
        random_state=42
    ).generate(combined_text)
    
    return wordcloud

def plot_distribution_comparison(df, column, title, save_path=None):
    """
    Sahte vs gerçek haber için dağılım karşılaştırması yapar
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Histogram
    axes[0].hist(df[df['type'] == 'Sahte'][column], alpha=0.7, 
                label='Sahte', bins=50, color='#ff6b6b')
    axes[0].hist(df[df['type'] == 'Gerçek'][column], alpha=0.7, 
                label='Gerçek', bins=50, color='#4ecdc4')
    axes[0].set_title(f'{title} - Histogram', fontweight='bold')
    axes[0].set_xlabel(column)
    axes[0].set_ylabel('Frekans')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Box plot
    sns.boxplot(data=df, x='type', y=column, ax=axes[1])
    axes[1].set_title(f'{title} - Box Plot', fontweight='bold')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()

def generate_summary_report(df):
    """
    Kapsamlı özet raporu oluşturur
    """
    report = {
        'Genel Bilgiler': {
            'Toplam Haber Sayısı': f"{len(df):,}",
            'Sahte Haber Sayısı': f"{len(df[df['label'] == 0]):,}",
            'Gerçek Haber Sayısı': f"{len(df[df['label'] == 1]):,}",
            'Sahte Haber Oranı': f"{len(df[df['label'] == 0]) / len(df) * 100:.1f}%",
            'Veri Seti Dengeli mi': 'Evet' if abs(len(df[df['label'] == 0]) - len(df[df['label'] == 1])) < len(df) * 0.1 else 'Hayır'
        },
        'Metin İstatistikleri': {
            'Ortalama Başlık Uzunluğu': f"{df['title_length'].mean():.0f} karakter",
            'Ortalama Metin Uzunluğu': f"{df['text_length'].mean():.0f} karakter", 
            'Ortalama Kelime Sayısı': f"{df['word_count'].mean():.0f} kelime",
            'Sahte Haber Ort. Uzunluk': f"{df[df['type'] == 'Sahte']['text_length'].mean():.0f} karakter",
            'Gerçek Haber Ort. Uzunluk': f"{df[df['type'] == 'Gerçek']['text_length'].mean():.0f} karakter"
        }
    }
    
    if 'subject' in df.columns:
        subject_counts = df['subject'].value_counts()
        fake_ratios = df.groupby('subject')['label'].apply(lambda x: (x == 0).mean() * 100)
        
        report['Konu Analizi'] = {
            'Toplam Konu Sayısı': len(subject_counts),
            'En Popüler Konu': f"{subject_counts.index[0]} ({subject_counts.iloc[0]} haber)",
            'En Yüksek Sahte Oran': f"{fake_ratios.idxmax()} ({fake_ratios.max():.1f}%)",
            'En Düşük Sahte Oran': f"{fake_ratios.idxmin()} ({fake_ratios.min():.1f}%)"
        }
    
    return report

def save_analysis_results(df, save_dir='../reports/'):
    """
    Analiz sonuçlarını dosyalara kaydeder
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Özet istatistikler
    summary_stats = df.groupby('type').agg({
        'title_length': ['count', 'mean', 'std', 'min', 'max'],
        'text_length': ['mean', 'std', 'min', 'max'],
        'word_count': ['mean', 'std', 'min', 'max']
    }).round(2)
    
    summary_stats.to_csv(f'{save_dir}ozet_istatistikler_{timestamp}.csv')
    
    # Konu analizi (eğer varsa)
    if 'subject' in df.columns:
        subject_analysis = pd.crosstab(df['subject'], df['type'])
        subject_analysis.to_csv(f'{save_dir}konu_analizi_{timestamp}.csv')
    
    print(f"💾 Analiz sonuçları kaydedildi: {timestamp}")

def print_colored_header(text, color='blue'):
    """
    Renkli başlık yazdırır
    """
    colors = {
        'blue': '\033[94m',
        'green': '\033[92m',
        'red': '\033[91m',
        'yellow': '\033[93m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'end': '\033[0m'
    }
    
    print(f"{colors.get(color, '')}{text}{colors['end']}")
