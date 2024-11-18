'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from NAIF Source code = ]
{"Developer":"https://t.me/naifn09"}

'''

import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *


@Client.on_message(filters.group, group=24)
def addCustomReplyG(c,m):
    k = r.get(f'{Dev_Naif}:botkey')
    Thread(target=addreplyg,args=(c,m,k)).start()
    
def addreplyg(c,m,k):
  if not r.get(f'{m.chat.id}:enable:{Dev_Naif}'):  return
  if r.get(f'{m.chat.id}:mute:{Dev_Naif}') and not admin_pls(m.from_user.id,m.chat.id):  return 
  if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Naif}'):  return 
  if r.get(f'{m.from_user.id}:mute:{Dev_Naif}'):  return 
  if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}'):  return    
  if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}'):  return
  if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}'):  return 
  if m.text:
   text = m.text
   name = r.get(f'{Dev_Naif}:BotName') if r.get(f'{Dev_Naif}:BotName') else 'نايف'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={text}')
   if r.get(f'Custom:{Dev_Naif}&text={text}'):
       text = r.get(f'Custom:{Dev_Naif}&text={text}')
   
   if r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Naif}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد العام')
     return 
   
   if r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Naif}')
     m.reply(f'{k} من عيوني لغيت مسح الرد العام')
     return 
   
   if m.text == 'الغاء' and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}'):
       r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
       m.reply(f'{k} من عيوني لغيت اضافة الرد العام')

   if r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id,m.chat.id):
      if not r.get(f'{m.text}:filterInfo:{Dev_Naif}'):
        r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Naif}')
        return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود العامه')
      else:
           r.delete(f'{m.text}:filter:{Dev_Naif}')
           r.delete(f'{m.text}:filtertype:{Dev_Naif}')
           r.delete(f'{m.text}:filterInfo:{Dev_Naif}')
           r.srem(f'FiltersList:{Dev_Naif}', m.text)
           r.delete(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Naif}')
           return m.reply(f'( {m.text} )\n{k} وحذفنا الرد ياحلو')   

   
   if text == 'تعطيل ردود المطور':
     if not owner_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المالك وفوق ) بس')
     if r.get(f'{m.chat.id}:lock_global:{Dev_Naif}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود المطور معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.set(f'{m.chat.id}:lock_global:{Dev_Naif}',1)
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت ردود المطور\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل ردود المطور':
     if not owner_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المالك وفوق ) بس')
     if not r.get(f'{m.chat.id}:lock_global:{Dev_Naif}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود المطور مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.delete(f'{m.chat.id}:lock_global:{Dev_Naif}')
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت ردود المطور\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'الردود العامه':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
      if not r.smembers(f'FiltersList:{Dev_Naif}'):
       return m.reply(f'{k} مافيه ردود عامه مضافه')
      else:
       text = 'ردود البوت:\n'
       count = 1
       for reply in r.smembers(f'FiltersList:{Dev_Naif}'):
          rep = reply
          type = r.get(f'{rep}:filtertype:{Dev_Naif}')
          text += f'\n{count} - ( {rep} ) ࿓ ( {type} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
  
   if text == 'مسح الردود العامه':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
      if not r.smembers(f'FiltersList:{Dev_Naif}'):
        return m.reply(f'{k} مافيه ردود عامه مضافه')
      else:
        total = 0
        for reply in r.smembers(f'FiltersList:{Dev_Naif}'):
           rep = reply
           r.delete(f'{rep}:filter:{Dev_Naif}')
           r.delete(f'{rep}:filtertype:{Dev_Naif}')
           r.delete(f'{rep}:filterInfo:{Dev_Naif}')
           r.srem(f'FiltersList:{Dev_Naif}', rep)
           total += 1
        return m.reply(f'{k} ابشر مسحت ( {total} ) من الردود العامه')   
     
   if text == 'مسح رد عام':
     if not r.get(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Naif}'):
      if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
      else:
        r.set(f'{m.chat.id}:delFilterG:{m.from_user.id}{Dev_Naif}',1)
        m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
        return 
   
   if text == 'اضف رد عام':
       if not r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Naif}'):
         if not dev2_pls(m.from_user.id, m.chat.id):
           return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
         else:
           m.reply(f'{k} حلو ، الحين ارسل الكلمة اللي تبيها')
           r.set(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Naif}',1)
           return 
   
   if r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id, m.chat.id):
       text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
       r.set(f'{text}:filter:{Dev_Naif}', f'type=text&text={m.text.html}')
       r.set(f'{text}:filtertype:{Dev_Naif}','نص')
       r.set(f'{text}:filterInfo:{Dev_Naif}', f'by={m.from_user.id}')
       r.sadd(f'FiltersList:{Dev_Naif}', f'{text}')
       r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
       return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
     
   if r.get(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id,m.chat.id):
      r.set(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}', m.text)
      r.delete(f'{m.chat.id}:addFilterG:{m.from_user.id}{Dev_Naif}')
      m.reply(f'{k} حلو الحين ارسل جواب الرد\n{k} ( نص,صوره,فيديو,متحركه,بصمه,صوت,ملف )\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
      return 
  
  addreply_media(c,m,k)

def addreply_media(c,m,k):
   if m.photo and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'photo'
      photo = m.photo.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      r.set(f'{text}:filter:{Dev_Naif}', f'type={type}&photo={photo}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Naif}','صوره')
      r.set(f'{text}:filterInfo:{Dev_Naif}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Naif}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.video and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'video'
      video = m.video.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      r.set(f'{text}:filter:{Dev_Naif}', f'type={type}&video={video}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Naif}','فيديو')
      r.set(f'{text}:filterInfo:{Dev_Naif}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Naif}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.animation and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'animation'
      anim = m.animation.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      r.set(f'{text}:filter:{Dev_Naif}', f'type={type}&animation={anim}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Naif}','متحركه')
      r.set(f'{text}:filterInfo:{Dev_Naif}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Naif}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.audio and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'audio'
      aud = m.audio.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      r.set(f'{text}:filter:{Dev_Naif}', f'type={type}&audio={aud}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Naif}','صوت')
      r.set(f'{text}:filterInfo:{Dev_Naif}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Naif}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.voice and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'voice'
      voice = m.voice.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      r.set(f'{text}:filter:{Dev_Naif}', f'type={type}&voice={voice}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Naif}','بصمه')
      r.set(f'{text}:filterInfo:{Dev_Naif}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Naif}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.document and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'doc'
      doc = m.document.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      r.set(f'{text}:filter:{Dev_Naif}', f'type={type}&doc={doc}&caption={caption}')
      r.set(f'{text}:filtertype:{Dev_Naif}','ملف')
      r.set(f'{text}:filterInfo:{Dev_Naif}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Naif}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.sticker and r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id, m.chat.id):
      type = 'sticker'
      stic = m.sticker.file_id
      text = r.get(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      r.set(f'{text}:filter:{Dev_Naif}', f'type={type}&sticker={stic}')
      r.set(f'{text}:filtertype:{Dev_Naif}','ملصق')
      r.set(f'{text}:filterInfo:{Dev_Naif}', f'by={m.from_user.id}')
      r.sadd(f'FiltersList:{Dev_Naif}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2GG:{m.from_user.id}{Dev_Naif}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   
   
   
   
'''
@Client.on_message(filters.group, group=25)
def addCustomReplyDoneG(c,m):
    k = r.get(f'{Dev_Naif}:botkey')
    addreply2g(c,m,k)
    
