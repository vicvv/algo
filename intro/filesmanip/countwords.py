with open("programmingExpert.txt",'r') as file:
   print(sum(len((line.replace('\n','').replace('"','').replace(',','').replace('-','')).split()) for line in file.readlines()))
