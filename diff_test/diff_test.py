from PIL import Image,ImageFile
import imagehash,os, difflib
from glob import glob

hash_a='21a161c4c8c8d8d8'
hash_b='21a121c4d8c8d8d8'
diff = difflib.SequenceMatcher(None, hash_a, hash_b).ratio()
print(hash_a)
print(hash_b)
print('diff=%f' % diff)
print('---------------------')

hash_a='0c18a7669697d3c8'
hash_b='0c1cbb6ed693d3c8'
diff = difflib.SequenceMatcher(None, hash_a, hash_b).ratio()
print(hash_a)
print(hash_b)
print('diff=%f' % diff)
print('---------------------')

hash_a='e0e8da7229f1d0e9'
hash_b='e0c89a7228f1d3e9'
diff = difflib.SequenceMatcher(None, hash_a, hash_b).ratio()
print(hash_a)
print(hash_b)
print('diff=%f' % diff)
print('---------------------')

hash_a='34baea48cccc9ef8'
hash_b='24b8ea48ccccb6f8'
diff = difflib.SequenceMatcher(None, hash_a, hash_b).ratio()
print(hash_a)
print(hash_b)
print('diff=%f' % diff)
print('---------------------')

hash_a='e0e8da7229f1d0e9'
hash_b='24b8ea48ccccb6f8'
diff = difflib.SequenceMatcher(None, hash_a, hash_b).ratio()
print(hash_a)
print(hash_b)
print('diff=%f' % diff)
print('---------------------')
