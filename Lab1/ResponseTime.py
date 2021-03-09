import requests
import matplotlib.pyplot as plt

m = 0
sites = ['http://www.google.com', 'http://www.merumusic.online', 'http://www.youtube.com', 'http://www.facebook.com', 'http://www.netflix.com']

for url in sites:
    print('Pinging URL: ', url)
    times = []

    for i in range(1000):
        r = requests.get(url)
        times.append(r.elapsed.microseconds / 1000)

    print('Minimo tempo di risposta: ', min(times))
    print('Massimo tempo di risposta: ', max(times))
    print('Tempo di risposta medio: ', sum(times) / len(times))
    m = max([m, max(times)])
    plt.plot(times, label=url)

print("\nPing massimo assoluto: ", m)

plt.xlabel('Request ID')
plt.ylabel('Response time (ms)')
plt.title('Site response time')
plt.ylim([0, 1.1 * m])
plt.legend(loc='upper right', fontsize=10)
plt.show()
