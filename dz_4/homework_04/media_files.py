from abc import ABC

class MediaFile(ABC):
    def __init__(self, name, size, created_at, owner):
        self.name = name
        self.size = size
        self.created_at = created_at
        self.owner = owner

    def save(self, path):
        # сохранение файла
        pass

    def update(self):
    # обновление файла
        pass

    def delete(self):
        # удаление файла
        pass

    def convert(self, target_format):
        # конвертация файла
        pass

    def extract_features(self):
        # выгрузка фичей
        pass

class AudioFile(MediaFile):
    def __init__(self, name, size, created_at, owner, duration, bitrate):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.bitrate = bitrate

class VideoFile(MediaFile):
    def __init__(self, name, size, created_at, owner, duration, resolution):
        super().__init__(name, size, created_at, owner)
        self.duration = duration
        self.resolution = resolution

class PhotoFile(MediaFile):
    def __init__(self, name, size, created_at, owner, width, height):
        super().__init__(name, size, created_at, owner)
        self.width = width
        self.height = height

