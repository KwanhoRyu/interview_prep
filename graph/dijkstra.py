###############################
# Dijkstra in
# pros : 
# - 
# 
# cons:
# - 
#
# time complexity : O(|V|+|E|)
# space complexity : O(|V|+|E|)
###############################

import sys
sys.path.insert(0, '/Users/kwanhoryu/study/interview_prep/data_structures')

from min_heap import MinHeap


class Vertex:
	def __init__ (self, id):
		self.id = id
		self.parent = None
		self.dist = None

class Edge:
	def __init__ (self, start_vertex_id, dest_vertex_id, weight = None):
		self.start_vertex_id = start_vertex_id
		self.dest_vertex_id = dest_vertex_id
		self.weight = weight
		
def dijkstra (source_vertex, vertices, edges):

	minheap = MinHeap("dist")

	for vertex in vertices:
		vertex.parent = vertex
		vertex.dist = 999999
		minheap.push(vertex)

	minheap.update_key( minheap.find_index(vertices[0]), 0 )

	while not minheap.is_empty():
		vertex = minheap.pop()
		print(vertex.id, vertex.parent.id, vertex.dist)

		for dest_vertex, weight in edges[vertex]:
			if dest_vertex.dist > vertex.dist + weight:
				dest_vertex.parent = vertex
				minheap.update_key( minheap.find_index(dest_vertex), vertex.dist + weight )
				


################################################################################################################
# test cases
################################################################################################################

def main():
	testcase_1()
#	testcase_2()

def testcase_1():
	print("-- testcase 1 --")
	print("(id, parent, dist)")

	vertex_ids = range(1, 6)
	vertices = build_vertices(vertex_ids)

	# (vertex.id, dest_vertex.id, weight)
	edges_list = [ (1,2,4), (1,3,1), (1,4,2), (2,3,1), (2,5,1), (4,5,2) ]
	edges = build_edges(vertices, edges_list)

	dijkstra(vertices[0], vertices, edges)

def testcase_2():
	print("-- testcase 2 --")
	print("(id, parent, dist)")



def build_vertices(vertex_ids):
	vertices = []

	for vertex_id in vertex_ids:
		vertices.append(Vertex(vertex_id))

	return vertices

def build_edges(vertices, edges_list):
	edges = {}

	for start_vertex in vertices:
		edges[start_vertex] = []

	for start_vertex_id, dest_vertex_id, weight in edges_list:
		for vertex in vertices:
			if vertex.id == start_vertex_id:
				start_vertex = vertex
			if vertex.id == dest_vertex_id:
				dest_vertex = vertex
			
		edges[start_vertex].append( (dest_vertex,weight) )
		# bidirectional edges -> undirected graphs
		edges[dest_vertex].append( (start_vertex,weight) )

	return edges 



if __name__ == "__main__":
	main()






