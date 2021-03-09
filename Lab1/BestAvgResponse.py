import requests

sites = ('http://www.google.com', 'http://www.youtube.com')
times = []
avg = []

for url in sites:
    for req in range(10):
        r = requests.get(url)
        times.append(r.elapsed.microseconds/1000)

    avg.append(sum(times)/len(times))

best = min(avg)
ind = avg.index(min(avg))
print('Il sito con tempo di risposta migliore è: ', sites[ind])
