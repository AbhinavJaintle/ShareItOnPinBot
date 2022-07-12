import tweepy
import logging
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

auth = tweepy.OAuthHandler("I62D3tAPbWhIyCbaMf9p0Vu9F", "bZp8J7ow718BzJsPjphdplDIbmvtctsZHXbtvrtgGegA3ndmHq")
auth.set_access_token("1526681083701362689-SN3YcRQH76Zr4AM17E0NO2KC3BiOIm", "YPOvaqYe2UBJDCBBlUZcKQvLBbGtIbYESxuSCYTUrINid")
api = tweepy.API(auth)

if api.verify_credentials() == False:
    print("The user credentials are invalid.")
else:
    print("The user credentials are valid.")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


path = "D:/Documents/codes/bot"

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    file_object = open('my_output.txt', 'a')

    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
    #  if api.mentions_timeline != 0:
        
        new_since_id = max(tweet.id, new_since_id)
        # if tweet.in_reply_to_status_id is not None:
        #     continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to {tweet.user.name}")
            
            logger.info(f"URL: {tweet.in_reply_to_status_id}")
            link = "https://twitter.com/jaintle/status/"
            link += str(tweet.in_reply_to_status_id)


            count = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><div id="tweet" style="width: 550px"><blockquote class="twitter-tweet"> <a href='
            count+=link
            count+='></a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></div></body></html>'

            files = open('embed.html', 'a')
            files.truncate(0)
            print(count,file=files)
        

            files.close()

            path = "file:///D:/Documents/codes/bot/embed.html"
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(path)
            sleep(5)

            filename = str(tweet.in_reply_to_status_id)
            filename+=".png"
            print(filename)
            while 1>0:
                try:
                    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'tweet')))
                    image = driver.find_element(By.ID,"tweet").screenshot_as_png
                    break
                except:
                    continue

            with open(filename, 'wb') as f:
                f.write(image)
            driver.quit()
            print("end...")

            
            if filename != "None.png":
                sharetweet = api.update_with_media("D:/Documents/codes/bot/"+filename, "Please click on the link in the immediate reply to this tweet to save this screenshot as a pin on any of your boards.\nConsider following the bot as a token for appreciation :)", in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)
                sharelink = "https://twitter.com/jaintle/status/"
                sharelink += str(sharetweet.id)
                api.update_status("http://pinterest.com/pin/create/button/?url="+sharelink,in_reply_to_status_id = sharetweet.id , auto_populate_reply_metadata=True)
            if filename == "None.png":
                api.update_status("Error! Please mention me only in replies to tweets you want screenshots of",in_reply_to_status_id = tweet.id , auto_populate_reply_metadata=True)


            # api.destroy_mentions_timeline(tweet.id)
        file_object.truncate(0)
        print(new_since_id,file=file_object)
    
    file_object.close()

    return new_since_id



def main():


    file_object = open('my_output.txt', 'r')

    file = file_object.readlines()

    for element in file:
        since_id = int(element)

    file_object.close()    

    while True:
        since_id = check_mentions(api, [""], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()