#Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
#the amount exceeds $1000, or;
#if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans=set()
        transactionmap=collections.defaultdict(list)
        for transaction in transactions:
            name,time,amount,city = transaction.split(',')
            if int(amount)>1000:
                ans.add(transaction)
            transactionmap[name].append((time,amount,city))
        for name in transactionmap:
            n = transactionmap[name]
            d = len(n)
            for i in range(d):
                for j in range(i+1,d):
                    if abs(int(n[i][0])-int(n[j][0]))<=60 and n[i][-1]!=n[j][-1]:
                        ans.add( name+','+",".join(n[i]) )
                        ans.add( name+','+",".join(n[j]) )
        return list(ans)