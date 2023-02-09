class Solution:
    def reformatDate(self, date: str) -> str:
        hash={"Jan":'01', "Feb":'02', "Mar":'03', "Apr":'04', 
            "May":'05', "Jun":'06', "Jul":'07', "Aug":'08',
             "Sep":'09', "Oct":'10', "Nov":'11', "Dec":'12'}
        a=date.split()
        # print(a)
        # print(a[0][:-2])#day
        # print(hash[a[1]])#month
        # print(a[-1])#year
        if len(a[0])==3:
            a[0]='0'+a[0]
        return a[-1]+"-"+hash[a[1]]+'-'+a[0][:-2]
