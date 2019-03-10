from PIL import Image,ImageFile
import imagehash,os, difflib
from glob import glob
#サイズの大きな画像をスキップしない
ImageFile.LOAD_TRUNCATED_IMAGES = True

hash_a = imagehash.phash(Image.open('./a_resize_cut_a.png'))
hash_b = imagehash.phash(Image.open('./a_resize_cut_b.png'))
print('hash_a=')
print(hash_a)
print('hash_b=')
print(hash_b)

sub = hash_a - hash_b
print(sub)
hash_a = str(hash_a)
hash_b = str(hash_b)
diff = difflib.SequenceMatcher(None, hash_a, hash_b).ratio()
print('diff=')
print(diff)
