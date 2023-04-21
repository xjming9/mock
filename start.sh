BUILD_ID=dontKillMe
if [ -z $1 ]
then
	str=app.py
else
	str=$1
fi
echo "根据 $str 筛选进程"
pid=$(ps -ef |grep $str |awk '{print $2}')
arr=($pid)
for (( i=0;i<${#arr[@]};i++))
do
echo  "删除进程ID：${arr[$i]}"
kill -9 ${arr[$i]}
done

nohup python3 app.py>> nohup.out &