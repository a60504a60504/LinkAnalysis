import networkx as nx
import matplotlib.pyplot as plt
import csv
import time

def OpenGraphFile(Filename):
    with open(Filename, 'rb') as inf:
        G = nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), nodetype=int, encoding="utf-8")
    return G
    
def WriteCsvFile(Filename, data):
    with open(Filename+'.csv', 'w') as outfile:
        w = csv.DictWriter(outfile, data.keys())
        w.writeheader()
        w.writerow(data)

if __name__ == '__main__':
    GraphFile = ['graph_1','graph_2','graph_3','graph_4','graph_5','graph_6','graph_7','graph_8']
    for gf in GraphFile:
        G = OpenGraphFile(gf+'.txt')
        
        tStart = time.time()
        h,a = nx.hits(G, max_iter=1000)
        tEnd = time.time()
        print ("HITS cost %f sec" % (tEnd - tStart))
        
        tStart = time.time()
        pr = nx.pagerank(G, alpha=0.15)
        tEnd = time.time()
        print ("PageRank cost %f sec" % (tEnd - tStart))
        
        print (gf,':')
        print ('Hub:')
        for Hub in h:
            print (Hub,':',h[Hub])
        print ('Authority:')
        for Authority in a:
            print (Authority,':',a[Authority])
        print ('PageRank:')
        for PageRank in pr:
            print (PageRank,':',pr[PageRank])
        print ()
        WriteCsvFile(gf+'Hub', h)
        WriteCsvFile(gf+'Authority', a)
        WriteCsvFile(gf+'PageRank', pr)

        nx.draw_networkx(G)
        plt.axis('off')
        plt.draw()
        plt.savefig('Pic'+gf+'.png')
        plt.close()