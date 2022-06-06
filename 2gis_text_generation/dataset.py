import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):

    def __init__(self, texts, titles, tokenizer, source_len, summ_len):
        self.texts = texts
        self.summaries = titles
        self.tokenizer = tokenizer
        self.source_len = source_len
        self.summ_len = summ_len
        
    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        summary = self.summaries[idx]

        text = self.tokenizer.batch_encode_plus(
                [text],
                max_length=self.source_len,
                padding='max_length',
                truncation=True,
                return_tensors='pt'
            )
        summary = self.tokenizer.batch_encode_plus(
                [summary],
                max_length=self.summ_len,
                padding='max_length',
                truncation=True,
                return_tensors='pt'
            )

        source_ids = text['input_ids'].squeeze()
        source_mask = text['attention_mask'].squeeze()
        target_ids = summary['input_ids'].squeeze()
        target_mask = summary['attention_mask'].squeeze()

        return {
            'input_ids': source_ids.to(dtype=torch.long), 
            'attention_mask': source_mask.to(dtype=torch.long), 
            'target_ids': target_ids.to(dtype=torch.long),
            'target_attention_mask': target_mask.to(dtype=torch.long)
            }
