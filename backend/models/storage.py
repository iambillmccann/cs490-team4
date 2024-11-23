from uuid import uuid4


class TempStorage:
    def __init__(self):
        self.__storage = {}

    def __generate_uid(self) -> str:
        return str(uuid4())

    def create(self, resume_text: str, job_description: str) -> str:
        session_uid = self.__generate_uid()
        self.__storage[session_uid] = {
            "resume_text": resume_text,
            "job_description": job_description
        }

        return session_uid

    def read(self, session_uid: str) -> dict:
        return self.__storage.get(session_uid)

    def delete(self, session_uid: str) -> bool:
        if session_uid in self.__storage:
            del self.__storage[session_uid]
            return True
        return False

    def update(self, session_uid: str, resume_text: str, job_description: str) -> bool | str:
        if session_uid in self.__storage:
            if resume_text and job_description:
                self.__storage[session_uid] = {
                    "resume_text": resume_text,
                    "job_description": job_description
                }
            elif resume_text:
                self.__storage[session_uid]["resume_text"] = resume_text
            elif job_description:
                self.__storage[session_uid]["job_description"] = job_description
            else:
                return False
            return session_uid
