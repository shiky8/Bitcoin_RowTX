import requests
TxId=raw_input("Enter the TXID : ")
print "the RowTx = "
RowTx=requests.get('https://blockchain.info/tx/'+TxId+'?format=hex').text
print RowTx
out=open('rowtx.txt', 'w')
out.write("RowTX = \n %s \n" % RowTx)

