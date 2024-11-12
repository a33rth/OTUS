from datetime import datetime

# 1. Базовый класс для медиа-файлов
class MediaFile:
    def __init__(self, name, size, created_at, owner):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner

    def save(self):
        # Логика сохранения файла
        pass

    def delete(self):
        # Логика удаления файла
        pass

    def update_metadata(self, **kwargs):
        # Логика обновления метаданных
        pass

# 2. Классы для различных типов медиа-файлов
class AudioFile(MediaFile):
    def __init__(self, name, size, created_at, owner, sample_rate):
        super().__init__(name, size, created_at, owner)
        self.sample_rate = sample_rate

    def extract_features(self):
        # Извлечение особенностей из аудио
        pass

    def convert(self, new_format):
        # Конвертация аудио в другой формат
        pass

class VideoFile(MediaFile):
    def __init__(self, name, size, created_at, owner, resolution, duration):
        super().__init__(name, size, created_at, owner)
        self.resolution = resolution
        self.duration = duration

    def extract_features(self):
        # Извлечение особенностей из видео
        pass

    def convert(self, new_format):
        # Конвертация видео в другой формат
        pass

class PhotoFile(MediaFile):
    def __init__(self, name, size, created_at, owner, iso, focal_length):
        super().__init__(name, size, created_at, owner)
        self.iso = iso
        self.focal_length = focal_length

    def extract_features(self):
        # Извлечение особенностей из фото
        pass

    def convert(self, new_format):
        # Конвертация фото в другой формат
        pass

# 3. Базовый класс для хранения
class Storage:
    def upload(self, file):
        # Загрузка файла в хранилище
        pass

    def download(self, file_name):
        # Скачивание файла из хранилища
        pass

    def delete(self, file_name):
        # Удаление файла из хранилища
        pass

# 4. Классы для конкретных типов хранилищ
class LocalStorage(Storage):
    def upload(self, file):
        print(f"Uploading {file.name} to local storage")

    def download(self, file_name):
        print(f"Downloading {file_name} from local storage")

class CloudStorage(Storage):
    def upload(self, file):
        print(f"Uploading {file.name} to cloud storage")

    def download(self, file_name):
        print(f"Downloading {file_name} from cloud storage")

class RemoteStorage(Storage):
    def upload(self, file):
        print(f"Uploading {file.name} to remote server")

    def download(self, file_name):
        print(f"Downloading {file_name} from remote server")

# Примеры использования
audio_file = AudioFile(name="song.mp3", size=5000, created_at=datetime.now(), owner="User", sample_rate=44100)
video_file = VideoFile(name="movie.mp4", size=20000, created_at=datetime.now(), owner="User", resolution="1080p", duration=120)
photo_file = PhotoFile(name="image.jpg", size=3000, created_at=datetime.now(), owner="User", iso=100, focal_length=35)

local_storage = LocalStorage()
local_storage.upload(audio_file)
local_storage.download("song.mp3")

cloud_storage = CloudStorage()
cloud_storage.upload(video_file)
cloud_storage.download("movie.mp4")

remote_storage = RemoteStorage()
remote_storage.upload(photo_file)
remote_storage.download("image.jpg")
