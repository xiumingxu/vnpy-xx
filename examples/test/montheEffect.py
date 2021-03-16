# import sys
# import pandas as pd
# import numpy as np
#
# # import zwSys as zw  #::zwQT
# # import zwTools
#
#
#
# def zw_anz_m1sub(xcod,rss,kstr):
#      fss=rss+xcod+".csv";print(fss)
#      nSum=0;nAdd=0;nDec=0;
#      knum=int(kstr);knum2=knum+1;
#      try:
#          df = pd.read_csv(fss,index_col=0,parse_dates=[0],encoding= 'gbk')
#          df =df.rename(columns={'Close':'close'});df =df.sort_index()
#          #
#          _tim0=df.index[0];_ynum0=_tim0.year
#          _tim9=df.index[-1];_ynum9=_tim9.year+1;
#          for ynum in range(_ynum0,_ynum9):
#              ystr=str(ynum);_tim1x='-1';
#              ystr2=ystr+"-"+kstr
#              #print(ystr2,len(df),knum)
#              if knum==12:
#                  ystr3=ystr+"-"+kstr+'-31';
#                  df2=df[(df.index>=ystr2)&(df.index<=ystr3)];
#              else:
#                  kstr2=str(knum2);
#                  if knum2<10:kstr2='0'+kstr2;
#                  ystr3=ystr+"-"+kstr2+'-01';
#                  df2=df[(df.index>=ystr2)&(df.index<ystr3)];
#              #print(ystr2,ystr3,len(df2))
#              if (len(df2)>0):
#                  _tim1x=str(df2.index[0].month);
#                  if (len(_tim1x)<2):_tim1x='0'+_tim1x;
#              if (_tim1x==kstr):
#                  df1=df2[ystr2];
#                  if (len(df1)>0):
#                      xd1a=df1.ix[0];xd1z=df1.ix[-1];nSum+=1;
#                      vd1a=xd1a['close'];vd1z=xd1z['close'];
#                      if (vd1z>vd1a):nAdd+=1
#                      else:nDec+=1;
#
#      except IOError:
#          pass;    #skip,error
#
#      #print('nSum,nAdd,nDec,',nSum,nAdd,nDec);
#      return nSum,nAdd,nDec
# “def zw_stk_anz_m01(qx,finx0,rss,ksgn):
#      fss = qx.rdatInx+finx0+".csv";   #stk_code.csv,inxYahoo.csv
#      dinx = pd.read_csv(fss,encoding='gbk')
#
#      mx1={};mx1['finx']=finx0;mx1['ksgn']=ksgn;
#      mx1['nSum']=0;mx1['nAdd']=0;mx1['nDec']=0;
#      #nSum=0;nAdd=0;nDec=0;
#      i=0;xn9=len(dinx['code']);mx1['nstk']=xn9;
#      for xcod in dinx['code']:
#          i+=1;
#          if (not isinstance(xcod,str)):xcod="%06d" %xcod;
#
#          dSum,dAdd,dDec=zw_anz_m1sub(xcod,rss,ksgn);
#
#          mx1['nSum']=mx1['nSum']+dSum;
#          mx1['nAdd']=mx1['nAdd']+dAdd;
#          mx1['nDec']=mx1['nDec']+dDec;
#          print(i,'/',xn9,mx1);
#
#      mx1['kAdd']=np.round(mx1['nAdd']*100/ mx1['nSum']);
#      mx1['kDec']=np.round(mx1['nDec']*100/ mx1['nSum']);
#
#      return mx1
#
# def zw_stk_anz_mx(qx,finx0,rss):
#      c10=["finx","ksgn","nstk",'nSum','nAdd','nDec','kAdd','kDec'];
#      df=pd.DataFrame(columns=c10);
#      ftg="tmp\\mx_"+finx0+".csv";print(ftg)
#
#      for i in range(12):
#          ksgn=str(i+1);
#          if i<9:ksgn='0'+ksgn;
#          #print(ksgn)
#          mx1=zw_stk_anz_m01(qx,finx0,rss,ksgn);
# “
#          ds1=pd.Series(mx1,index=c10);
#          ds2=ds1.T;
#          df=df.append(ds2,ignore_index=True);
#          df.to_csv(ftg,index=False,encode='utf8');
#
# def zw_stk_anz_mx_all(qx,xlst):
#      for fx in xlst:
#          if (fx.find('Yah')>0):
#              rss=qx.rZWusDay
#          else:
#              if (fx=='inx_code'):rss=qx.rZWcnXDay
#              else:rss=qx.rZWcnDay
#
#          finx0=fx;
#          zw_stk_anz_mx(qx,finx0,rss);
#
#
# qx=zw.zwDatX(zw._rdatCN);
#
# uslst=['inxYahoo30sp','inxYahoo100ns','inxYahoo100sp','inxYahoo600','inxYahoo500sp','inxYahoo']
# zw_stk_anz_mx_all(qx,uslst)
#
# cnlst=['inx_code','stk_sz50','stk_hs300','stk_zz500','stk_code','stk_code'];
# zw_stk_anz_mx_all(qx,cnlst)
#
#
#
#
#
