import os
import census2010


print('Anchorage: %s' % census2010.allData['AK']['Anchorage'])

anchoragePop = census2010.allData['AK']['Anchorage']['pop']
print('The 2010 population of Anchorage was %s' % str(anchoragePop))
