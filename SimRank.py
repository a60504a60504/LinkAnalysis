from collections import defaultdict
import copy
import networkx as nx
import matplotlib.pyplot as plt
import csv
import time

def OpenGraphFile(Filename):
    with open(Filename, 'rb') as inf:
        G = nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), nodetype=int, encoding="utf-8")
    return G
    
def WriteCsvFile(Filename, data):
    with open(Filename+'.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Node u', 'Node v', 'SimRank'])
        for u in data:
            for v in data[u]:
                writer.writerow ([u,v,data[u][v]])
    
def Simrank(G, C=0.9, max_iter=100):
    
    def _is_converge(s1, s2, eps=1e-8):
        for i in s1.keys():
            for j in s1[i].keys():
                if abs(s1[i][j] - s2[i][j]) >= eps:
                    return False
        return True

    # init. vars
    sim_old = defaultdict(list)
    sim = defaultdict(list)
    for n in G.nodes():
        sim[n] = defaultdict(int)
        sim[n][n] = 1
        sim_old[n] = defaultdict(int)
        sim_old[n][n] = 0

    # recursively calculate simrank
    for iter_ctr in range(max_iter):
        if _is_converge(sim, sim_old):
            break
        sim_old = copy.deepcopy(sim)
        for u in G.nodes():
            for v in G.nodes():
                if u == v:
                    continue
                s_uv = 0.0
                for n_u in G.neighbors(u):
                    for n_v in G.neighbors(v):
                        s_uv += sim_old[n_u][n_v]
                if list(G.neighbors(u))==[] or list(G.neighbors(v))==[]:
                    sim[u][v] = 0.0
                else:
                    sim[u][v] = (C * s_uv / (len(list(G.neighbors(u))) * len(list(G.neighbors(v)))))
    return sim
if __name__ == '__main__':
    GraphFile = ['graph_1','graph_2','graph_3','graph_4','graph_5']
    for gf in GraphFile:
        G = OpenGraphFile(gf+'.txt')
        
        tStart = time.time()
        SR = Simrank(G, C=0.85, max_iter=100)
        tEnd = time.time()
        print ("SimRank cost %f sec" % (tEnd - tStart))
        
        print (gf,':')
        print ('SimRank:')
        for u in SR:
            for v in SR[u]:
                print (u," ",v," ",SR[u][v])
        print ()
        
        WriteCsvFile(gf+'SimRank', SR)
