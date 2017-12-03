from modules.grab_list import GrabList
from modules.crack.blockchain import Blockchain


gl = GrabList('targets')
cbl = Blockchain(passphrases=gl.list(), chunks=10, threads=98)
cbl.run()

# import winsound
# winsound.Beep(2500, 1000)
