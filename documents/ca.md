# Windows
(http://blog.csdn.net/zhaotengfei36520/article/details/41962077)
- 安装 openssl
    - 下载 http://slproweb.com/products/Win32OpenSSL.html
    - 下载上面相应版本的tar.gz http://www.openssl.org/
    - 解压tar.gz 并复制apps目录下的demoCA目录和openssl.cnf文件到安装的openssl的bin目录下（默认为C:\OpenSSL-Win64\bin\）
    - 在上面的bin目录下生成四个文件夹 ca, jks, server, client
        
- 生成证书
    - 生成CA证书
        - 创建私钥
            - openssl genrsa -out ca/ca-key.pem 1024
        - 创建证书请求
            - openssl req -new -out ca/ca-req.csr -key ca/ca-key.pem -config openssl.cnf
        - 自签署证书
            - openssl x509 -req -in ca/ca-req.csr -out ca/ca-cert.pem -signkey ca/ca-key.pem -days 3650
        - 将证书导出成浏览器支持的.p12格式
            - openssl pkcs12 -export -clcerts -in ca/ca-cert.pem -inkey ca/ca-key.pem -out ca/ca.p12
            - 密码 passca （自己设置）
    - 生成Server证书
        - 创建私钥
            - openssl genrsa -out server/server-key.pem 1024
        - 创建证书请求
            - openssl req -new -out server/server-req.csr -key server/server-key.pem -config openssl.cnf
            - common name这一项时一定要写服务器所在的IP地址，本机可以用localhost
        - 自签署证书
            - openssl x509 -req -days 365 -in server/server-req.csr -signkey server/server-key.pem -out server/server-cert.pem
            - (http://www.cnblogs.com/interdrp/p/4881116.html)
        - 将证书导出成浏览器支持的.p12格式
            - openssl pkcs12 -export -clcerts -in server/server-cert.pem -inkey server/server-key.pem -out server/server.p12
            - 密码 passca （自己设置）
    - 生成Client证书
        - 创建私钥
            - openssl genrsa -out client/client-key.pem 1024
        - 创建证书请求
            - openssl req -new -out client/client-req.csr -key client/client-key.pem -config openssl.cnf
        - 自签署证书
            - openssl x509 -req -days 365 -in client/client-req.csr -signkey client/client-key.pem -out client/client-cert.pem
        - 将证书导出成浏览器支持的.p12格式
            - openssl pkcs12 -export -clcerts -in client/client-cert.pem -inkey client/client-key.pem -out client/client_err.p12
            - 密码 passca （自己设置）
        - 生成客户端证书导出成浏览器支持的.p12格式（用于导入浏览器）
            - openssl pkcs12 -export -clcerts -in ca/ca-cert.pem -inkey ca/ca-key.pem -out client/client.p12
            - 密码 passca （自己设置）
    - 根据ca证书生成jks文件