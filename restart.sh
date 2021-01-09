if [ "$(uname)" == "Darwin" ]; then
    pstree | grep gunicorn | grep -v grep | awk 'NR>1{system("kill -HUP "$2)}'
    # 或者
    # pstree | grep gunicorn | grep -v grep | sed '1d' | awk '{system("kill -HUP "$2)}'
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    ps aux | grep gunicorn | grep -v grep | awk 'NR>1{system("kill -HUP "$2)}'
    # 或者
    # ps aux | grep gunicorn | grep -v grep | sed '1d' | awk '{system("kill -HUP "$2)}'
fi