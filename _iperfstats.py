from multiprocessing import Process, Queue
import time
import psutil
from os import getpid

class iPerfStats:
    def __init__(self):
        self.cpupercent = [] #List - for each CPU
        self.vmem = [] #[Used mem, free mem] in %


class iPerfSysStats(iPerfStats):
    def __init__(self):
        iPerfStats.__init__(self)

class iPerfLocalStats(iPerfStats):
    def __init__(self):
        iPerfStats.__init__(self)

def collect_stats(ppid,childq,tts):
    p = psutil.Process(ppid)
    collector = StatsMan(p)
    while(1):
        stats = collector.get()
        childq.put(stats)
        time.sleep(tts)


class StatsMan():
    def __init__(self,p):
        self._pphdl = p

    def get(self):
        print "child: stats collection ongoing"
        sys_cpu_per = psutil.cpu_percent(interval=1,percpu=True)
 
        cput = psutil.cpu_times()
        total_time = sum(cput)
        sys_cpu_times = [(cput.user/total_time)*100,
                         (cput.system/total_time)*100,(cput.idle/total_time)*100]

        vm = psutil.virtual_memory()
        sys_vm_data = [vm.percent, 100.0-vm.percent]


        #Process specific collection
        pp_cpu_per = self._pphdl.cpu_percent(interval=1)

        pcput = self._pphdl.cpu_times()
        pp_cpu_times = [pcput.user,pcput.system]

        pp_vm_data = self._pphdl.memory_percent()
        
        csw = self._pphdl.num_ctx_switches()
        pp_ctx_switches = [csw.voluntary,csw.involuntary]

        return [sys_cpu_per,sys_cpu_times,sys_vm_data,pp_cpu_per,pp_cpu_times,pp_vm_data,pp_ctx_switches]

    #Since this class knows the data ordering..so it can format
    def format(self, raw_data):
        dict_data = {}
        dict_data["Sys_CPU%"] = []
        dict_data["Sys_user_time%"] = []
        dict_data["Sys_system_time%"] = []
        dict_data["Sys_idle_time%"] = []
        dict_data["Sys_used_VM%"] = []
        dict_data["Sys_available_VM%"] = []
        dict_data["Proc_CPU%"] = []
        dict_data["Proc_user_time_sec"] = []
        dict_data["Proc_system_time_sec"] = []
        dict_data["Proc_used_VM%"] = []
        dict_data["Proc_vol_ctx_switch"] = []
        dict_data["Proc_invol_ctx_switch"] = []
        for data in raw_data:
            dict_data["Sys_CPU%"].append(data[0])
            dict_data["Sys_user_time%"].append(data[1][0])
            dict_data["Sys_system_time%"].append(data[1][1])
            dict_data["Sys_idle_time%"].append(data[1][2])
            dict_data["Sys_used_VM%"].append(data[2][0])
            dict_data["Sys_available_VM%"].append(data[2][1])
            dict_data["Proc_CPU%"].append(data[3])
            dict_data["Proc_user_time_sec"].append(data[4][0])
            dict_data["Proc_system_time_sec"].append(data[4][1])
            dict_data["Proc_used_VM%"].append(data[5])
            dict_data["Proc_vol_ctx_switch"].append(data[6][0])
            dict_data["Proc_invol_ctx_switch"].append(data[6][1])

        return dict_data


#Open a new process and start stat collection periodically
#
class iPerfStatsTask:
    def __init__(self):
        #self._quit = False
        self._sleep = 2
        self._pid = getpid()
        self._q = Queue(10)
        self._p = Process(target=collect_stats, args=(self._pid,self._q,self._sleep))

    def start(self):
        self._p.start()
        print("started the new process")
        ##Temporarily added a sleep to allow atleast one data collection
        time.sleep(4)

    def stop(self):
        self._p.terminate()
        #self._quit = True
        tmp = []
        while not self._q.empty():
            tmp.append(self._q.get())
     
        #Pass this list to StatsMan object asking it to give back formatted dictionary object 
        stats = StatsMan(1).format(tmp)
        return stats
