from selenium.webdriver import Firefox, FirefoxOptions
from selenium.common.exceptions import NoSuchElementException
from bz2 import compress, decompress
from json import dumps, loads


try:
    with open('user.txt', 'r') as f:
        user_info = loads(f.read())
        user_id = user_info['id']
        user_pw = user_info['password'].encode('latin1')
        eco = decompress(user_pw).decode()
except FileNotFoundError:
    user_id = input('아이디를 입력하세요 : ')
    user_pw = eco = input('비밀번호를 입력하세요 : ')
    enc = compress(user_pw.encode())
    user_info = {'id': user_id, 'password': enc.decode('latin1')}
    with open('user.txt', 'w') as f:
        f.write(dumps(user_info))

# ---------- 브라우저 옵션 ----------
opts = FirefoxOptions()
# opts.add_argument('--headless')

# ---------- 로그인 ----------
web = Firefox(firefox_options=opts)
web.get('http://eclass.kpu.ac.kr/ilos/main/member/login_form.acl')
web.find_element_by_name('usr_id').send_keys(user_id)
web.find_element_by_name('usr_pwd').send_keys(eco)
web.find_element_by_id('login_btn').click()

board = [['http://eclass.kpu.ac.kr/ilos/st/course/notice_list_form.acl', '공지', 'site-link'],
         ['http://eclass.kpu.ac.kr/ilos/st/course/lecture_material_list_form.acl', '자료', 'top_div'],
         ['http://eclass.kpu.ac.kr/ilos/st/course/report_list_form.acl', '과제', 'site-link'],
         ['http://eclass.kpu.ac.kr/ilos/st/course/project_list_form.acl', '팀플', 'site-link']]
info = dict()

class_cnt = len(web.find_elements_by_class_name('sub_open'))
for i in range(class_cnt):
    web.get('http://eclass.kpu.ac.kr/ilos/main/main_form.acl')
    class_ = web.find_elements_by_class_name('sub_open')
    class_name = class_[i].text
    class_[i].click()
    info[class_name] = dict()
    for bd in board:
        web.get(bd[0])
        try:
            obj = web.find_element_by_class_name(bd[2])
            sub = obj.text
            try:
                if bd[1] == '자료':
                    raise NoSuchElementException
                sub = sub.replace(obj.find_element_by_tag_name('span').text, '')
            except NoSuchElementException:
                pass
            finally:
                info[class_name][bd[1]] = sub
        except NoSuchElementException:
            info[class_name][bd[1]] = 'empty'
web.quit()

# ---------- 기존 정보와 비교 ----------
try:
    with open('eclass.txt', 'r') as f:
        saved_info = loads(f.read())
        for x, y in info.items():
            if y != saved_info[x]:
                for v, w in y.items():
                    if w != saved_info[x][v]:
                        print('[%s] 새 %s : %s' % (x, v, w))
except FileNotFoundError:
    print('정보 파일 새로 저장')
finally:
    with open('eclass.txt', 'w') as f:
        f.write(dumps(info))
