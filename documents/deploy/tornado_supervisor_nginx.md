# tornado
- 启动
    
        /python/path/python   /project/path/main.py
# supervisor
- 添加tornado的配置文件放到supervisor的conf.d文件夹中

        [program:ohho]
        user=www
        command=/python/path/python /project/path/main.py
        process_name=%(program_name)s ; process_name expr (default %(program_name)s)
        numprocs=1                    ; number of processes copies to start (def 1)
        startretries=2                ;
        stopsignal=TERM               ; signal used to kill process (default TERM)
        redirect_stderr=true          ; redirect proc stderr to stdout (default false)
        directory=/project/path/
        autostart=true
        stdout_logfile = /log/path/ohho.out
        stdout_logfile_maxbytes=100MB
        stdout_logfile_backups=10
        stderr_logfile = /log/path/ohho.err
        stderr_logfile_maxbytes=100MB
        stderr_logfile_backups=10
- 启动服务

        supervisorctl -c /etc/supervisor/supervisor.conf
        start ohho
# nginx
- 添加nginx配置
        
        upstream frontends {
            server 服务器域名或IP:tornado启动的端口; 
        }
        server {
            listen 80;  #监听端口
            location / {
                proxy_read_timeout 1800;
                proxy_pass_header Server;
                proxy_set_header Host $http_host;
                proxy_redirect off;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Scheme $scheme;
                proxy_pass http://frontends;
            }
        }
