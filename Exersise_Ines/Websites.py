class Website:
    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        self.queries = queries


data = input()
websites = []

while not data == 'end':
    domain = data.split(" | ")[1]
    host = data.split(" | ")[0]
    queries = None

    if len(data.split(" | ")) > 2:
        queries = data.split(" | ")[2].split(",")

    website = Website(host=host, domain=domain, queries=queries)

    websites.append(website)

    data = input()

for website in websites:
    if website.queries:
        website.queries = list(map(lambda x: "[" + x + "]", website.queries))
        print(f'https://www.{website.host}.{website.domain}/query?={"&".join(website.queries)}')
    else:
        print(f'https://www.{website.host}.{website.domain}')