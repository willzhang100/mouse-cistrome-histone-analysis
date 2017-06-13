import statistics, collections


''' This class represents a summary value object '''
class SummaryValue:
    def __init__(self, value):
        self.bag = set()
        self.bag.add(value)
        self.mean = None
        self.stdev = None
        self.update()

    def get_mean(self):
        return self.mean

    def get_stdev(self):
        return self.stdev

    def update(self):
        self.mean = statistics.mean(self.bag)
        if len(self.bag) > 1:
            self.stdev = statistics.stdev(self.bag)

    def add(self, value):
        self.bag.add(value)
        self.update()


histone_mark_set = collections.OrderedDict()

with open("Cistrome-IDs.txt") as f:
    data = f.readline().strip().split(sep='\t')
    print(data[6], data[7])
    histone_mark_data = str(data[6])
    filename = "histone_mouse/" + str(data[7])
    with open(filename) as f1:
        for line1 in f1:
            data1 = line1.strip().split(sep='\t')
            m_log_fdr = float(data1[8])
            print(m_log_fdr)
            if histone_mark_data not in histone_mark_set:
                histone_mark_set[histone_mark_data] = SummaryValue(m_log_fdr)
            else:
                histone_mark_set[histone_mark_data].add(m_log_fdr)

'''
with open("Cistrome-IDs.txt") as f:
    for line in f:
        data = line.strip().split(sep='\t')
        histone_mark_data = str(data[6])
        filename = "histone_mouse/" + str(data[7])
        print(histone_mark_data, filename)
        with open(filename) as f1:
            for line1 in f1:
                data1 = line1.strip().split(sep="\t")
                m_log_fdr = float(data1[8]) 
                if histone_mark_data not in histone_mark_set:
                    histone_mark_set[histone_mark_data] = SummaryValue(m_log_fdr)
                else:
                    histone_mark_set[histone_mark_data].add(m_log_fdr)
'''

print("Finished processing cistrome file.")

with open("summary-fdr.txt", 'w') as output:
    for histone in histone_mark_set:
        print(histone, histone_mark_set[histone].get_mean(),
              histone_mark_set[histone].get_stdev())
        output.write("{};{};{}\n".format(histone,
                                         histone_mark_set[histone].get_mean(),
                                         histone_mark_set[histone].get_stdev()))

