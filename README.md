# LinkAnalysis

## Implementation detail 
### Run.bat
* 將執行IBMdata2graph.py、HITS_Pagerank.py、SimRank.py
* 需要安裝套件
  * networkx
  * pandas
  * matplotlib
* 透過windows執行Run.bat
* 會將執行結果輸出分別存在各式開頭Output.txt
### IBMdata2graph.py
* 從project1的IBM資料產生兩筆有向圖(directed graph)
  * graph_7:其中一筆為在同一個transaction底下的items做單向(directed)連接e.g. 1 ---> 2 ---> 3 ---> 4
  * graph_8:另外一筆為在同一個transaction底下的items做雙向(bidirected)連接e.g. 1 <--> 2 <--> 3 <--> 4
### HITS_Pagerank.py
* 使用 networkx package輔助繪圖
* 計算graph_1到graph_8每個節點的authority/hub與pagerank
* HITS 
  * 產生 authority與hub
* Pagerank 
  * 產生 pr
  * alpha = 0.15 代表 damping factor=0.15
* 產生authority、hub、Pagerank的csv檔案
* 產生每種graph實際簡圖
### SimRank.py
* 使用 networkx package輔助繪圖
* 計算graph_1到graph_5每個節點連線的simrank
* Simrank
  * 產生simrank
  * C是damping factor設定為0.85
* 產生Simrank的csv檔案

