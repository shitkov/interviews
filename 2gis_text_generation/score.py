import numpy as np
from rouge import Rouge

def get_rouge_score(hypothesis, reference):
    rouge = Rouge()

    hypothesis = [i if len(i) > 0 else 'empty generate error' for i in hypothesis]
    
    scores = rouge.get_scores(hypothesis, reference)
    r1_fm = np.mean([s['rouge-1']['f'] for s in scores])
    r2_fm = np.mean([s['rouge-2']['f'] for s in scores])
    rlcs_fm = np.mean([s['rouge-l']['f'] for s in scores])
    return round(np.mean([r1_fm, r2_fm, rlcs_fm]), 3)
