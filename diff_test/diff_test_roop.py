from PIL import Image,ImageFile
import imagehash,os, difflib
from glob import glob
#サイズの大きな画像をスキップしない

#アプリから送られてきた画像のdhash
test_hash='21a161c4c8c8d8d8'

#マスター画像のdhash
master_hash_list = [
'21a161c4c8c8d8d8',
'21a121c4d8c8d8d8',
'0c18a7669697d3c8',
'0c1cbb6ed693d3c8',
'e0e8da7229f1d0e9',
'e0c89a7228f1d3e9',
'34baea48cccc9ef8',
'24b8ea48ccccb6f8',
'c36eb85323c42eb9',
'c36e789383546e99'
]

for master_hash in master_hash_list:
	print(master_hash)
	diff = difflib.SequenceMatcher(None, test_hash, master_hash).ratio()
	print('diff=%f' % diff)

