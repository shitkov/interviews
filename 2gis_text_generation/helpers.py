import re
import os
import os.path
import json
import gzip
from razdel import tokenize
from bs4 import BeautifulSoup

class ExtData:
    
    def __init__(self, path, lines):
        '''
        path: path to json archive
        lines: lines for work
        '''
        self.path = path
        self.lines = lines

    def _clean_text(self, text):
        '''
        Clean input text
        '''
        soup = BeautifulSoup(text, features="html.parser")
        
        for script in soup(["script", "style"]):
            script.extract()
        
        text = soup.get_text()
        
        text = re.sub(r'[^А-Яа-я0-9ЁёA-Za-z :%.,!?-]', ' ', text)
        text = re.sub(r" +", " ", text).strip()
        text = text.replace(' .', '.')
        text = text.replace(' ,', ',')
        
        return text
    
    def load_data(self):
        '''
        1. Download archived file
        2. Unpacking
        3. Cleaning data
        '''
        # download compressed data
        os.system('wget ' + self.path)

        # unpacking
        with gzip.open(self.path.split('/')[-1], 'rb') as f:
            file_content = f.read()
            file_content = file_content.decode('utf-8')
            file_content = file_content.splitlines()

        # cleaning
        texts = []
        titles = []
        for line in file_content[:self.lines]:
            try:
                s = json.loads(line)
                text = self._clean_text(s['text'])
                title = self._clean_text(s['title'])
                
                if text != '' and title != '':
                    texts.append(text)
                    titles.append(title)
            except:
                pass
        
        return texts, titles

    def get_summ_len(self, data):
        '''
        Get maximum summary length
        '''
        summ_len_list = [len(list(tokenize(i))) for i in data]
        summ_max_len = np.max(summ_len_list)
        summ_len = min((int(summ_max_len/10) + 1) * 10, MAX_LEN)
        return summ_len
