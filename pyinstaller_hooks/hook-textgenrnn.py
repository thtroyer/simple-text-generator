
# datas=[
#     # ('textgenrnn/textgenrnn_vocab.json', 'textgenrnn')
#     ('textgenrnn/*', 'textgenrnn')
# ]
from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all('textgenrnn')
