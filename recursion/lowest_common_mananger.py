# we are given an org chart in form if tree input.
# return the lowest common manger for 2 given groups
# O(n) time | O(d) space
def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager


def getOrgInfo(manager, reportOne, reportTwo):
	numImportantReports = 0
	for directReport in manager.directReports:
		orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
		if orgInfo.lowestCommonManager is not None:
			return orgInfo
		numImportantReports += orgInfo.numImportantReports
	if manager == reportOne or manager == reportTwo:
		numImportantReports += 1
	lowestCommonManager = manager if numImportantReports == 2 else None
	return OrgInfo(lowestCommonManager, numImportantReports)
		
class OrgInfo:
	def __init__(self, lowestCommonManager, numImportantReports):
		self.numImportantReports = numImportantReports
		self.lowestCommonManager = lowestCommonManager


'''
topManager "A"
reportOne "E"
reportTwo "I"

orgChart
An OrgChart is represented by a list of nodes. Every node has to have a unique 
string id that will be referenced by other nodes' lists of directReports and by 
the topManager, the reportOne, and the reportTwo.


{
  "nodes": [
    {"directReports": ["B", "C"], "id": "A", "name": "A"},
    {"directReports": ["D", "E"], "id": "B", "name": "B"},
    {"directReports": ["F", "G"], "id": "C", "name": "C"},
    {"directReports": ["H", "I"], "id": "D", "name": "D"},
    {"directReports": [], "id": "E", "name": "E"},
    {"directReports": [], "id": "F", "name": "F"},
    {"directReports": [], "id": "G", "name": "G"},
    {"directReports": [], "id": "H", "name": "H"},
    {"directReports": [], "id": "I", "name": "I"}
  ]
}
'''