---
## Result analysis and discussion 
### Graph Topology
* graph_1 <br />  
![image](https://github.com/a60504a60504/LinkAnalysis/blob/master/Picgraph_1.png)
* graph_2 <br /> 
![image](https://github.com/a60504a60504/LinkAnalysis/blob/master/Picgraph_2.png)
* graph_3 <br /> 
![image](https://github.com/a60504a60504/LinkAnalysis/blob/master/Picgraph_3.png)
* graph_4 <br /> 
![image](https://github.com/a60504a60504/LinkAnalysis/blob/master/Picgraph_4.png)
* graph_5 <br /> 
![image](https://github.com/a60504a60504/LinkAnalysis/blob/master/Picgraph_5.png)
* graph_6 <br /> 
![image](https://github.com/a60504a60504/LinkAnalysis/blob/master/Picgraph_6.png)
* graph_7 <br /> 
![image](https://github.com/a60504a60504/LinkAnalysis/blob/master/Picgraph_7.png)
* graph_8 <br /> 
![image](https://github.com/a60504a60504/LinkAnalysis/blob/master/Picgraph_8.png)

### HITS_Authority
#### graph_1
| 1   | 2   | 3   | 4   | 5   | 6   |
| --- |-----|-----|-----|-----|-----|
| 0.0 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
#### graph_2
| 1   | 2   | 3   | 4   | 5   |
|-----|-----|-----|-----|-----|
| 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
#### graph_3 
| 1                 | 2                 | 3                 | 4                 |
|-------------------|-------------------|-------------------|-------------------|
| 0.190983005521049 | 0.309016994478951 | 0.309016994478951 | 0.190983005521049 |
#### graph_4 
| 1                  | 2                  | 3                   | 4                  | 5                   | 7                   | 6                   |
|--------------------|--------------------|---------------------|--------------------|---------------------|---------------------|---------------------|
| 0.1394838930854497 | 0.1779120314091907 | 0.20082320536937326 | 0.1401777533243232 | 0.20142536348733986 | 0.08408849143863972 | 0.05608926188568348 |
#### graph_5 (取其中8 nodes)
| 1 | 8 | 11 | 168 | 227 | 253 | 264 | 307 |
|-----|-----------------------|-----------------------|------------------------|-----------------------|----------------------|------------------------|------------------------|
| 0.0 | 7.472963348981608e-20 | 7.472963348981608e-20 | 1.4165122344998102e-19 | 8.611631929121863e-20 | 9.41100944169924e-20 | 1.4746749256098907e-19 | 1.2752979217764556e-18 |
#### graph_6 (取其中8 nodes)
| 1 | 6 | 68 | 95 | 142 | 273 | 298 | 367 |
|-----|-----------------------|-----------------------|----------------------|-----------------------|----------------------|----------------------|-----------------------|
| 0.0 | 0.0011249976389747188 | 0.0030420277203979723 | 0.003442652083550649 | 0.0033371122512950904 | 0.004490627885974409 | 0.003270702401903986 | 0.0041102114307905455 |
#### graph_7 (取其中8 nodes)
| 4 | 5 | 26 | 48 | 9 | 28 | 19 | 35 |
|-----|-----------------------|----------------------|---------------------|-----|--------------------|-----|---------------------|
| 0.0 | 7.977898868747948e-28 | 0.010100369726265275 | 0.08485237254235313 | 0.0 | 0.1240714541232222 | 0.0 | 0.06635414460222441 |
#### graph_8 (取其中8 nodes)
| 4 | 5 | 26 | 48 | 9 | 28 | 19 | 35 |
|----------------------|----------------------|----------------------|----------------------|----------------------|--------------------|----------------------|----------------------|
| 0.006484718625091435 | 0.012418061161435873 | 0.034226297284237955 | 0.040469765210898574 | 0.040609927236660986 | 0.0896919012470277 | 0.030913654805859773 | 0.051366613955768366 |

### HITS_Hub
#### graph_1
| 1 | 2 | 3 | 4 | 5 | 6 |
|-----|-----|-----|-----|-----|-----|
| 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.0 |
#### graph_2
| 1 | 2 | 3 | 4 | 5 |
|-----|-----|-----|-----|-----|
| 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
#### graph_3 
| 1 | 2 | 3 | 4 |
|--------------------|--------------------|--------------------|--------------------|
| 0.1909830056647784 | 0.3090169943352216 | 0.3090169943352216 | 0.1909830056647784 |
#### graph_4 
| 1 | 2 | 3 | 4 | 5 | 7 | 6 |
|--------------------|----------------------|---------------------|--------------------|--------------------|---------------------|---------------------|
| 0.2754531765654345 | 0.047762306376935765 | 0.10868323971440082 | 0.1986595564890898 | 0.1837345993425369 | 0.06897240756733328 | 0.11673471394426906 |
#### graph_5 (取其中8 nodes)
| 1 | 8 | 11 | 168 | 227 | 253 | 264 | 307 |
|------------------------|-----|-----------------------|-----|-----------------------|-----------------------|------------------------|-----------------------|
| 1.0324628273669713e-19 | 0.0 | 9.257103567698106e-20 | 0.0 | 3.651281302596552e-21 | 4.645497342869489e-21 | 1.4836717751518094e-23 | 4.533719331071321e-19 |
#### graph_6 (取其中8 nodes)
| 1 | 6 | 68 | 95 | 142 | 273 | 298 | 367 |
|----------------------|-----|---------------------|----------------------|-----|-----------------------|-----|-----|
| 0.002691682627007344 | 0.0 | 0.00404574609271247 | 0.003837619270016946 | 0.0 | 0.0038878241901060054 | 0.0 | 0.0 |
#### graph_7 (取其中8 nodes)
| 4 | 5 | 26 | 48 | 9 | 28 | 19 | 35 |
|-----------------------|----------------------|---------------------|-----|---------------------|---------------------|---------------------|----------------------|
| 8.478256961332574e-28 | 0.014662529635953388 | 0.06903747708251352 | 0.0 | 0.09362031202212574 | 0.10002053141156911 | 0.04537462972065729 | 0.060553120041920656 |
#### graph_8 (取其中8 nodes)
| 4 | 5 | 26 | 48 | 9 | 28 | 19 | 35 |
|----------------------|----------------------|----------------------|---------------------|----------------------|---------------------|---------------------|---------------------|
| 0.006484718601431361 | 0.012418061198099947 | 0.034226297233030355 | 0.04046976516676028 | 0.040609927251899214 | 0.08969190119721432 | 0.03091365484215147 | 0.05136661398086176 |

### PageRank
#### graph_1
| 1 | 2 | 3 | 4 | 5 | 6 |
|---------------------|-------------------|---------------------|---------------------|---------------------|---------------------|
| 0.14595957523600261 | 0.167853496866862 | 0.17113757255045572 | 0.17163017313639323 | 0.17170405399576824 | 0.17171512821451823 |
#### graph_2
| 1 | 2 | 3 | 4 | 5 |
|-----|-----|-----|-----|-----|
| 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
#### graph_3 
| 1 | 2 | 3 | 4 |
|---------------------|---------------------|---------------------|---------------------|
| 0.23255809814453124 | 0.26744190185546873 | 0.26744190185546873 | 0.23255809814453124 |
#### graph_4 
| 1 | 2 | 3 | 4 | 5 | 7 | 6 |
|---------------------|---------------------|---------------------|--------------------|---------------------|---------------------|---------------------|
| 0.16902690367606024 | 0.14356677737444196 | 0.13918989663364953 | 0.1325617908579799 | 0.16166426917131696 | 0.12649943813058034 | 0.12749092415597096 |
#### graph_5 (取其中8 nodes)
| 1 | 8 | 11 | 168 | 227 | 253 | 264 | 307 |
|-----------------------|-----------------------|-----------------------|-----------------------|----------------------|-----------------------|-----------------------|----------------------|
| 0.0020499061207765227 | 0.0020938338790000787 | 0.0020938338790000787 | 0.0021566517080962716 | 0.002146695971891001 | 0.0022020223652715557 | 0.0024684404220471907 | 0.002277870573361635 |
#### graph_6 (取其中8 nodes)
| 1 | 6 | 68 | 95 | 142 | 273 | 298 | 367 |
|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|-----------------------|
| 0.0007951429435035324 | 0.0008496985327496081 | 0.0009049917877139021 | 0.0009191251228350132 | 0.0009145101783090725 | 0.0009454841606283452 | 0.0009083780689383312 | 0.0009271139322977424 |
#### graph_7 (取其中8 nodes)
| 4 | 5 | 26 | 48 | 9 | 28 | 19 | 35 |
|----------------------|----------------------|----------------------|---------------------|----------------------|---------------------|----------------------|----------------------|
| 0.024140543292009153 | 0.025951078395718682 | 0.031186542518848615 | 0.03775308020552477 | 0.024140543292009153 | 0.03098327233160916 | 0.024140543292009153 | 0.028011463894668277 |
#### graph_8 (取其中8 nodes)
| 4 | 5 | 26 | 48 | 9 | 28 | 19 | 35 |
|----------------------|---------------------|----------------------|---------------------|----------------------|--------------------|----------------------|---------------------|
| 0.026046341288714938 | 0.02713766715058221 | 0.031004712728167638 | 0.02835523477555381 | 0.026516647243889704 | 0.0340865783000946 | 0.024725045807823604 | 0.03167225541172875 |

### SimRank
#### graph_1
|   | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
|**1**| 1 | 0 | 0 | 0 | 0 | 0 |
|**2**| 0 | 1 | 0 | 0 | 0 | 0 |
|**3**| 0 | 0 | 1 | 0 | 0 | 0 |
|**4**| 0 | 0 | 0 | 1 | 0 | 0 |
|**5**| 0 | 0 | 0 | 0 | 1 | 0 |
|**6**| 0 | 0 | 0 | 0 | 0 | 1 |
#### graph_2
|   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
|**1**| 1 | 0 | 0 | 0 | 0 |
|**2**| 0 | 1 | 0 | 0 | 0 |
|**3**| 0 | 0 | 1 | 0 | 0 |
|**4**| 0 | 0 | 0 | 1 | 0 |
|**5**| 0 | 0 | 0 | 0 | 1 |
#### graph_3 
|   | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
|**1**| 1 | 0 | 0.73913 | 0 |
|**2**| 0 | 1 | 0 | 0.73913 |
|**3**| 0.73913 | 0 | 1 | 0 |
|**4**| 0 | 0.73913 | 0 | 1 |
#### graph_4 
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
|**1**| 1 | 0.372523954 | 0.425064327 | 0.47964778 | 0.446585268 | 0.420010017 | 0.46749608 |
|**2**| 0.372523954 | 1 | 0.583322677 | 0.352515833 | 0.494003447 | 0.614798736 | 0.379597473 |
|**3**| 0.425064327 | 0.583322677 | 1 | 0.470545783 | 0.451337599 | 0.491536438 | 0.399750199 |
|**4**| 0.47964778 | 0.352515833 | 0.470545783 | 1 | 0.430144078 | 0.451847896 | 0.55117996 |
|**5**| 0.446585268 | 0.494003447 | 0.451337599 | 0.430144078 | 1 | 0.434247646 | 0.374491845 |
|**6**| 0.420010017 | 0.614798736 | 0.491536438 | 0.451847896 | 0.434247646 | 1 | 0.614798736 |
|**7**| 0.46749608 | 0.379597473 | 0.399750199 | 0.55117996 | 0.374491845 | 0.614798736 | 1 |
#### graph_5 (取其中8 nodes)
| 0 | 1 | 8 | 11 | 168 | 227 | 253 | 264 | 307 |
|-----|-------------|---|-------------|-----|-------------|-------------|-------------|-------------|
|**1**| 1 | 0 | 0.073003248 | 0 | 0.006538008 | 0.003381009 | 0.002568105 | 0.004355618 |
|**8**| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
|**11**| 0.073003248 | 0 | 1 | 0 | 0 | 0 | 0.00137227 | 0.004643829 |
|**168**| 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
|**227**| 0.006538008 | 0 | 0 | 0 | 1 | 0.061502073 | 0 | 0 |
|**253**| 0.003381009 | 0 | 0 | 0 | 0.061502073 | 1 | 0 | 0 |
|**264**| 0.002568105 | 0 | 0.00137227 | 0 | 0 | 0 | 1 | 0 |
|**307**| 0.004355618 | 0 | 0.004643829 | 0 | 0 | 0 | 0 | 1 |


---
## Computation performance analysis 
### HITS
一個iteration所需的time complexity O(|E(G)|)
#### 表為每張graph運行時間(sec)
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|----------|----------|----------|----------|----------|
| 0 | 0 | 0 | 0.001029 | 0.109675 | 3.056393 | 0.013964 | 0.015622 |

### Pagerank
所需的time complexity O(n+m) n是node數 m是edge數
#### 表為每張graph運行時間(sec)
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0.000998 | 0 | 0.046833 | 0.000997 | 0 |

### Simrank
所需的time complexity O(Kn^2d)  K是The number of iterations n是node數 d是|I(a)|\*|I(b)|的平均
#### 表為每張graph運行時間(sec)
| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| 0 | 0 | 0 | 0.031243 | 13.584184 |

---
## Discussion
### More limitations about link analysis algorithms 
應該對同一時間段產生的網站節點，做HITS或Pagerank才有意義。
### Can link analysis algorithms really find the “important” pages from Web? 
首先要先了解什麼是"important"的，如果是指擁有大量進出連結的網頁代表重要的，那在HITS、Pagerank中找出來的高數值都代表著過去相當多的連進連出。
但如果"重要"的是網頁內容品質，那以HITS與pagerank可能在某些情況無法保證內容品質是高的、並且有可能有一些剛出爐的網頁其內容品質很高卻被HITS、Pagerank評為0，只因為沒有連結。
### What are practical issues when implement these algorithms in a real Web? 
    Performance discussion (time cost) 
- 比較Time cost來說，使用Pagerank運算會比HITS來的快速一些，但HITS的資訊量會比Pagerank來的多
- 至於simrank屬於linked-based的相似度測量，效率肯定最差
- 但是如果想要再精準度上在做精進的測量，勢必需要更多的節點資訊，那計算量肯定會比目前的演算法複雜，至於如何取捨就得看使用者想要的重要資料定義精細或模糊，運行時間的取捨可能也會是重點
- 當然也有一種方法就是先快速大範圍搜索，找出可能重要的節點再運用複雜精密的評估演算法找出重要資訊，或許可以應用在生活。
### Any new idea about the link analysis algorithm? 
產生一個時間函數，時間越靠近現在的權重數值越高、越古老的權重數值越低。
並在simrank高的兩端降低納入HITS或pagerank的權重。
### What is the effect of “C” parameter in SimRank? 
用來做遞減參數必須介於0與1之間，假設有A節點到B節點會經過5層，那就會有總共C^5的遞減進入計算，也就是說節點相差越遠越不相似的概念。
### Design a new link-based similarity measurement 
可以基於原本simrank的架構下，另外加上找出兩個endpoint間內容的差異性，透過一些transform將節點的內容transform到2維影像，再透過兩張2維影像辨識分析相識度給予一個權重帶入simrank，或許可以增加simrank評估準確度。
