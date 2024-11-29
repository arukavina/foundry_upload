import requests
import certifi
# response = requests.get('https://alixpartners.palantirfoundry.com/io/s3/ri.foundry.main.dataset.d2a0bda7-1751-47b4-b275-217aee0a8c22/PDI-301%20-%20Jan23-Dec23v2.rpt?uploads', verify=certifi.where())
# print(response.text)
#
#
import requests
import warnings
# 1.
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 2.
warnings.simplefilter('ignore', InsecureRequestWarning)
# 3.
response = requests.get('https://example.com', verify=False)
# 4.
print(response.text)
