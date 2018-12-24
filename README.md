# LinkAnalysis

## Implementation detail 
### Run.bat
* 將執行IBMdata2graph.py、HITS_Pagerank.py、SimRank.py
* 需要安裝套件
  * networkx
  * pandas
  * matplotlib
* 透過windows執行Run.bat
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
### SimRank.py
* 使用 networkx package輔助繪圖

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
* graph_1 <br />  
| 1   | 2   | 3   | 4   | 5   | 6   |
|-----|-----|-----|-----|-----|-----|
| 0.0 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
* graph_2 <br /> 
| 1   | 2   | 3   | 4   | 5   |
|-----|-----|-----|-----|-----|
| 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
* graph_3 <br /> 
| 1                 | 2                 | 3                 | 4                 |
|-------------------|-------------------|-------------------|-------------------|
| 0.190983005521049 | 0.309016994478951 | 0.309016994478951 | 0.190983005521049 |
* graph_4 <br /> 
| 1                  | 2                  | 3                   | 4                  | 5                   | 7                   | 6                   |
|--------------------|--------------------|---------------------|--------------------|---------------------|---------------------|---------------------|
| 0.1394838930854497 | 0.1779120314091907 | 0.20082320536937326 | 0.1401777533243232 | 0.20142536348733986 | 0.08408849143863972 | 0.05608926188568348 |
* graph_5 <br /> 

* graph_6 <br /> 

* graph_7 <br /> 

* graph_8 <br /> 

### HITS_Hub
* graph_1 <br />  

* graph_2 <br /> 

* graph_3 <br /> 

* graph_4 <br /> 

* graph_5 <br /> 

* graph_6 <br /> 

* graph_7 <br /> 

* graph_8 <br /> 

---
## Computation performance analysis 

---
## Discussion
### More limitations about link analysis algorithms 
### Can link analysis algorithms really find the “important” pages from Web? 
### What are practical issues when implement these algorithms in a real Web? 
    Performance discussion (time cost) 
### What do the result say for your actor/movie graph?  
### Any new idea about the link analysis algorithm? 
### What is the effect of “C” parameter in SimRank? 
### Design a new link-based similarity measurement 
