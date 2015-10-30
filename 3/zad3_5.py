leng = 10 #dlugosc miarki
fline="|"
sline="0"
for x in range(0,leng,1):
	fline=fline+"----|"
	sline=sline+"    "+str(x+1)
final=fline+"\n"+sline
print(final)