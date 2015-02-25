{"filter":false,"title":"acceleration.py","tooltip":"/acceleration.py","undoManager":{"mark":65,"position":65,"stack":[[{"group":"doc","deltas":[{"start":{"row":9,"column":1},"end":{"row":10,"column":1},"action":"insert","lines":["dist_list = np.zeros((N,N),dtype=float)","\t"]},{"start":{"row":20,"column":4},"end":{"row":21,"column":118},"action":"remove","lines":["if abs_distance < cutoff:","\t\t\t\t# F = (12*(np.power(sigma,12))/(np.power(total_distance,13)))-6*((np.power(sigma,6))/(np.power(total_distance,7)))"]},{"start":{"row":20,"column":4},"end":{"row":23,"column":29},"action":"insert","lines":["dist_list[ii,iii] = abs_distance","","","\t\t\t\tif abs_distance < cutoff:"]},{"start":{"row":35,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["\tdist_list = dist_list.flatten()\t\t\t\t\t\t\t\t\t\t# Change the 2d array to a 1d array","\tdist_list = dist_list[dist_list !=0]\t\t\t\t\t\t\t\t# remove zeroes from the 1d array","\tdist_hist = np.histogram(dist_list,100000)\t\t\t\t\t\t\t# create a histogram of the distances, with width delta r","\tprint len(dist_hist)",""]},{"start":{"row":39,"column":37},"end":{"row":39,"column":47},"action":"insert","lines":[",dist_hist"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"remove","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":11},"end":{"row":38,"column":20},"action":"remove","lines":["dist_hist"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"remove","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":7},"end":{"row":38,"column":8},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"insert","lines":["h"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":36},"end":{"row":37,"column":37},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":37},"end":{"row":37,"column":38},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":38},"end":{"row":37,"column":39},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":39},"end":{"row":37,"column":40},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":40},"end":{"row":37,"column":41},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":14},"end":{"row":37,"column":15},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"insert","lines":["d"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":17},"end":{"row":37,"column":18},"action":"insert","lines":["g"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":18},"end":{"row":37,"column":19},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":19},"end":{"row":37,"column":20},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":11},"end":{"row":37,"column":20},"action":"remove","lines":["bin_edges"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":56},"end":{"row":37,"column":57},"action":"remove","lines":["\t"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":55},"end":{"row":37,"column":56},"action":"remove","lines":["\t"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":57},"end":{"row":37,"column":63},"action":"remove","lines":["create"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":56},"end":{"row":37,"column":58},"action":"remove","lines":["  "]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":57},"end":{"row":37,"column":58},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":56},"end":{"row":37,"column":57},"action":"remove","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":56},"end":{"row":37,"column":57},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":70},"end":{"row":37,"column":73},"action":"remove","lines":["the"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":69},"end":{"row":37,"column":70},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":36},"end":{"row":21,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":9},"end":{"row":37,"column":10},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":10},"end":{"row":37,"column":11},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":1},"end":{"row":37,"column":3},"action":"insert","lines":["# "]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"remove","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":13},"end":{"row":37,"column":22},"action":"remove","lines":["dist_hist"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"remove","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":9},"end":{"row":37,"column":12},"action":"remove","lines":["len"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":8},"end":{"row":37,"column":9},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":3},"end":{"row":37,"column":4},"action":"remove","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":2},"end":{"row":37,"column":3},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":1},"end":{"row":37,"column":2},"action":"remove","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":0},"end":{"row":37,"column":1},"action":"remove","lines":["\t"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":99},"end":{"row":37,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":47},"end":{"row":36,"column":48},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":46},"end":{"row":36,"column":47},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":36,"column":45},"end":{"row":36,"column":46},"action":"remove","lines":["0"]}]}]]},"ace":{"folds":[],"scrolltop":393,"scrollleft":0,"selection":{"start":{"row":36,"column":96},"end":{"row":36,"column":96},"isBackwards":false},"options":{"tabSize":4,"useSoftTabs":true,"guessTabSize":false,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":81,"mode":"ace/mode/python"}},"timestamp":1424888390008,"hash":"8996076e6f6272c99f79ac3dc266a6523ecd96a7"}