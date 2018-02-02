# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import models
import chardet
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')
# 首页
def index(request):
    #news = models.newsinfo.objects.get(id=1)
    #print(news.content)
    return render(request,'home.html')
# 功能 ajax
def ajax_verify(request):
    '''
    绿：green 红：red   蓝：blue  黑：black 灰：grey  黄：yellow    紫：purple    白：while
    :param request: 请求
    :return:
    '''
    number = 0
    # 正文
    text = request.GET["text"]
    # 人名
    prople_name = request.GET["prople_name"]
    if  prople_name:
        text,num = myReplace(text,prople_name,"red")
        number += num
    # 地名
    toponymy = request.GET["toponymy"]
    if  toponymy:
        text, num = myReplace(text,toponymy,"#3390FF")
        number += num
    # 组织机构
    institutional_framework = request.GET["institutional_framework"]
    if  institutional_framework:
        text, num = myReplace(text,institutional_framework,"yellow") #wine red
        number += num

    re_text =text
    data={}
    data["re_text"] = re_text
    data["number"] = number
    return JsonResponse(data)

def myReplace(text,rep,color=""):
    reps = []
    if rep!=None:
        reps = rep.split()
    num = len(reps)
    for x in reps:
        strlist = []
        for i in x:
            if not i.isdigit():
                strlist.append(i)
        x = "".join(strlist)

        if "市" in x or "省" in x or "县" in x:
            x = x[0:-1]
        text = text.replace(x,'<span style="background:%s">%s</span>' %(color,x))
    return text,num

# 按 id 查询
def ajax_select(request):
    newsid = int(request.GET["newsid"])
    news = models.newsinfo.objects.get(id=newsid)
    news = objectToDict(news)
    content = news["content"]
    people = news["people"]
    toponymy = news["toponymy"]
    organization = news["organization"]
    content,num= myReplace(content,people,"red")
    news["people_num"] = num
    content,num= myReplace(content,toponymy, "#3399FF")#3390FF
    news["toponymy_num"] = num
    content,num = myReplace(content,organization, "yellow")
    news["organization_num"] = num
    news["centent"] = content
    return JsonResponse(news)
# 对象转换为字典
def objectToDict(myobject):
    mydict = {}
    mydict["id"] = myobject.id
    mydict["title"] = myobject.title
    mydict["content"] = myobject.content
    mydict["people"] = myobject.people
    mydict["toponymy"] = myobject.toponymy
    mydict["organization"] = myobject.organization
    mydict["people_num"] = myobject.people_num
    mydict["toponymy_num"] = myobject.toponymy_num
    mydict["organization_num"] = myobject.organization_num
    mydict["people_error"] = myobject.people_error
    mydict["people_error_num"] = myobject.people_error_num
    mydict["people_miss"] = myobject.people_miss
    mydict["people_miss_num"] = myobject.people_miss_num
    mydict["toponymy_error"] = myobject.toponymy_error
    mydict["toponymy_error_num"] = myobject.toponymy_error_num
    mydict["toponymy_miss"] = myobject.toponymy_miss
    mydict["toponymy_miss_num"] = myobject.toponymy_miss_num
    mydict["organization_error"] = myobject.organization_error
    mydict["organization_error_num"] = myobject.organization_error_num
    mydict["organization_miss"] = myobject.organization_miss
    mydict["organization_miss_num"] = myobject.organization_miss_num

    return mydict

# 保存
def ajax_save(request):
    newsid = int(request.GET["newsid"])
    news = models.newsinfo.objects.get(id=newsid)

    news.people_num = int(request.GET["people_num"])
    news.toponymy_num = int(request.GET["toponymy_num"])
    news.organization_num = int(request.GET["organization_num"])
    # 错误人名
    people_error = request.GET["people_error"].strip()
    news.people_error = people_error
    if people_error !=None and people_error !="":
        news.people_error_num = strNum(people_error)
    else:
        news.people_error_num = 0
    # 漏掉人名
    people_miss = request.GET["people_miss"].strip()
    news.people_miss = people_miss
    if people_miss != None and people_miss != "":
        news.people_miss_num = strNum(people_miss)
    else:
        news.people_miss_num = 0
    # 错误地名
    toponymy_error = request.GET["toponymy_error"].strip()
    news.toponymy_error = toponymy_error
    if toponymy_error != None and toponymy_error != "":
        news.toponymy_error_num = strNum(toponymy_error)
    else:
        news.toponymy_error_num = 0
    # 漏掉地名
    toponymy_miss = request.GET["toponymy_miss"].strip()
    news.toponymy_miss = toponymy_miss
    if toponymy_miss != None and toponymy_miss != "":
        news.toponymy_miss_num = strNum(toponymy_miss)
    else:
        news.toponymy_miss_num = 0
    # 错误机构
    organization_error = request.GET["organization_error"].strip()
    news.organization_error = organization_error
    if organization_error != None and organization_error != "":
        news.organization_error_num = strNum(organization_error)
    else:
        news.organization_error_num = 0
    # 漏掉机构
    organization_miss = request.GET["organization_miss"].strip()
    news.organization_miss = organization_miss
    if organization_miss != None and organization_miss != "":
        news.organization_miss_num = strNum(organization_miss)
    else:
        news.organization_miss_num = 0

    news.save()
    return JsonResponse({"msg":"保存成功！"})


# 词个数
def strNum(string):
    strs = str(string).split()
    num = len(strs)
    return num







