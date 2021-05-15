import unittest

def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs,deps)
    return getOrderedJobs(jobGraph)


def createJobGraph(jobs,deps):
    graph = JobGraph(jobs)
    for job, dep in deps:
        graph.addDep(job,dep)
    return graph

def getOrderedJobs(jobGraph):
    orderedJobs = []
    nodesWithNoPrereq = list(filter(lambda node: node.numOfPrereq == 0, jobGraph.nodes))
    while len(nodesWithNoPrereq):
        node = nodesWithNoPrereq.pop()
        orderedJobs.append(node.job)
        removeDeps(node,nodesWithNoPrereq)
    graphHasEdges = any(node.numOfPrereq for node in jobGraph.nodes)
    return [] if graphHasEdges else orderedJobs

def removeDeps(node,nodesWithNoPrereq):
    while len(node.deps):
        dep = node.deps.pop()
        dep.numOfPrereq -= 1
        if dep.numOfPrereq == 0:
            nodesWithNoPrereq.append(dep)
			
	

class JobGraph:
	def __init__(self,jobs):
		self.nodes = []
		self.graph = {}
		for job in jobs:
			self.addNode(job)
			
	def addDep(self,job,dep):
		jobNode = self.getNode(job)
		depNode = self.getNode(dep)
		jobNode.deps.append(depNode)
		depNode.numOfPrereq +=1
		
			
	def addNode(self,job):
		self.graph[job] = JobNode(job)
		self.nodes.append(self.graph[job])
		
	def getNode(self, job):
		if job not in self.graph:
			self.addNode(job)
		return self.graph[job]
		
class JobNode:
	def __init__(self,job):
		self.job = job
		self.deps = []
		self.numOfPrereq = 0
		




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        jobs = [1, 2, 3, 4]
        deps = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
        order = topologicalSort(jobs, deps)
        self.assertEqual(isValidTopologicalOrder(order, jobs, deps), True)


def isValidTopologicalOrder(order, jobs, deps):
    visited = {}
    for candidate in order:
        for prereq, job in deps:
            if candidate == prereq and job in visited:
                return False
        visited[candidate] = True
    for job in jobs:
        if job not in visited:
            return False
    return len(order) == len(jobs)


if __name__ == "__main__":
    unittest.main()