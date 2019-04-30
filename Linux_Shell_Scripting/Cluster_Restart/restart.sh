#This section of code is looking for a input . We need the input on which cluster we would wish to restart.
# If there is no input then it will exit
if [ $# -eq 0 ]
  then
    echo "No arguments supplied. We need the Presto Cluster name in small caps"
    exit 1
fi

# Once we have a input what are doing a grep on a complete file to see if we have a entry and we are taking in the second field in here.
HOSTNAME=`grep $1 ip|cut -d= -f2`
echo ${HOSTNAME}

function runCommandOnHost(){
	echo "Running Restart on $1"
  ssh -i /Users/raghunandanask/Desktop/PEM/newpem/xyz.pem ec2-user@${HOSTNAME} /home/ec2-user/prestoadmin/presto-restart.sh
}

runCommandOnHost ${HOSTNAME} ${CMD}
