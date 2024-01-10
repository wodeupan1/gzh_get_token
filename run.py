import requests
import datetime

sess = requests.session()
sess.verify = False

# 获取公网IP
def getMyIp():
        try:
            get_url_1 = sess.get('http://httpbin.org/ip')
            return get_url_1.json()['origin']
        except requests.HTTPError as e:
            senderror(e)
        except:
            get_url_2 = sess.get('http://ip.42.pl/short')
            return get_url_2

# 将结果写入日志文件
def write_to_log(ip_address):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"{current_time} - IP地址： {ip_address}\n"
    with open("ip.log", "a") as log_file:
        log_file.write(log_content)

if __name__ == "__main__":
    ip_address = getMyIp()
    write_to_log(ip_address)
