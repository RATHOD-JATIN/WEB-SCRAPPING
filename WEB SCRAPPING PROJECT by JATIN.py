# WEB SCRAPPING PROJECT
# Name = RATHOD JATIN DINESHBHAI

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
AGE = []
NAME = []
OVA = []
POT = []
TEAM_NAME = []
CONTRACT = []
VALUE = []
WAGE = []
TOTAL_STATS = []
a = [0,60,120,180,240,300,360,420,480,540]
for i in a:
  url= f'https://sofifa.com/players?offset={i}'
  resp=requests.get(url)
  soup=BeautifulSoup(resp.content,'lxml')

  for nameofplayer in soup.findAll('tr'):
    NOP = re.sub(
            '\↘|<div class="popover-arrow">|<div c.*s\">|(Jan)|(Feb)|(Mar)|(Apr)|(May)|(Jul)|(Aug)|(Sep)|(Oct)|(Nov)|(Dec)|(Jun)|★|\,|<d.*r\">|On Loan|</span>|<a c.*[0-9]/">|<t.*>|<i.*>|\~|\↗|\→|<a h.*>|</div></a>|</figure>|</div>|</td>|<fig.*>|<sp.*s">|[0-9]{1,2}|[0-9]{4}|\~[0-9]{4}|\s|<div class="b.*t\">|<div c.*br>|<abb.*>|<span c.*>',
            '', str(nameofplayer))
    NAME.append(NOP)    #NAME


  for t in soup.find_all('td'):
   ageop=re.sub('\n|\s|<t.*>[^0-9]{2}.*|€[0-9]{1,3}[MK]|€[0-9]{1,3}\.[0-9][MK]|[0-9]{4} \~ [0-9]{4}|</f.*|[0-9]{2}</span>|<td class="col-name">|</td>|</div>|<i.*>|<t.*[^ae]">|<a.*>|<d.*>|<f.*>|<s.*>|\n','',str(t))
   ageofplayer=re.sub('€[0-9]{1,3}|<t.*>|\n','',str(ageop))
   AGE.append(ageofplayer)    #AGE


   perf = re.sub(
       '[0-9]{4} \~ [0-9]{4}|<a.*>|</f.*>|</div>|</td>|<t.*"">|<t.*me">|<t.*[vlwg]">\€[0-9]{1,3}[MK]|<i.*>|<f.*>|<d.*>|<t.*"ae">\d+</td>|<t.*"pt"><span class="bp.*</span></td>',
       '', str(t))
   perfo = re.sub(
       '<span class="bp3-t.*n|\.[0-9]M|<t.*[vlwg]">\€[0-9]{1,3}|<t.*[vlwg]">\€[0-9]{1,4}\.[0-9]{1,2}[MK]|<t.*oa"><s.*\d+">|</span>|<t.*r">|<td class="col col-tt" data-col="tt"><span class="bp3-tag p">[0-9]{1,4}',
       '', str(perf))
   performance = re.sub(
       '\>|Free|\n|Dec [0-9]{1,2}, [0-9]{4}|Nov [0-9]{1,2}, [0-9]{4}|Oct [0-9]{1,2}, [0-9]{4}|Sep [0-9]{1,2}, [0-9]{4}|Aug [0-9]{1,2}, [0-9]{4}|Jul [0-9]{1,2}, [0-9]{4}|Jan [0-9]{1,2}, [0-9]{4}|Feb [0-9]{1,2}, [0-9]{4}|Mar [0-9]{1,2}, [0-9]{4}|Apr [0-9]{1,2}, [0-9]{4}|May [0-9]{1,2}, [0-9]{4}|Jun [0-9]{1,2}, [0-9]{4}',
       '', str(perfo))
   OVA.append(performance)    #PERFORMANCE


   pote = re.sub(
       '[0-9]{4} \~ [0-9]{4}|<a.*>|</f.*>|</div>|</td>|<t.*"">|<t.*me">|<t.*[vlwg]">\€[0-9]{1,3}[MK]|<i.*>|<f.*>|<d.*>|<t.*"ae">\d+</td>|<t.*"oa"><span class="bp.*</span></td>',
       '', str(t))
   poten = re.sub(
       '<span class="bp3-t.*n|\.[0-9]M|<t.*[vlwg]">\€[0-9]{1,3}|<t.*[vlwg]">\€[0-9]{1,4}\.[0-9]{1,2}[MK]|<t.*pt"><s.*\d+">|</span>|<t.*r">|<td class="col col-tt" data-col="tt"><span class="bp3-tag p">[0-9]{1,4}',
       '', str(pote))
   potent = re.sub(
       '\n|Dec [0-9]{2}, [0-9]{4}|Nov [0-9]{2}, [0-9]{4}|Oct [0-9]{2}, [0-9]{4}|Sep [0-9]{2}, [0-9]{4}|Aug [0-9]{2}, [0-9]{4}|Jul [0-9]{2}, [0-9]{4}|Jan [0-9]{2}, [0-9]{4}|Feb [0-9]{2}, [0-9]{4}|Mar [0-9]{2}, [0-9]{4}|Apr [0-9]{2}, [0-9]{4}|May [0-9]{2}, [0-9]{4}|Jun [0-9]{2}, [0-9]{4}',
       '', str(poten))
   POT.append(potent)    #POTENTIAL


   te = re.sub(
       '<f.*">|</figure>|<i.*"/>|<td class="col col-vl".*</td>|<td class="col col-wg".*</td>|<td class="col col-tt".*</td>|<div class="sub">|[0-9]{4} \~ [0-9]{4}</div>',
       '', str(t))
   tea = re.sub(
       '<div class="b.*</div>|<d.*lout">|<div class="popover.*">|<div class="popover-a.*</div>|<t.*"">|<span class="b.*</span>|<t.*tar">|<t.*me">|<a class="t.*">|[A-Z]{2}</span></a></td>|<td class="col col-ae" .*</td>|<td class="col col-oa".*</td>|<td class="col col-pt".*</td>|<d.*sis">',
       '', str(te))
   team = re.sub(
       '</div>|</td>|Dec [0-9]{1,2}, [0-9]{4}|Nov [0-9]{1,2}, [0-9]{4}|Oct [0-9]{1,2}, [0-9]{4}|Sep [0-9]{1,2}, [0-9]{4}|Aug [0-9]{1,2}, [0-9]{4}|Jul [0-9]{1,2}, [0-9]{4}|Jan [0-9]{1,2}, [0-9]{4}|Feb [0-9]{1,2}, [0-9]{4}|Mar [0-9]{1,2}, [0-9]{4}|Apr [0-9]{1,2}, [0-9]{4}|May [0-9]{1,2}, [0-9]{4}|Jun [0-9]{1,2}, [0-9]{4}|<a h.*">|</a>|\n',
       '', str(tea))
   TEAM_NAME.append(team)    #TEAM NAME


   con = re.sub(
       '[0-9]{2}</span>|[A-Z]{2,3}</span></a>|<ab.*</abbr>|<d.*">|</figure>|<f.*">|<t.*">|<a.*">|<s.*</span>|</div>|</td>|<i.*/>',
       '', str(t))
   cont = re.sub('|[^0-9]{4}|\€.*[MK]', '', str(con))
   contra = re.sub('^[0-9]{2}|\>|\n', '', str(cont))
   CONTRACT.append(contra)    #CONTRACT


   va = re.sub('<d.*b">|<d.*t">|<s.*</span>|<t.*t">|<t.*e">|<td class="col col-wg" data-col="wg">.*K|<d.*</div>|<i.*"/>|</figure>|<a.*</a>|', '', str(t))
   val = re.sub('[0-9]{2}</td>|<td class="col-avatar">|<f.*r">|<t.*a">|</div>|[0-9]{4} \~ [0-9]{4}', '', str(va))
   vale = re.sub(
       '<t.*g">[0-9]{1}|\→|\↗|<d.*">|<f.*">|</span>|<ab.*</abbr>|\↘|<t.*"">|\€|<td class="col col-vl" data-col="vl">|</td>',
       '', str(val))
   valueofplayer = re.sub(
       '\n|<td class="col col-wg" data-col="wg">5|[0-9]{2,3}cm|Free|Dec [0-9]{1,2}, [0-9]{4}|Nov [0-9]{1,2}, [0-9]{4}|Oct [0-9]{1,2}, [0-9]{4}|Sep [0-9]{1,2}, [0-9]{4}|Aug [0-9]{1,2}, [0-9]{4}|Jul [0-9]{1,2}, [0-9]{4}|Jan [0-9]{1,2}, [0-9]{4}|Feb [0-9]{1,2}, [0-9]{4}|Mar [0-9]{1,2}, [0-9]{4}|Apr [0-9]{1,2}, [0-9]{4}|May [0-9]{1,2}, [0-9]{4}|Jun [0-9]{1,2}, [0-9]{4}|\n',
       '', str(vale))
   VALUE.append(valueofplayer)    #VALUE


   wa = re.sub(
       '<d.*b">|<d.*t">|<s.*</span>|<t.*t">|<t.*e">|<td class="col col-vl" data-col="vl">.*[MK]|<d.*</div>|<i.*"/>|</figure>|<a.*</a>',
       '', str(t))
   wag = re.sub('[0-9]{2}</td>|<td class="col-avatar">|<f.*r">|<t.*a">|</div>|[0-9]{4} \~ [0-9]{4}', '', str(wa))
   wage = re.sub(
       '<td class="col-avatar" d.*"">|<f.*">|<d.*er">|</span>|<ab.*</abbr>|\↗|\↘|\→|<td class="col col-vl" data-col="vl">€0</td>|<td class="col col-wg" data-col="wg">|<td class="col col-vl" data-col="vl">|</td>',
       '', str(wag))
   wageofplayer = re.sub(
       '\n|[0-9]{2,3}cm|Free|Dec [0-9]{1,2}, [0-9]{4}|Nov [0-9]{1,2}, [0-9]{4}|Oct [0-9]{1,2}, [0-9]{4}|Sep [0-9]{1,2}, [0-9]{4}|Aug [0-9]{1,2}, [0-9]{4}|Jul [0-9]{1,2}, [0-9]{4}|Jan [0-9]{1,2}, [0-9]{4}|Feb [0-9]{1,2}, [0-9]{4}|Mar [0-9]{1,2}, [0-9]{4}|Apr [0-9]{1,2}, [0-9]{4}|May [0-9]{1,2}, [0-9]{4}|Jun [0-9]{1,2}, [0-9]{4}|\€|\n',
       '', str(wage))
   WAGE.append(wageofplayer)    #WAGE


   s = re.sub(
       '<a.*</a.*>|<td class="col col-oa" .*</td>|<td class="col col-pt".*</td>|<td class="col col-ae".*</td>|<d.*">|<i.*"/>|<td class="col col-vl".*</td>|<td class="col col-wg".*</td>',
       '', str(t))
   st = re.sub(
       '\↘|\w+</span></span>|[A-Za-z]{1,20}</abbr></div></div>|<t.*">|<f.*">|</figure>|[0-9]{4} \~ [0-9]{4}</div>|</div></div></td>|</div>|</td>',
       '', str(s))
   status = re.sub(
       '\↗|\→|Free|Overall|Sprint|N/A|N/|</span>.*cm</span>|<span class="bp3-tag b.*</span>|Dec [0-9]{1,2}, [0-9]{4}|Nov [0-9]{1,2}, [0-9]{4}|Oct [0-9]{1,2}, [0-9]{4}|Sep [0-9]{1,2}, [0-9]{4}|Aug [0-9]{1,2}, [0-9]{4}|Jul [0-9]{1,2}, [0-9]{4}|Jan [0-9]{1,2}, [0-9]{4}|Feb [0-9]{1,2}, [0-9]{4}|Mar [0-9]{1,2}, [0-9]{4}|Apr [0-9]{1,2}, [0-9]{4}|May [0-9]{1,2}, [0-9]{4}|Jun [0-9]{1,2}, [0-9]{4}|</span>|\n',
       '', str(st))
   TOTAL_STATS.append(status)    #STATUS

