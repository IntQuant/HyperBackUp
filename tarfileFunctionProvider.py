import tarfile
import pathlib
#"/home/iquant/backup.tar.gz"
def make_archieve(archieve_path, files_to_pack, mode="w:gz", verbose=False)
	if type(archieve_path)!="str":
		raise TypeError("Archieve path needs to be a sting")
	if type(files_to_pack) not in ["list", "iter", "set"]:
		raise TypeError("Files_to_pack needs to be \
		iterable-like object of strings/pathes")
	
	tararch = tarfile.open(archieve_path, mode)
	
	files_to_pack = map(pathlib.Path(), files_to_pack)
	
	for i, cfile in enumerate(files_to_pack):
		if verbose:
			print(str(round(i/len(files_to_pack)*100))+"%", cfile, sep="\t\t")
		if cfile.exists():
			tararch.add(str(cfile))
		else:
			if verbose:
				print(cfile, "Nonexistent")
			
	tararch.close()
