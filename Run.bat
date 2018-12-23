@echo off
python IBMdata2graph.py
python HITS_Pagerank.py > HITS_Pagerank_Output.txt
python SimRank.py > SimRank_Output.txt
pause