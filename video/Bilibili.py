from selenium.webdriver.common.by import By

from util.SystemWebUtil import SystemWebUtil

SystemWebUtil = SystemWebUtil()

browser = SystemWebUtil.get_browser()
browser.get('https://www.bilibili.com/bangumi/play/ep251429?theme=movie&spm_id_from=333.337.0.0')

video = browser.find_element(By.TAG_NAME, 'video')
print(video.get_attribute('src'))
# 最终拿到就是这个地址，可以下载视频

'https://xy61x164x145x210xy240eyf7yc000y301yy13xy.mcdn.bilivideo.cn:4483/upgcxcode/04/86/57328604/57328604_da8-1-416.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1717488617&gen=playurlv2&os=mcdn&oi=3078732882&trid=000060cbb08b9895456ebd3694e225b6dfb2p&mid=0&platform=pc&og=hw&upsig=2fe3a6ee9cc77565f4f509db470a2bb2&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&mcdnid=50004272&bvc=vod&nettype=0&orderid=0,3&buvid=ACE8377F-8DD3-CF43-D69A-22518B6AD21229681infoc&build=0&f=p_0_0&agrr=1&bw=96087&logo=A0020000'


SystemWebUtil.close_browser()