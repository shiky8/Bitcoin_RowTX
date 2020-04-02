import requests
TxId=input("Enter the TxID : ")
print("the RoqTX = ")
RowTx=requests.get('https://blockchain.info/tx/'+TxId+'?format=hex').text
print (RowTx)
out=open('rowtx.txt', 'w')
out.write("RowTX = \n %s \n" % RowTx)
