#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class jiaoshi(BaseModel):
    __doc__ = u'''jiaoshi'''
    __tablename__ = 'jiaoshi'

    __loginUser__='jiaoshigonghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='jiaoshigonghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    jiaoshigonghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='教师工号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    jiaoshixingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='教师姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    lianxishouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系手机' )
    xiangpian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='相片' )
    '''
    jiaoshigonghao=VARCHAR
    mima=VARCHAR
    jiaoshixingming=VARCHAR
    xingbie=VARCHAR
    youxiang=VARCHAR
    lianxishouji=VARCHAR
    xiangpian=VARCHAR
    '''
    class Meta:
        db_table = 'jiaoshi'
        verbose_name = verbose_name_plural = '教师'
class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='xuehao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='xuehao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xuehao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='学号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xueshengxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='学生姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    xiangpian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='相片' )
    '''
    xuehao=VARCHAR
    mima=VARCHAR
    xueshengxingming=VARCHAR
    xingbie=VARCHAR
    youxiang=VARCHAR
    shoujihaoma=VARCHAR
    xiangpian=VARCHAR
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = '学生'
class fudaoyuan(BaseModel):
    __doc__ = u'''fudaoyuan'''
    __tablename__ = 'fudaoyuan'

    __loginUser__='gonghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='gonghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    gonghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='工号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    youxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='邮箱' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    xiangpian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='相片' )
    '''
    gonghao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    youxiang=VARCHAR
    shouji=VARCHAR
    xiangpian=VARCHAR
    '''
    class Meta:
        db_table = 'fudaoyuan'
        verbose_name = verbose_name_plural = '辅导员'
class xiangmuxinxi(BaseModel):
    __doc__ = u'''xiangmuxinxi'''
    __tablename__ = 'xiangmuxinxi'



    __authTables__={'gonghao':'fudaoyuan',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xinxibianhao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='信息编号' )
    xiangmumingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='项目名称' )
    xiangmuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目类型' )
    xiangmujianjie=models.TextField   (  null=True, unique=False, verbose_name='项目简介' )
    fengmian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='封面' )
    xiangmuneirong=models.TextField   (  null=True, unique=False, verbose_name='项目内容' )
    gonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    faburiqi=models.DateField   (  null=True, unique=False, verbose_name='发布日期' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    xinxibianhao=VARCHAR
    xiangmumingcheng=VARCHAR
    xiangmuleixing=VARCHAR
    xiangmujianjie=Text
    fengmian=VARCHAR
    xiangmuneirong=Text
    gonghao=VARCHAR
    xingming=VARCHAR
    faburiqi=Date
    userid=BigInteger
    '''
    class Meta:
        db_table = 'xiangmuxinxi'
        verbose_name = verbose_name_plural = '项目信息'
class baomingshenqing(BaseModel):
    __doc__ = u'''baomingshenqing'''
    __tablename__ = 'baomingshenqing'



    __authTables__={'gonghao':'fudaoyuan','xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目名称' )
    xiangmuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目类型' )
    fengmian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='封面' )
    gonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    shenqingriqi=models.DateField   (  null=True, unique=False, verbose_name='申请日期' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    xiangmumingcheng=VARCHAR
    xiangmuleixing=VARCHAR
    fengmian=VARCHAR
    gonghao=VARCHAR
    xingming=VARCHAR
    xuehao=VARCHAR
    xueshengxingming=VARCHAR
    beizhu=VARCHAR
    shenqingriqi=Date
    sfsh=VARCHAR
    shhf=Text
    userid=BigInteger
    '''
    class Meta:
        db_table = 'baomingshenqing'
        verbose_name = verbose_name_plural = '报名申请'
class gerenzuopin(BaseModel):
    __doc__ = u'''gerenzuopin'''
    __tablename__ = 'gerenzuopin'



    __authTables__={'xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目名称' )
    xiangmuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目类型' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    zuopinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作品名称' )
    zuopintupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作品图片' )
    zuopinjianjie=models.TextField   (  null=True, unique=False, verbose_name='作品简介' )
    tijiaoriqi=models.DateField   (  null=True, unique=False, verbose_name='提交日期' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    xiangmumingcheng=VARCHAR
    xiangmuleixing=VARCHAR
    xuehao=VARCHAR
    xueshengxingming=VARCHAR
    zuopinmingcheng=VARCHAR
    zuopintupian=VARCHAR
    zuopinjianjie=Text
    tijiaoriqi=Date
    userid=BigInteger
    '''
    class Meta:
        db_table = 'gerenzuopin'
        verbose_name = verbose_name_plural = '个人作品'
class zuopinxinxi(BaseModel):
    __doc__ = u'''zuopinxinxi'''
    __tablename__ = 'zuopinxinxi'



    __authTables__={'jiaoshigonghao':'jiaoshi',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='是'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='前要登'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目名称' )
    xiangmuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目类型' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xueshengxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学生姓名' )
    zuopinmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作品名称' )
    zuopintupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='作品图片' )
    zuopinjianjie=models.TextField   (  null=True, unique=False, verbose_name='作品简介' )
    tijiaoriqi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='提交日期' )
    jiaoshigonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师工号' )
    jiaoshixingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='教师姓名' )
    pingyu=models.TextField   (  null=True, unique=False, verbose_name='评语' )
    pinglunriqi=models.DateField   (  null=True, unique=False, verbose_name='评论日期' )
    userid=models.BigIntegerField  (  null=True, unique=False, verbose_name='用户id' )
    '''
    xiangmumingcheng=VARCHAR
    xiangmuleixing=VARCHAR
    xuehao=VARCHAR
    xueshengxingming=VARCHAR
    zuopinmingcheng=VARCHAR
    zuopintupian=VARCHAR
    zuopinjianjie=Text
    tijiaoriqi=VARCHAR
    jiaoshigonghao=VARCHAR
    jiaoshixingming=VARCHAR
    pingyu=Text
    pinglunriqi=Date
    userid=BigInteger
    '''
    class Meta:
        db_table = 'zuopinxinxi'
        verbose_name = verbose_name_plural = '作品信息'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '公告信息'
class messages(BaseModel):
    __doc__ = u'''messages'''
    __tablename__ = 'messages'



    __authTables__={}
    __hasMessage__='是'#表属性hasMessage为是，新增留言板表messages,字段content（内容），userid（用户id）
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    userid=models.BigIntegerField  ( null=False, unique=False, verbose_name='留言人id' )
    username=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户名' )
    content=models.TextField   ( null=False, unique=False, verbose_name='留言内容' )
    cpicture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='留言图片' )
    reply=models.TextField   (  null=True, unique=False, verbose_name='回复内容' )
    rpicture=models.CharField ( max_length=255, null=True, unique=False, verbose_name='回复图片' )
    '''
    userid=BigInteger
    username=VARCHAR
    content=Text
    cpicture=VARCHAR
    reply=Text
    rpicture=VARCHAR
    '''
    class Meta:
        db_table = 'messages'
        verbose_name = verbose_name_plural = '留言板'
