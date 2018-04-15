cat cluster_output | grep ClusterId | cut -c 18- | sed -e 's/^"//' -e 's/"$//' > cluster_id

echo "" > /tmp/master_pool_ip
while read p; do
echo ""$p
aws emr  describe-cluster --cluster-id  j-3LX7XRP0HRHEJ | grep "MasterPublicDnsName" | cut -c 36- | sed 's/".*//' > /tmp/master_pool_ip
done < cluster_id
