USER=$1
HOSTS=$2
CMDS=$3
IFS=$'\n'

function runCommandOnHost(){
	echo "Running \"${CMD}\" on ${HOST}"
	#This is login to AWS EC2 machine. Hence we are using pem file
  ssh -i /Users/raghunandanask/Desktop/PEM/newpem/<xyz.pem> ${USER}@${HOST} ${CMD}
}

for HOST in `cat ${HOSTS}`;
do
  for CMD in `cat ${CMDS}`;
  do
    runCommandOnHost ${USER} ${HOST} ${CMD}
  done
done
