from abc import ABC, abstractmethod

class RemoteStorage(ABC):
    
    @abstractmethod
    def upload(self, file, remote_path):
        # загрузка файл в удаленное хранилище
        pass

    @abstractmethod
    def download(self, file, remote_path):
        # скачивание файла из удаленного хранилища
        pass

    @abstractmethod
    def delete(self, file, remote_path):
        # удаление файла в удаленном хранилище
        pass

class CloudStorage(RemoteStorage):
    
    def upload(self, file, remote_path):
        pass

    def download(self, file, remote_path):
        pass

    def delete(self, file, remote_path):
        pass

class RemoteServerStorage(RemoteStorage):
    
    def upload(self, file, remote_path):
        pass

    def download(self, file, remote_path):
        pass

    def delete(self, file, remote_path):
        pass

class S3LikeStorage(RemoteStorage):
    
    def upload(self, file, remote_path):
        pass

    def download(self, file, remote_path):
        pass

    def delete(self, file, remote_path):
        pass
