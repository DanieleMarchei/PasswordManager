import getpass
import crypto

print "Password Manager\n"

pwd = getpass.getpass("Password > ")

crypto.encrypt(pwd, "original.txt", "encoded.enc")

crypto.decrypt(pwd, "encoded.enc", "decoded.txt")
