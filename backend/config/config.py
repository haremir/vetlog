# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 14:50:36 2024

@author: emirh
"""

import os
from pathlib import Path

# Proje kök dizini
BASE_DIR = Path(__file__).resolve().parent.parent

# Veritabanı bağlantı ayarları
DATABASE = {
    'ENGINE': 'sqlite',
    'NAME': os.path.join(BASE_DIR, 'database', 'vetlog.db'),  # SQLite veritabanı dosya yolu
}

# Uygulama ayarları
APP_SETTINGS = {
    'DEBUG': True,  # Geliştirme aşamasında True, dağıtımda False yapılacak
    'SECRET_KEY': os.getenv('SECRET_KEY', 'bu-cok-gizli-bir-anahtar'),  # Güvenlik için gizli anahtar
    'JWT_EXPIRATION_DELTA': 60 * 60 * 24,  # JWT token süresi (1 gün)
}

# Diğer ayarlar
NOTIFICATION_SETTINGS = {
    'REMINDER_DAYS': 3,  # Aşı/bakım hatırlatmaları için gün sayısı. Kaç gün kala haberdar edilinmeli.
}
