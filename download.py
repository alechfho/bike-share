import sched, time, datetime, requests

s = sched.scheduler(time.time, time.sleep)
url = "https://toronto-us.publicbikesystem.net/ube/gbfs/v1/en/station_status"


def download_data(dc):
    now = datetime.datetime.now()
    file_name = "{0}.json".format(now.isoformat())
    with open(file_name, "w") as f:
        r = requests.get(url)
        f.write(r.text)
    print("Download {0}".format(file_name))
    s.enter(900, 1, download_data, (dc,))


s.enter(1, 1, download_data, (s,))
s.run()
