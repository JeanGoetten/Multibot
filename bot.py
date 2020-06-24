import tweepy
import time
import json
import sys

auth = tweepy.OAuthHandler('hbO2yaNy5x2nyJvcXSJjlTSbz', 'yl27imA0x41yr1hf7XJLZKPZhit5ypVaZyPgmnZTpVGfYIu6XS')
auth.set_access_token('1272602932454789123-N3oU9ZBp1yzetakqw8CmMcMRIz7IRm', 'WhiCWzC0GWyCWNH0w0qXwRNlZtZjFWpVuIzIpnCLwTobY')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.me()

BRAZIL_WOE_ID = 23424768
nrTweets = 100
go_to_next = 0

def Range(start, end):
    x = range(start, end)
    for n in x:
        restart = n
    return restart

def searching():
    brazil_trends = api.trends_place(BRAZIL_WOE_ID)
    trends = json.loads(json.dumps(brazil_trends, indent=1))
    top_trend = trends[0]["trends"][go_to_next]
    top_trend_tag = top_trend["name"]
    start = time.time()
    elapsed = 0
    error = ''

    print('\n\n' + "searching for " + top_trend_tag + "...")

    count = 0
    for tweet in tweepy.Cursor(api.search, top_trend_tag).items(nrTweets):
        elapse = time.time()
        elapsed = elapse - start
        horas = int(elapsed/3600)
        minutos = int(elapsed/60)
        minutos = int(minutos%60)
        segundos = int(elapsed%60)
        final_time = (str(horas) + ":" + str(minutos) + ":" + str(segundos))

        try:
            tweet.favorite()
            count += 1
            print('\r' + final_time + " - Tweet liked: " + str(count))

            data = {'time': elapsed, 'tag': top_trend_tag, 'liked': count}
            with open('data/' + 'data_' + top_trend_tag + '.json', 'a') as f:
                json.dump(data, f)
                f.write('\n')
            time.sleep(Range(2, 23))
        except tweepy.TweepError as e:
            if(e.reason == error):
                pass
            else:
                error = e.reason
                with open('error/' + 'error_' + top_trend_tag + '.json', 'a') as f:
                    json.dump(error, f)
                    f.write('\n')

            sys.stdout.write('\r' + final_time)

while True:
    searching()
    time.sleep(Range(10, 60))
    go_to_next += 1
    if(go_to_next > 5):
        go_to_next = 0
