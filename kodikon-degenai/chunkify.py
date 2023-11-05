import pickle
f=open("data.txt","rb+")
with open("data.txt","rb") as g:
    r=pickle.load(g)
    e=pickle.load(f)
pickle.dump(e+r,f)
print(len(e+r))
f.close()