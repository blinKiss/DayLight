from bs4 import BeautifulSoup
txt_data = '''
<div class="section" style="margin-bottom:20px; white-space:nowrap;" id="right_dailyList"> 
 <h4>분야별 주요뉴스</h4> 
 <div class="classfy sd" style="display:block"> 
  <ul class="list_txt"> 
   <li> <a href="https://n.news.naver.com/mnews/article/021/0002556235?sid=100" class="nclicks(rig.secteco)" title="[속보] 박홍근 “김건희 여사, 신성 불가침?…‘국민 특검’ 꼭 관철”">[속보] 박홍근 “김건희 여사, 신성 불가침?…‘국민 특검’ 꼭 관철”</a> </li> 
   <li> <a href="https://n.news.naver.com/mnews/article/469/0000723081?sid=100" class="nclicks(rig.secteco)" title="탈당→레임덕→탄핵... 험해지는 '친윤 시나리오'의 진화">탈당→레임덕→탄핵... 험해지는 '친윤 시나리오'의 진화</a> </li> 
   <li> <a href="https://n.news.naver.com/mnews/article/277/0005217170?sid=100" class="nclicks(rig.secteco)" title="野3당 '대장동 특검' 한 목소리… 정의당 '김건희 특검'엔 반기">野3당 '대장동 특검' 한 목소리… 정의당 '김건희 특검'엔 반기</a> </li> 
   <li> <a href="https://n.news.naver.com/mnews/article/001/0013752941?sid=104" class="nclicks(rig.secteco)" title="美, 3일 연속 정체불명 비행체 격추…&quot;셋 다 크기&middot;속도 비슷&quot;(종합2보)">美, 3일 연속 정체불명 비행체 격추…&quot;셋 다 크기&middot;속도 비슷&quot;(종합2보)</a> </li> 
   <li> <a href="https://n.news.naver.com/mnews/article/081/0003338861?sid=104" class="nclicks(rig.secteco)" title="지진으로 튀르키예 GDP의 10% 손실 전망…“107조원 증발”">지진으로 튀르키예 GDP의 10% 손실 전망…“107조원 증발”</a> </li> 
  </ul> 
  <ul class="list_txt"> 
   <ul class="list_txt"> 
    <li> <a href="https://n.news.naver.com/mnews/article/018/0005423564?sid=101" class="nclicks(rig.secteco)" title="삼성전자, 전국 삼성 디지털프라자서 ‘혼수&middot;이사 특별 기획전’ 연다">삼성전자, 전국 삼성 디지털프라자서 ‘혼수&middot;이사 특별 기획전’ 연다</a> </li> 
    <li> <a href="https://n.news.naver.com/mnews/article/022/0003782866?sid=101" class="nclicks(rig.secteco)" title="2월 초 반도체 수출 40.7% 감소… 누적 무역적자 176억달러">2월 초 반도체 수출 40.7% 감소… 누적 무역적자 176억달러</a> </li> 
    <li> <a href="https://n.news.naver.com/mnews/article/092/0002282468?sid=101" class="nclicks(rig.secteco)" title="정부, 튀르키예 지진피해 성금 송금절차 완화">정부, 튀르키예 지진피해 성금 송금절차 완화</a> </li> 
    <li> <a href="https://n.news.naver.com/mnews/article/648/0000013801?sid=105" class="nclicks(rig.secteco)" title="야놀자&middot;여기어때 '어쩌나'…카톡 선물하기에 호텔 입점한다">야놀자&middot;여기어때 '어쩌나'…카톡 선물하기에 호텔 입점한다</a> </li> 
    <li> <a href="https://n.news.naver.com/mnews/article/003/0011688469?sid=105" class="nclicks(rig.secteco)" title="네이버, 튀르키예&middot;시리아 지진 피해 복구에 100만 달러 기부">네이버, 튀르키예&middot;시리아 지진 피해 복구에 100만 달러 기부</a> </li> 
   </ul> 
   <ul class="list_txt"> 
    <ul class="list_txt"> 
     <li> <a href="https://n.news.naver.com/mnews/article/023/0003745880?sid=102" class="nclicks(rig.secteco)" title="[단독] 김성태 수백억 돈세탁, 로비 의혹… 검찰, 300억 사용처 추적">[단독] 김성태 수백억 돈세탁, 로비 의혹… 검찰, 300억 사용처 추적</a> </li> 
     <li> <a href="https://n.news.naver.com/mnews/article/586/0000052261?sid=102" class="nclicks(rig.secteco)" title="&quot;3월23일까지 답 달라&quot; 전장연, 지하철 탑승 시위 재개 경고">&quot;3월23일까지 답 달라&quot; 전장연, 지하철 탑승 시위 재개 경고</a> </li> 
     <li> <a href="https://n.news.naver.com/mnews/article/022/0003782867?sid=102" class="nclicks(rig.secteco)" title="스마트 워치 자르고 전 여친 납치한 20대 체포 “같이 마약”…필로폰 ‘양성’">스마트 워치 자르고 전 여친 납치한 20대 체포 “같이 마약”…필로폰 ‘양성’</a> </li> 
     <li> <a href="https://n.news.naver.com/mnews/article/421/0006626940?sid=103" class="nclicks(rig.secteco)" title="현대차그룹, 美 전기차 누적 10만대 팔았다…&quot;올해만 13만대 목표&quot;">현대차그룹, 美 전기차 누적 10만대 팔았다…&quot;올해만 13만대 목표&quot;</a> </li> 
     <li> <a href="https://n.news.naver.com/mnews/article/016/0002102912?sid=103" class="nclicks(rig.secteco)" title="1원짜리 참기름병, 국보 된 사연..수만 배 경매">1원짜리 참기름병, 국보 된 사연..수만 배 경매</a> </li> 
    </ul> 
   </ul>
  </ul>
 </div> 
</div>
'''

# 15개 뉴스를 글자만 뽑아서 출력
soup = BeautifulSoup(txt_data, 'html.parser')
count = 0
for i in soup.select('div a'):
    print(i.string)
    # print(i['title'])
    count += 1
    if(count == 15):
        break