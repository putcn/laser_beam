from embed import SentenceEncoder
from scipy import spatial
from text_processing import TokenLine, BPEfastApplyLine


encoder = SentenceEncoder("/LASER/models/bilstm.93langs.2018-12-26.pt", cpu=True, max_sentences=None, max_tokens=12000, sort_kind="mergesort")

sentences = [
    {
        "lang":"en",
        "content":"While the question of hamsters powering homes may seem a bit farcical, it should be noted that at one point humans did specifically breed a certain type of dog for the sole purpose of it just walking along at a steady pace on a giant wheel… (See our article The Curious Tale of Turnspit Dogs.)", 
    },{
        "lang": "zh",
        "content": "靠仓鼠产电功能这个问题似乎有些可笑，但却前有古人，人类曾经靠驱使狗狗跑轮子来烧炉子..."
    }
]

def pre_process(sentence, lang):
    # tokenrize
    sentence = TokenLine(sentence,lang=lang, romanize=True if lang == 'el' else False, lower_case=True)
    # bpe
    return BPEfastApplyLine(sentence, bpe_codes="/LASER/models/93langs.fcodes")

sentences = [pre_process(s["content"], s["lang"]) for s in sentences]
embs = encoder.encode_sentences(sentences)
print(embs)
print("similarity %f" % (1-spatial.distance.cosine(embs[0], embs[1])))