import socket
import datetime

# 获取当前IP地址
def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# 将结果写入日志文件
def write_to_log(ip_address):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_content = f"{current_time} - IP地址： {ip_address}\n"
    with open("ip.log", "a") as log_file:
        log_file.write(log_content)

if __name__ == "__main__":
    ip_address = get_ip_address()
    write_to_log(ip_address)
