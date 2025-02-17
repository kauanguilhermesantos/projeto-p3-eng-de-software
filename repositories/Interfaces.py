from abc import ABC, abstractmethod

class IRegisterUser(ABC):
    @abstractmethod
    def register_user(self, connect):
        pass

class IRegisterBook(ABC):
    @abstractmethod
    def register_book(self, connect):
        pass

class ISearchBook(ABC):
    @abstractmethod
    def search_book(self, connect):
        pass

class IReserveBook(ABC):
    @abstractmethod
    def reserve_book(self, connect):
        pass
