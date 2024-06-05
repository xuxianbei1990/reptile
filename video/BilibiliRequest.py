import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Origin': 'https://www.bilibili.com',
    'Range': 'bytes=26889839-27010677',
    'Referer': 'https://www.bilibili.com/bangumi/play/ep251429?theme=movie&spm_id_from=333.337.0.0',
    'Accept': '*/*',
    'Accept-Encoding': 'identity;q=1, *;q=0',
    'Accept-Language': 'zh-CN,zh;q=0.9',
}


def send_request(url):
    response = requests.get(url=url, headers=headers, stream=True)
    return response


url = 'https://xy182x201x240x19xy.mcdn.bilivideo.cn:4483/upgcxcode/04/86/57328604/57328604_da8-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1717505474&gen=playurlv2&os=mcdn&oi=3078732882&trid=0000fc857bb0ba514dfdbb9db30163c3d196p&mid=398007110&platform=pc&og=hw&upsig=30ee6255cc29ecd5d7da237e1f5ab68b&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&mcdnid=50003771&bvc=vod&nettype=0&orderid=0,3&buvid=D20EC79E-2C13-E6DF-0E6C-01CE5988C34332297infoc&build=0&f=p_0_0&agrr=1&bw=24208&logo=A0020000'

response = send_request(url)

# 定义保存视频的文件名
video_filename = 'downloaded_video.mp4'

# 检查Content-Type是否为video/mp4
if response.headers.get('Content-Type') == 'video/mp4' and response.status_code == 206:
    with open(video_filename, 'wb') as f:
        for chunk in response.iter_content(1024):
            if chunk:
                f.write(chunk)
    print(f'Video saved to {video_filename}')
else:
    print('Failed to retrieve video. Either the content type is not video/mp4 or the request failed.')
