def airportConnections(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableNotes(airportGraph, airports, startingAirport)
    markUnreachableConnections(airportGraph,unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph,unreachableAirportNodes)

def createAirportGraph(airports, routes):
    airportGraph = {}
    for airport in airports:
        airportGraph[airport] = AirportNode(airport)
    for route in routes:
        airport, connection = route
        airportGraph[airport].connections.append(connection)

    return airportGraph

def getUnreachableNotes(airportGraph, airports, startingAirport):
    visitedAirports ={}
    depthFirstTraverseAirports(airportGraph, startingAirport,visitedAirports)

    unreachableNodes = []
    for airport in airports:
        if airport in visitedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isReachable = False
        unreachableNodes.append(airportNode)
    return unreachableNodes

def depthFirstTraverseAirports(airportGraph, airport,visitedAirports):
	
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstTraverseAirports(airportGraph, connection,visitedAirports)

def markUnreachableConnections(airportGraph,unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableConnections = []
        depthFirstAddUnreachangeConnections(airportGraph, airport,unreachableConnections, {})
        airportNode.unreachableConnections = unreachableConnections

		
def depthFirstAddUnreachangeConnections(airportGraph, airport,unreachableConnections, visitedAirports):
    if airportGraph[airport].isReachable:
        return
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    unreachableConnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        depthFirstAddUnreachangeConnections(airportGraph, connection,unreachableConnections, visitedAirports)
		

def getMinNumberOfNewConnections(airportGraph,unreachableAirportNodes):
	unreachableAirportNodes.sort(key=lambda airport: len(airport.unreachableConnections),reverse=True)
	
	numberOfNewConnections = 0
	for airportNode in unreachableAirportNodes:
		if airportNode.isReachable:
			continue
		numberOfNewConnections += 1
		
		for connection in airportNode.unreachableConnections:
			airportGraph[connection].isReachable = True
	return numberOfNewConnections


class AirportNode:
	def __init__(self, airport):
		self.airport = airport
		self.connections =[]
		self.isReachable = True
		self.unreachableConnections = []


import unittest


AIRPORTS = [
    "BGI",
    "CDG",
    "DEL",
    "DOH",
    "DSM",
    "EWR",
    "EYW",
    "HND",
    "ICN",
    "JFK",
    "LGA",
    "LHR",
    "ORD",
    "SAN",
    "SFO",
    "SIN",
    "TLV",
    "BUD",
]

STARTING_AIRPORT = "LGA"


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        routes = [
            ["DSM", "ORD"],
            ["ORD", "BGI"],
            ["BGI", "LGA"],
            ["SIN", "CDG"],
            ["CDG", "SIN"],
            ["CDG", "BUD"],
            ["DEL", "DOH"],
            ["DEL", "CDG"],
            ["TLV", "DEL"],
            ["EWR", "HND"],
            ["HND", "ICN"],
            ["HND", "JFK"],
            ["ICN", "JFK"],
            ["JFK", "LGA"],
            ["EYW", "LHR"],
            ["LHR", "SFO"],
            ["SFO", "SAN"],
            ["SFO", "DSM"],
            ["SAN", "EYW"],
        ]
        self.assertTrue(airportConnections(AIRPORTS, routes, STARTING_AIRPORT) == 3)

if __name__ == "__main__":
    unittest.main()
