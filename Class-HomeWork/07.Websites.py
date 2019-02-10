class Websites:
    def __init__(self, host, domain, queries):
        self.__hsot = self.set_host(host)
        self.__domain = self.set_domain(domain)
        self.__queries = self.set_queries(queries)

    def set_host(self, host):
        if isinstance(host, str):
            return host

    def get_host(self):
        return self.__hsot

    def set_domain(self, domain):
        if isinstance(domain, str):
            return domain

    def get_domain(self):
        return self.__domain

    def set_queries(self, queries):
        if isinstance(queries, list):
            return queries

    def get_queries(self):
        return self.__queries

    def __str__(self):
        if len(self.get_queries()) == 0:
            return f'https://www.{self.get_host()}.{self.get_domain()}'
        else:
            return f'https://www.{self.get_host()}.{self.get_domain()}/query?={"&".join(["["+x+"]" for x in self.get_queries()])}'


data = input()
wed_list=[]
while data != "end":
    data_lst = data.split(' | ')
    host_i = data_lst[0]
    domain_i = data_lst[1]
    if len(data_lst) >= 3:
        queries_i = data_lst[2:][0].split(',')
    else:
        queries_i = []
    web = Websites(host_i, domain_i, queries_i)
    wed_list.append(web)
    data = input()

for x in wed_list:
    print(x)
