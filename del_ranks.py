'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from Naif Source code = ]
{"Developer":"https://t.me/naifn09"}

'''

import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *
from helpers.Ranks import isLockCommand


@Client.on_message(filters.text & filters.group, group=13)
def delRanksHandler(c,m):
    k = r.get(f'{Dev_Naif}:botkey')
    Thread(target=del_ranks_func,args=(c,m,k)).start()
    

def del_ranks_func(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Naif}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Naif}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Naif}'):  return 
   
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}'):  return 
   text = m.text
   name = r.get(f'{Dev_Naif}:BotName') if r.get(f'{Dev_Naif}:BotName') else 'نايف'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={text}')
   if r.get(f'Custom:{Dev_Naif}&text={text}'):
       text = r.get(f'Custom:{Dev_Naif}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   id = m.from_user.id
   cid = m.chat.id
   demoted = '''{} ابشر مسحتها {}
{} مسحت ( {} ) من {} 
☆
'''
   if text == 'مسح قائمه Dev':
      if not devp_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( Dev🎖️) بس')
      else:
        if not r.smembers(f'{Dev_Naif}DEV2'):
          return m.reply(f'{k} مافيه قائمة Dev²🎖')
        else:
          count = 0
          for dev2 in r.smembers(f'{Dev_Naif}DEV2'):
             r.srem(f'{Dev_Naif}DEV2', int(dev2))
             r.delete(f'{int(dev2)}:rankDEV2:{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'قائمة Dev'))
   
   if text == 'مسح قائمه MY':
      if not dev2_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      else:
        if not r.smembers(f'{Dev_Naif}DEV'):
          return m.reply(f'{k} مافيه قائمة Myth🎖️')
        else:
          count = 0
          for dev in r.smembers(f'{Dev_Naif}DEV'):
             r.srem(f'{Dev_Naif}DEV', int(dev))
             r.delete(f'{int(dev)}:rankDEV:{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'قائمة MY'))
   
   if text == 'مسح المالكين الاساسيين':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( Myth🎖️ مالك القروب وفوق) بس')
      else:
        if not r.smembers(f'{cid}:listGOWNER:{Dev_Naif}'):
          return m.reply(f'{k} مافيه مالكين اساسيين')
        else:
          count = 0
          for gowner in r.smembers(f'{cid}:listGOWNER:{Dev_Naif}'):
             r.srem(f'{cid}:listGOWNER:{Dev_Naif}', int(gowner))
             r.delete(f'{cid}:rankGOWNER:{int(gowner)}{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المالكين الاساسيين'))
   
   if text == 'مسح المالكين':
      if not gowner_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المالك الاساسي وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listOWNER:{Dev_Naif}'):
          return m.reply(f'{k} مافيه مالكين ')
        else:
          count = 0
          for owner in r.smembers(f'{cid}:listOWNER:{Dev_Naif}'):
             r.srem(f'{cid}:listOWNER:{Dev_Naif}', int(owner))
             r.delete(f'{cid}:rankOWNER:{int(owner)}{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المالكين'))
   
   if text == 'مسح المدراء':
      if not owner_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المالك وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listMOD:{Dev_Naif}'):
          return m.reply(f'{k} مافيه مدراء')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listMOD:{Dev_Naif}'):
             r.srem(f'{cid}:listMOD:{Dev_Naif}', int(MOD))
             r.delete(f'{cid}:rankMOD:{int(MOD)}{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المدراء'))
   
   if text == 'مسح الادمنيه' or text == 'مسح الادمن':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listADMIN:{Dev_Naif}'):
          return m.reply(f'{k} مافيه ادمن')
        else:
          count = 0
          for ADM in r.smembers(f'{cid}:listADMIN:{Dev_Naif}'):
             r.srem(f'{cid}:listADMIN:{Dev_Naif}', int(ADM))
             r.delete(f'{cid}:rankADMIN:{int(ADM)}{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'الادمن'))
   
   if text == 'مسح المميزين':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listPRE:{Dev_Naif}'):
          return m.reply(f'{k} مافيه مميزين')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listPRE:{Dev_Naif}'):
             r.srem(f'{cid}:listPRE:{Dev_Naif}', int(MOD))
             r.delete(f'{cid}:rankPRE:{int(MOD)}{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المميزين'))
   
   if text == 'مسح المكتومين':
      if not mod_pls(id, cid):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        if not r.smembers(f'{cid}:listMUTE:{Dev_Naif}'):
          return m.reply(f'{k} مافيه مكتومين')
        else:
          count = 0
          for MOD in r.smembers(f'{cid}:listMUTE:{Dev_Naif}'):
             try:
               mod = int(MOD)
             except:
               mod = MOD
             r.srem(f'{cid}:listMUTE:{Dev_Naif}', mod)
             r.delete(f'{mod}:mute:{cid}{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المكتومين'))
   
   if text == 'مسح المكتومين عام':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( Myth🎖️ وفوق ) بس')
      else:
        if not r.smembers(f'listMUTE:{Dev_Naif}'):
          return m.reply(f'{k} مافيه مكتومين عام')
        else:
          count = 0
          for MOD in r.smembers(f'listMUTE:{Dev_Naif}'):
             r.srem(f'listMUTE:{Dev_Naif}', int(MOD))
             r.delete(f'{int(MOD)}:mute:{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'المكتومين عام'))
   
   if text == 'مسح المحظورين عام':
      if not dev_pls(id, cid):
        return m.reply(f'{k} هذا الامر يخص ( Myth🎖️ وفوق ) بس')
      else:
        if not r.smembers(f'listGBAN:{Dev_Naif}'):
          return m.reply(f'{k} مافيه حمير محظورين')
        else:
          count = 0
          for MOD in r.smembers(f'listGBAN:{Dev_Naif}'):
             r.srem(f'listGBAN:{Dev_Naif}', int(MOD))
             r.delete(f'{int(MOD)}:gban:{Dev_Naif}')
             count += 1
          m.reply(demoted.format(k,get_rank(id,cid),k,count,'الحمير المحظورين عام'))
          
             
       
   
   
