import pathlib
import itertools
import sys
import concurrent.futures as cf

class fileseeker:
	def __init__(self):
		pass
	def get_all_files(self, path):
		def files_in_dir(x):
			try:
				return list(itertools.filterfalse(lambda x:x.is_dir(), x.iterdir()))
			except Exception as e:
				print(e, file=sys.stderr)
		try:
			path = pathlib.Path(path)
			dirs_to_seek = path.rglob("")
			with cf.ThreadPoolExecutor(max_workers=4) as ex:
				files = ex.map(files_in_dir, dirs_to_seek)
			return list(itertools.chain(files))
		except Exception as e:
			raise e
			

fseek = fileseeker()

fileiter = fseek.get_all_files("/home/iquant")

print(*fileiter[0])

