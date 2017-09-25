import pathlib
import itertools
import sys
import concurrent.futures as cf

def get_all_files(path):
	def files_in_dir(x):
		out = []
		try:
			out = list(itertools.filterfalse(lambda x:x.is_dir(), x.iterdir()))
		except PermissionError as e:
			print("[Warn] Access denied to", x, file=sys.stderr)
		if len(out)>0:
			return out
	try:
		path = pathlib.Path(path)
		dirs_to_seek = path.rglob("")
		with cf.ThreadPoolExecutor(max_workers=4) as ex:
			files = itertools.filterfalse(lambda x:x is None, ex.map(files_in_dir, dirs_to_seek))
		return list(itertools.chain(*files))
	except Exception as e:
		raise e

#Some testing
if __name__ == "__main__":
	print("Starting test of 'get_all_files'")
	fileiter = get_all_files("/home/")
	print(*fileiter[:30], sep="\n")
	print("Found", len(fileiter), "files")
	print("Ended test of 'get_all_files'")

