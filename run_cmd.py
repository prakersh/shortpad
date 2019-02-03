import os
import subprocess 
import sys

def runcmd(cmd):
	out = subprocess.Popen(cmd,
            shell = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            close_fds=True)
	(stdout, stderr) = out.communicate()
	if 'byte' in str(type(stdout)) :
		stdout = stdout.decode("utf-8")
	if 'byte' in str(type(stderr)) :
		stderr = stderr.decode("utf-8")
	ret =  (out.returncode)
	return (ret, stdout ,stderr)
def main(*agrs):
	runcmd(sys.argv[1])
if __name__ =="__main__":
	main()
