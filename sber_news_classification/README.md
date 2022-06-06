Модель для выявления в новости события, соответствующего задержке ввода некоторого объекта в эксплуатацию.</br>


Exploration data analysis:  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shitkov/news_classification/blob/main/news_classification_EDA.ipynb)</br>
news classification with BERT: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shitkov/news_classification/blob/main/news_classification_EDA.ipynb)</br>

Положительных примеров: 329.</br>
Данных мало, можно аугментировать:
1. Сгенерировать заголовки для размеченного корпуса: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shitkov/news_classification/blob/main/news_classification_summarization.ipynb)</br>
2. Парафраз для положительных примеров: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shitkov/news_classification/blob/main/news_classification_paraphrase.ipynb)</br>
3. Обучить BERT на заголовках: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/shitkov/news_classification/blob/main/headlines_classification_bert.ipynb)</br>
На тестовых данных (классы сбалансированы, ~100 примеров) f-мера около 90% - намного лучше, чем на текстах без аугментации.
5. Дообучить языковую модель mT5/ruGPT3 на задачу генерации метки: для нормального качества это довольно долго. 
