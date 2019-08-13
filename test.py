import sys
sys.path.append('/c/users/aldwin galapon/appdata/local/programs/python/python36/lib/site-packages') # Replace this with the place you installed facebookads using pip
sys.path.append('/c/users/aldwin galapon/appdata/local/programs/python/python36/lib/site-packages/facebook_business_mirror-4.0.0.dist-info') # same as above

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

my_app_id = '474530250048926'
my_app_secret = '57bcb17d93cca10a5e600c0558aacfbf'
my_access_token = 'EAAHdtNmdoqgBAIi6OZBW7Un9M06s8PtAPAVNaxCoy9iU2DYAyZAC9SF2zSImfOl6r5Iqp3NTxtAc4Cux4EVzZBLEvCDSnW4k2ZByKKbS86fxs07Sf4tUKf5XvlixwS0rwe1iy8Lr9rWW5HwcztldnvXbyPZBjhLToWMlL6KDEP4IlTcedPHBeUv7OhCqH72IZD'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_565008260617668')
campaigns = my_account.get_campaigns()
print(campaigns)