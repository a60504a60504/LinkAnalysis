# LinkAnalysis
---
## Implementation detail 
### IBMdata2graph.py
* 從project1的IBM資料產生兩筆有向圖(directed graph)
  * 其中一筆為在同一個transaction底下的items做單向(directed)連接e.g. 1 ---> 2 ---> 3 ---> 4
  * 另外一筆為在同一個transaction底下的items做雙向(bidirected)連接e.g. 1 <--> 2 <--> 3 <--> 4
### HITS_Pagerank.py
* 使用 networkx package輔助繪圖
* HITS 
  * 產生 authority與hub
* Pagerank 
  * 產生 pr
  * alpha = 0.15 代表 damping factor=0.15
### SimRank.py
* 使用 networkx package輔助繪圖
## Result analysis and discussion 

## Computation performance analysis 

## Discussion
