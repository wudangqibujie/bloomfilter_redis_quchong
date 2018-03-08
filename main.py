import urls_create
import bloomfilter

urls = urls_create.Get_urls()
# print(urls)
bf = bloomfilter.BloomFilter()
aa=[]
for i in urls:
    if bf.isContains(i,"testurl"):
        print(i)
        aa.append(i)

    else:
        bf.insert(i,"testurl")

print(len(aa))

