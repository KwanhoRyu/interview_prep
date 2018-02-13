###############################
# Breadth First Search in Undirectied Graphs
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


from queue import Queue

class Vertex:
	def __init__ (self, id):
		self.id = id
		self.visited = False
		self.dist = None

class Edge:
	def __init__ (self, start_vertex_id, dest_vertex_id, weight = None):
		self.start_vertex_id = start_vertex_id
		self.dest_vertex_id = dest_vertex_id
		self.weight = weight
		
def bfs (source_vertex, vertices, edges):
	queue = Queue()
	queue.push(source_vertex)
	source_vertex.visited = True
	source_vertex.dist = 0

	while not queue.is_empty():
		vertex = queue.pop()
		print(vertex.id, vertex.dist)

		for dest_vertex in edges[vertex]:
			if dest_vertex.visited == False:
				queue.push(dest_vertex)
				dest_vertex.visited = True
				dest_vertex.dist = vertex.dist + 1


################################################################################################################
# test cases
################################################################################################################

def main():
	testcase_1()
	testcase_2()

def testcase_1():
	print("-- testcase 1 --")
	print("(id, dist)")

	vertex_ids = range(1, 6)
	vertices = build_vertices(vertex_ids)

	edges_list = [(1,2), (1,3), (3,4), (4,5)]
	edges = build_edges(vertices, edges_list)

	bfs(vertices[0], vertices, edges)

def testcase_2():
	print("-- testcase 2 --")
	print("(id, dist)")

	vertex_ids = range(0, 7)
	vertices = build_vertices(vertex_ids)
	
	edges_list = [ (0,1), (0,2), (1,3), (1,4), (2,5), (2,6) ]
	edges = build_edges(vertices, edges_list)

	bfs(vertices[0], vertices, edges)


def build_vertices(vertex_ids):
	vertices = []

	for vertex_id in vertex_ids:
		vertices.append(Vertex(vertex_id))

	return vertices

def build_edges(vertices, edges_list):
	edges = {}

	for start_vertex in vertices:
		edges[start_vertex] = []

	for start_vertex_id, dest_vertex_id in edges_list:
		for vertex in vertices:
			if vertex.id == start_vertex_id:
				start_vertex = vertex
			if vertex.id == dest_vertex_id:
				dest_vertex = vertex
		
		edges[start_vertex].append(dest_vertex)
		# bidirectional edges -> undirected graphs
		edges[dest_vertex].append(start_vertex)

	return edges 



if __name__ == "__main__":
	main()






