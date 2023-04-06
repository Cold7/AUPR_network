import multiprocessing as mp
import networkx as nx
import argparse
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import auc

if __name__ == "__main__":
	#arguments of the script
	parser = argparse.ArgumentParser("Script to compute the Area Under Precision-Recall curve based in a reference and a inferred network.\n")
	parser.add_argument("-r", "--reference", help="Route to the reference network (GML format)", required=True)
	parser.add_argument("-i", "--inferred", help="Route to the inferred network (GML format and a edge attribute called score)", required=True)
	parser.add_argument("-o","--output", help="Output path to save results", default = "./output.log")
	args = parser.parse_args()

	print("Reading reference...")
	ref = nx.read_gml(args.reference)
	print("Reading inferred...")
	inf = nx.read_gml(args.inferred)
	#getting shared TFs in both nets
	print("getting TFs from reference net...")
	TFs_ref = [node for node in ref.nodes if ref.out_degree(node) > 0]
	print("getting TFs from inferred net...")
	TFs_inf = [node for node in inf.nodes if inf.out_degree(node) > 0]
	print("getting shared TFs...")
	shared_tfs = []
	for node in TFs_ref:
		if node in TFs_inf:
			shared_tfs.append(node)
	#getting shared nodes in both nets
	print("getting shared nodes in both edges...")
	shared = []
	for n1 in ref.nodes:
		if n1 in inf.nodes:
			shared.append(n1)
	real = []
	pred = []
	for n1 in shared_tfs:
		for n2 in shared:
			if inf.has_edge(n1,n2):
				pred.append(float(inf[n1][n2]["score"]))
				if ref.has_edge(n1,n2):
					real.append(1)
				else:
					real.append(0)
	print("Computing PR...")
	precision, recall, thresholds = precision_recall_curve(real, pred)
	print("Computing AUPR...")
	auc_ = auc(recall, precision)
	print("Writting...")
	out = open(args.output,"w")
	out.write("Reference: "+args.reference+"\n")
	out.write("Input: "+args.inferred+"\n")
	out.write("AUPR: "+str(auc_)+"\n")
	out.write("Thresholds:\n")
	out.write(str([x for x in thresholds])[1:-1]+"\n")
	out.write("Recall:\n")
	out.write(str([x for x in recall])[1:-1]+"\n")
	out.write("Precision:\n")
	out.write(str([x for x in precision])[1:-1]+"\n")
	out.close()
	print("Done")
