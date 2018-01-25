#-*- coding:utf-8 -*-  
#2105-03-18  
#定义扫描的端口  
Port = [ 80,21,23,22,25,110,443,1080,3306,3389,1521,1433]  
#定义端口对应的服务  
Server = ['HTTP','FTP','TELNET','SSH','SMTP','POP3','HTTPS','SOCKS','MYSQL','Misrosoft RDP','Oracle','Sql Server']  
import socket   
import sys  
  
#获取目标站点的IP地址  
def get_remote_machine_info(Domain):  
    try:  
        return socket.gethostbyname(Domain)  
    except socket.error,e:  
        print '%s: %s'%(Domain,e)  
        return 0  
  
#进行扫描  
def scan(Domain):  
    IP = get_remote_machine_info(Domain)  
    if IP:  
        result = []  
        for port,server in zip(Port,Server):  
            temp = []  
            try:  
                s = socket.socket()  
                print "Attempting to connect to "+Domain+': '+str(port)  
                s.connect((Domain,port))  
                #print 'Port '+str(port)+' open:\n'  
                temp.append(port)  
                temp.append(server)  
                result.append(temp)  
                s.close()  
            except:pass  
        if result:  
            print '\n'+Domain+': --> '+IP  
            print '\nThe Open Port:'  
            for i in result:  
                print Domain+': %4d -->%s'%(i[0],i[1])  
          
def main():  
    print '''''\nX-man Port Scan 1.0 
playload:./Scan.py www.xxx.zzz'''  
    payload = sys.argv  
    print '\n'  
    scan(payload[1])  
  
if __name__=='__main__':  
    main()
