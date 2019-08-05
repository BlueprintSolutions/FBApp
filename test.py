import sys
sys.path.append('/c/users/aldwin galapon/appdata/local/programs/python/python36/lib/site-packages') # Replace this with the place you installed facebookads using pip
sys.path.append('/c/users/aldwin galapon/appdata/local/programs/python/python36/lib/site-packages/facebook_business_mirror-4.0.0.dist-info') # same as above

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

my_app_id = '525243791549096'
my_app_secret = '57bcb17d93cca10a5e600c0558aacfbf'
my_access_token = 'EAAHdtNmdoqgBAMSMaWgOZCKDihheWOeheEerUVvBE6wQpVxQSkNR6tXeEOpPYsxHyv0ZBFfP8uViCMzBOTp3vteOa187mZC2fPJ8iZBA831IEyP2X0EqrAh11Hokj0UUA3qmfvx77x4o1JlGpOlk1ka5wlWma8vDyRYxHzAWc357G58vHNn6LQBH88foZCGzvAa7yaVLLAaTZCHeGtOZCb4'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_565008260617668')
campaigns = my_account.get_campaigns()
print(campaigns)