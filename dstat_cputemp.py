### Displays the CPU temperature
### Author: marcelo.veiga@gmail.com

class dstat_plugin(dstat):
    """
    CPU temperature in Celsius as reported by lm_sensors.
    """

    def __init__(self):
        self.name = 'temperature'
        self.type = 'f'
        self.width = 5
        self.scale = 20

    def check(self): 
        if not os.access('/usr/bin/sensors', os.R_OK):
            raise Exception, 'Cannot access lm_sensors.'

    def vars(self):
        ret = []
        n = 0
        ret.append("total")
        for line in os.popen('/usr/bin/sensors'):
            if len(line) < 2:
                continue
            fields = line.split()
            if fields[0] == "Core":
                cpu = "cpu" + str(n)
                ret.append(cpu)
                n = n + 1
        return ret

    def nick(self):
        return [name.lower() for name in self.vars]

    def extract(self):
        n = 0
        total = 0.0
        for line in os.popen('/usr/bin/sensors'):
            if len(line) < 2:
                continue
            fields = line.split()
            if fields[0] == "Core":
                temp = fields[2].replace('+','')
                temp = temp[:4]
                cpu = "cpu" + str(n)
                self.val[cpu] = float(temp)
                total = total + float(temp)
                n = n + 1
        total = total/n
        self.val["total"] = total

# vim:ts=4:sw=4:et
