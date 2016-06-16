#   For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

events {
    worker_connections 1024;
}

http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
    	listen      80;
    	server_name epsilon.nordlinglab.org;

    	location = /favicon.ico { access_log off; log_not_found off; }
    	location /static/ {
		root /home/chinweze/info_retriv_sys;
    	}
	location /statistics {
		 autoindex on;
                 root /home/yslin;
		 index index.html;		
        }
	location /search_bar {
                 root /home/chinweze;
                 index  index.html;
        }
        location / {
		proxy_set_header Host $http_host;
	       	proxy_set_header X-Real-IP $remote_addr;
        	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        	proxy_set_header X-Forwarded-Proto $scheme;
                proxy_pass http://unix:/home/chinweze/info_retriv_sys/info_retriv_sys.sock;
       	}
    }

    server {
        listen       80 default_server;
        listen       [::]:80 ipv6only=on default_server;
        server_name  _;		# This is just an invalid value which will never trigger on a real hostname.
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
	    disable_symlinks off;
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
}