#Arrangement for element of LISTs

A=61
while 59<A<540002:
  del NAME[A:A+1]
  A=A+60
B=3
while 2<B<10000:
  del AGE[B:B+8]
  B=B+1
del AGE[1]
C=4
while 3<C<10000:
    del OVA[C:C+8]
    C=C+1
del OVA[0:2]
D=5
while 4<D<10000:
    del POT[D:D+8]
    D=D+1
del POT[0:3]
E=6
while 5<E<10000:
    del TEAM_NAME[E:E+8]
    E=E+1
del TEAM_NAME[0:4]
F=6
while 5<F<10000:
    del CONTRACT[F:F+8]
    F=F+1
del CONTRACT[0:4]
G=7
while 6<G<10000:
    del VALUE[G:G+8]
    G=G+1
del VALUE[0:5]
H=8
while 7<H<10000:
    del WAGE[H:H+8]
    H=H+1
del WAGE[0:6]
I=9
while 8<I<10000:
    del TOTAL_STATS[I:I+8]
    I=I+1
del TOTAL_STATS[0:7]

df = pd.DataFrame({"Name": NAME,
                   "Age": AGE,
                   "Overall_Rating": OVA,
                   "Potential": POT,
                   "Team_Name": TEAM_NAME,
                   "Contract_Year": CONTRACT,
                   "Value(M)": VALUE,
                   "Wage(K)": WAGE,
                   "Total_Stats": TOTAL_STATS})
df.head()
df.to_csv('WEB SCRAPPING PROJECT.csv')
