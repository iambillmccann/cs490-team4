from uuid import uuid4


class TempStorage:
    def __init__(self):
        self.__storage = {}

    def __generate_uid(self) -> str:
        return str(uuid4())

    def create(self, to_save: dict) -> str:
        session_uid = self.__generate_uid()
        self.__storage[session_uid] = to_save
        return session_uid

    def read(self, session_uid: str) -> dict:
        return self.__storage.get(session_uid)

    def delete(self, session_uid: str) -> bool:
        if session_uid in self.__storage:
            del self.__storage[session_uid]
            return True
        return False
