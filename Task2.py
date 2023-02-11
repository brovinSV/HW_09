import string

class TextProcessor:
    """
    Обробка текстових даних
    """
    def __init__(self):
        self._p = string.punctuation

    def get_clean_string(self, text):
        for p in string.punctuation:
            if p in text:
                text = text.replace(p, '')
        return print(text.strip())

    def __is_punktiantian(self, p):
        if p in self._p:
            return True
        else:
            return False

class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ''

    def set_clean_text(self, txt):
        self.__clean_string = self.__text_processor.get_clean_string(txt)

    @property
    def clean_string(self):
        print("Cleaned up text output")
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self._datalist = TextLoader()

    def process_texts(self, text_list):
        for text in text_list:
            self._datalist.set_clean_text(text)
        print(self._datalist.clean_string)



data_text = ('- Мама мыла раму, а Маша помогала. (из прописи 1 класса)', '$Hello, world$', '!!!123!!!')
list_text = DataInterface()
list_text.process_texts(data_text)

