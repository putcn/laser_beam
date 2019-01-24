from embed import SentenceEncoder

encoder = SentenceEncoder("/LASER/models/bilstm.93langs.2018-12-26.pt", cpu=True, max_sentences=None, max_tokens=12000, sort_kind="mergesort")

print(encoder.encode_sentences(["i like bananas"]))