def addreply2g(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Naif}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Naif}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Naif}') and not admin_pls(m.from_user.id,m.chat.id):  return
   
   
   if m.text:
     
'''     
     
   
   
   
   

@Client.on_message(filters.group & filters.text, group=26)
def addCustomReplyRandomG(c,m):
    k = r.get(f'{Dev_Naif}:botkey')
    Thread(target=addreplyrandomg,args=(c,m,k)).start()
   

def addreplyrandomg(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Naif}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Naif}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}'):  return 
   text = m.text
   name = r.get(f'{Dev_Naif}:BotName') if r.get(f'{Dev_Naif}:BotName') else 'نايف'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={text}')
   if r.get(f'Custom:{Dev_Naif}&text={text}'):
       text = r.get(f'Custom:{Dev_Naif}&text={text}')

   if r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Naif}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد المتعدد عام')
     return 
   
   if r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     rep = r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}')
     r.delete(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}')
     r.delete(f'{rep.decode("utf-8")}:randomfilter:{Dev_Naif}')
     m.reply(f'{k} من عيوني لغيت اضافه الرد المتعدد عام')
     return 
     
   if r.get(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Naif}')
     return m.reply(f'{k} من عيوني لغيت مسح الرد المتعدد العام')
   
   if r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}') and text == 'تم':
     text = r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}')
     count = len(r.smembers((f'{text}:randomfilter:{Dev_Naif}')))
     r.set(f'{text}:randomFilter:{Dev_Naif}', 1)
     r.sadd(f'RFiltersList:{Dev_Naif}', text)
     r.delete(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}')
     return m.reply(f'{k} تم اضافه الرد المتعدد ( {text} )\n{k} بـ ( {count} ) جواب رد\n☆',parse_mode=ParseMode.HTML)
   
   if r.get(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id,m.chat.id):
     if not r.get(f'{m.text}:randomFilter:{Dev_Naif}'):
       r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Naif}')
       return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
     else:
       r.delete(f'{m.text}:randomFilter:{Dev_Naif}')
       r.delete(f'{m.text}:randomfilter:{Dev_Naif}')
       r.delete(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Naif}')
       r.srem(f'RFiltersList:{Dev_Naif}',m.text)
       return m.reply(f'{k} ابشر مسحت الرد المتعدد ')
       
   
   if r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Naif}')
     r.set(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}',m.text)
     return m.reply(f'{k} حلو الحين ارسل اجوبة الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
   
   if r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}') and dev2_pls(m.from_user.id,m.chat.id):
     text = r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}')
     r.sadd(f'{text}:randomfilter:{Dev_Naif}', m.text.html)
     return m.reply(f'{k} حلو ضفت هذا الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
     
   if text == 'الردود المتعدده العامه':
     if not dev2_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
      if not r.smembers(f'RFiltersList:{Dev_Naif}'):
       return m.reply(f'{k} مافيه ردود عشوائيه عامة')
      else:
       text = 'الردود المتعدده:\n'
       count = 1
       for reply in r.smembers(f'RFiltersList:{Dev_Naif}'):
          rep = reply
          ttt = len(r.smembers(f'{rep}:randomfilter:{Dev_Naif}'))
          text += f'\n{count} - ( {rep} ) ࿓ ( {ttt} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح الردود المتعدده العامه':
     if not dev2_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
       if not r.smembers(f'RFiltersList:{Dev_Naif}'):
         return m.reply(f'{k} مافيه ردود عشوائيه عامة')
       else:
         count = 0
         for reply in r.smembers(f'RFiltersList:{Dev_Naif}'):
            rep = reply
            r.delete(f'{rep}:randomfilter:{Dev_Naif}')
            r.srem(f'RFiltersList:{Dev_Naif}', rep)
            r.delete(f'{rep}:randomFilter:{Dev_Naif}')
            count += 1
         return m.reply(f'{k} ابشر مسحت ( {count} ) رد متعدد ')
            
            
   
   if text == 'اضف رد متعدد عام' and not r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Naif}') and not r.get(f'{m.chat.id}:addFilterRG2:{m.from_user.id}{Dev_Naif}'):
     if not dev2_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Naif}',1)
       return m.reply(f'{k} حلو ، ارسل الحين الكلمة الي تبيها')
   
   if text == 'مسح رد متعدد عام' and not r.get(f'{m.chat.id}:addFilterRG:{m.from_user.id}{Dev_Naif}'):
     if not dev2_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( Dev²🎖️ وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:delFilterRG:{m.from_user.id}{Dev_Naif}',1)
       return m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
   
   
     
     
     
