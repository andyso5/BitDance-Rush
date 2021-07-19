# CPU Info

## 1 CPU base
#### 1.1 CPU物理个数
`$ cat /proc/cpuinfo |grep "physical id"| sort | uniq | wc -l`
`$ 1`
示例结果为1
#### 1.2 CPU逻辑个数
`$ cat /proc/cpuinfo | grep "processor" | wc -l`
`$ 8`
#### 1.3 CPU核数
也即CPU能处理数据的芯片组的个数
`$ cat /proc/cpuinfo | grep "cores" | wc -l`
`$ 8`
>> CPU逻辑个数 = SUM(物理CPU * CPU 核数 * 2/1 HT[超线程技术])
#### 1.4 CPU主频
`$ cat /proc/cpuinfo | grep MHz`
通常为了省电, 主频比较低, 当cpu负荷上升时, 会自动升频, 负荷较低时, 会降频, 已证实
详见[Linux系统下CPU频率的调整](https://blog.csdn.net/hddghhfd/article/details/83956197?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0&spm=1001.2101.3001.4242)
>> 是运算速度的一个重要影响因素

#### 1.5 操作系统内核信息
`$ uname -a`
`$ Linux xiaoao-HP 4.15.0-142-generic #146~16.04.1-Ubuntu SMP Tue Apr 13 09:27:15 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux`
#### 1.6 操作系统发型版本
`$ cat /etc/issue`
`Ubuntu 16.04.7 LTS \n \l`
#### 1.7 CPU当前运行的位数(32/64bits)
`$ getconf LONG_BIT`
#### 1.8 CPU是否支持64bit运算
`$ cat /proc/cpuinfo | grep flags | grep 'lm' | wc -l` 
>> 如果大于0表示可以


## 2 CPU concepts


## 3 CPU status
#### 3.1 CPU负载(load)
`$ uptime`
`$  22:38:24 up 2 days,  1:29,  1 user,  load average: 1.42, 1.42, 1.30`
load average 后三个数分别代表 1, 5, 15min可运行状态或不可中断状态(比如对磁盘的IO)的进程数, 经过测试, 一个进程数大约贡献0.01的load, 但是当进程很多的时候, 贡献值会飙升
其刷新间隔大概为5s
运行200个线程时, 1min内的load峰值为123
>> 需要注意的是, uptime的load并没有平摊到每个CPU核, 所以负载是否达到饱和(1), 还需除以核数

#### 3.2 进程的可运行状态

## Refference
1. [了解CPU的shell指令](https://blog.csdn.net/weixin_39795116/article/details/116846912)
2. [运维入门之CPU平均负载及问题排查](https://blog.csdn.net/u011294519/article/details/107293582/)
3. [物理cpu个数、逻辑cpu个数、核数](https://blog.csdn.net/haijiaoqihao20160106/article/details/53507839)
4. [CPU负荷](https://blog.csdn.net/m493096871/article/details/88862052)