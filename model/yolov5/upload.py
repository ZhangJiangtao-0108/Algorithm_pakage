import paramiko


def uploadfile(host, username, password, port, save_path, sever_path):

    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    
    sftp = paramiko.SFTPClient.from_transport(transport)#如果连接需要密钥，则要加上一个参数，hostkey="密钥"
    # print(save_path)
    save_path = save_path.replace("\\","/")
    sftp.put(save_path, sever_path)#将本地的Windows.txt文件上传至服务器/root/Windows.txt
    
    transport.close()#关闭连接