
'''


██████╗░██████╗░██████╗░
██╔══██╗╚════██╗██╔══██╗
██████╔╝░█████╔╝██║░░██║
██╔══██╗░╚═══██╗██║░░██║
██║░░██║██████╔╝██████╔╝
╚═╝░░╚═╝╚═════╝░╚═════╝░


[ = This plugin is a part from NAIF Source code = ]
{"Developer":"https://t.me/naifn0966"}

'''
import random, re, time
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *

@Client.on_message(filters.text & filters.group, group=999)
def customCummandHandler(c,m):
    k = r.get(f'{Dev_Naif}:botkey')
    Thread(target=addcommand,args=(c,m,k)).start()
   
   
def addcommand(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Naif}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Naif}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Naif}'):  return  
   if r.get(f'{m.chat.id}:mute:{Dev_Naif}') and not admin_pls(m.from_user.id,m.chat.id):  return
   text = m.text
   name = r.get(f'{Dev_Naif}:BotName') if r.get(f'{Dev_Naif}:BotName') else 'نايف'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={text}')
   if r.get(f'Custom:{Dev_Naif}&text={text}'):
       text = r.get(f'Custom:{Dev_Naif}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضافة امر ')
   
   if r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Naif}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضافة امر ')

   if text == 'الاوامر المضافه' or text == 'الاوامر المضافة':
      if not owner_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
      else:
          if not r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Naif}'):
            return m.reply(quote=True,text=f'{k} مافيه اوامر مضافه')
          else:
              text = 'الاوامر المضافة:\n'
              count = 0
              for cmnd in r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Naif}'):
                 count += 1
                 command = cmnd
                 cc = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={command}')
                 old_c = cc
                 text += f'{count}) {command} ~ ( {old_c} )\n'
              text += '\n༄'
              return m.reply(quote=True,text=text)
   
   if text == 'اضف امر' or text == 'تغيير امر':
     if not r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}'):
       if not owner_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}',1)
          m.reply(quote=True,text=f'{k} تمام عيني ، ارسل الامر القديم عشان اغيره')
          return

   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:addCustom:{m.from_user.id}{Dev_Naif}')
      r.set(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Naif}', m.text)
      m.reply(quote=True,text=f'{k} حلو عشان تغيير امر ( {m.text} )\n{k} ارسل الامر الجديد الحين\n☆')
      return
   
   if r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Naif}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      command_o = r.get(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Naif}')
      command_n = m.text
      r.delete(f'{m.chat.id}:addCustom2:{m.from_user.id}{Dev_Naif}')
      r.set(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={command_n}', command_o)
      r.sadd(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Naif}', command_n)
      m.reply(quote=True,text=f'{k} غيرت الامر القديم {command_o}\n{k} الى الامر الجديد ( {command_n} )')
      return 


@Client.on_message(filters.text & filters.group, group=1000)
def delCustomCommandHandler(c,m):
    k = r.get(f'{Dev_Naif}:botkey')
    Thread(target=delcommand,args=(c,m,k)).start()
   
   
def delcommand(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{Dev_Naif}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Naif}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Naif}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}'):  return
   text = m.text
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={m.text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={m.text}')
   
   if r.get(f'Custom:{Dev_Naif}&text={m.text}'):
       text = r.get(f'Custom:{Dev_Naif}&text={m.text}')
   
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت مسح امر ')

   if text == 'مسح الاوامر' or text == 'مسح الاوامر المضافة':
     if not mod_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المدير وفوق ) وبس') 
     else:
       if not r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Naif}'):
         return m.reply(quote=True,text=f'{k} مافيه اوامر مضافه')
       else:
         count = 0
         for cmnd in r.smembers(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Naif}'):
           command = cmnd
           r.delete(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={command}')
           r.srem(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Naif}', command)
           count += 1
         text = f'من「 {m.from_user.mention} 」\n{k} ابشر مسحت {count} أمر\n☆'
         return m.reply(quote=True,text=text)
       
   
   if text == 'مسح امر':
     if not r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}'):
       if not mod_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المدير وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}',1)
          m.reply(quote=True,text=f'{k} ارسل الامر الحين')
          return
      

   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}') and admin_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:delCustom:{m.from_user.id}{Dev_Naif}')
      if not r.get(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={m.text}'):
         return m.reply(quote=True,text=f'{k} هذا الأمر مو مضاف')
      r.srem(f'{m.chat.id}:listCustom:{m.chat.id}{Dev_Naif}', m.text)
      r.delete(f'{m.chat.id}:Custom:{m.chat.id}{Dev_Naif}&text={m.text}')
      m.reply(quote=True,text=f'{k} من「 {m.from_user.mention} 」\n{k} ابشر مسحت الأمر\n☆')
      return
   
   
      
      
############ global CustomCommand



@Client.on_message(filters.text, group=1001)
def customCummandGlobalHandler(c,m):
    k = r.get(f'{Dev_Naif}:botkey')
    Thread(target=addcommandg,args=(c,m,k)).start()
   
   
def addcommandg(c,m,k):
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Naif}'):  return 
   if r.get(f'{m.from_user.id}:mute:{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Naif}') and not admin_pls(m.from_user.id,m.chat.id):  return
   text = m.text
   if r.get(f'Custom:{Dev_Naif}&text={m.text}'):
       text = r.get(f'Custom:{Dev_Naif}&text={m.text}')
   
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضف امر عام')
   
   if r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Naif}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت اضف امر عام')

   if text == 'الاوامر العامه' or text == 'الاوامر المضافه العامه' and not m.chat.type == ChatType.PRIVATE:
      if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
      else:
          if not r.smembers(f'listCustom:{Dev_Naif}'):
            return m.reply(quote=True,text=f'{k} مافيه اوامر عامه مضافه')
          else:
              text = 'الاوامر العامه:\n'
              count = 0
              for cmnd in r.smembers(f'listCustom:{Dev_Naif}'):
                 count += 1
                 command = cmnd
                 cc = r.get(f'Custom:{Dev_Naif}&text={command}')
                 old_c = cc
                 text += f'{count}) {command} ~ ( {old_c} )\n'
              text += '\n☆'
              return m.reply(quote=True,text=text)
   
   if text == 'اضف امر عام' or text == 'تغيير امر عام':
     if not r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}'):
       if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}',1)
          m.reply(quote=True,text=f'{k} تمام عيني ، ارسل الامر القديم عشان اغيره')
          return

   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}addCustomG:{m.from_user.id}{Dev_Naif}')
      r.set(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Naif}', m.text)
      m.reply(quote=True,text=f'{k} حلو عشان تغيير امر ( {m.text} )\n{k} ارسل الامر الجديد الحين\n☆')
      return
   
   if r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Naif}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      command_o = r.get(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Naif}')
      command_n = m.text
      r.delete(f'{m.chat.id}:addCustom2G:{m.from_user.id}{Dev_Naif}')
      r.set(f'Custom:{Dev_Naif}&text={command_n}', command_o)
      r.sadd(f'listCustom:{Dev_Naif}', command_n)
      m.reply(quote=True,text=f'{k} غيرت الامر القديم {command_o}\n{k} الى الامر الجديد ( {command_n} )')
      return 


@Client.on_message(filters.text , group=1002)
def delCustomCommandGHandler(c,m):
    k = r.get(f'{Dev_Naif}:botkey')
    Thread(target=delcommandg,args=(c,m,k)).start()
   
   
def delcommandg(c,m,k):
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{Dev_Naif}'):  return 
   if r.get(f'{m.chat.id}:mute:{Dev_Naif}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{Dev_Naif}'):  return 
   text = m.text
   if r.get(f'Custom:{Dev_Naif}&text={m.text}'):
       text = r.get(f'Custom:{Dev_Naif}&text={m.text}')
   
   if r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}')
     return m.reply(quote=True,text=f'{k} من عيوني لغيت مسح امر عام')

   if text == 'مسح الاوامر العامه':
     if not dev_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس') 
     else:
       if not r.smembers(f'listCustom:{Dev_Naif}'):
         return m.reply(quote=True,text=f'{k} مافيه اوامر عامه مضافه')
       else:
         count = 0
         for cmnd in r.smembers(f'listCustom:{Dev_Naif}'):
           command = cmnd
           r.delete(f'Custom:{Dev_Naif}&text={command}')
           r.srem(f'listCustom:{Dev_Naif}', command)
           count += 1
         text = f'من「 {m.from_user.mention} 」\n{k} ابشر مسحت {count} أمر عام\n☆'
         return m.reply(quote=True,text=text)
       
   
   if text == 'مسح امر عام':
     if not r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}'):
       if not dev_pls(m.from_user.id, m.chat.id):
          return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المطور وفوق ) وبس')
       else:
          r.set(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}',1)
          m.reply(quote=True,text=f'{k} ارسل الامر الحين')
          return
   
   if re.match("^فتح امر ",text):
     if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
     else:
       txt=text.split(None,2)[2]
       if not r.hget(Dev_Naif+f"locks-{m.chat.id}", txt):
         return m.reply("الامر مو مقفول من قبل")
       r.hdel(Dev_Naif+f"locks-{m.chat.id}", txt)
       return m.reply("تم فتح الامر بنجاح")
   
   if text == "الاوامر المقفوله":
      if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
      else:
        if not r.hgetall(Dev_Naif+f"locks-{m.chat.id}"):
          return m.reply(f"{k} مافيه اوامر مقفولة")
        else:
          commands = r.hgetall(Dev_Naif+f"locks-{m.chat.id}")
          txt = "الاوامر المقفوله:\n\n"
          count = 1
          for command in commands:
            cc = int(commands[command])
            if cc == 0:
              rank = "مالك اساسي"
            elif cc == 1:
              rank = "مالك وفوق"
            elif cc == 2:
              rank = "مدير و فوق"
            elif cc == 3:
              rank = "ادمن وفوق"
            elif cc == 4:
              rank = "مميز و فوق"
            txt += f"{count} ) {command} - ( {rank} )\n"
            count += 1
          return m.reply(txt, disable_web_page_preview=True)
   
   if text == "مسح الاوامر المقفوله":
      if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
      else:
        if not r.hgetall(Dev_Naif+f"locks-{m.chat.id}"):
          return m.reply(f"{k} مافيه اوامر مقفولة")
        else:
          count = len(list(r.hgetall(Dev_Naif+f"locks-{m.chat.id}").keys()))
          r.delete(Dev_Naif+f"locks-{m.chat.id}")
          return m.reply(f"{k} ابشر مسحت ( {count} )")
   
   if re.match("^قفل امر ",text):
     if not gowner_pls(m.from_user.id, m.chat.id):
       return m.reply(quote=True,text=f'{k} هذا الامر يخص ( المالك الاساسي وفوق ) وبس')
     else:
       txt=text.split(None,2)[2]
       return m.reply(
          f"{k} حسناً عزيزي اختار نوع الرتبه :\n{k} سيتم وضع امر ↤︎( {txt} ) له فقط",
          reply_markup=InlineKeyboardMarkup(
            [
              [
                InlineKeyboardButton (
                   "مالك اساسي",
                   callback_data=f"gowner+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مالك",
                   callback_data=f"owner+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مدير",
                   callback_data=f"mod+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "ادمن",
                   callback_data=f"admin+{m.from_user.id}"
                )
              ],
              [
                InlineKeyboardButton (
                   "مميز",
                   callback_data=f"pre+{m.from_user.id}"
                )
              ]
            ]
          )
       )

   if r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}') and dev_pls(m.from_user.id, m.chat.id) and len(m.text) < 50:
      r.delete(f'{m.chat.id}:delCustomG:{m.from_user.id}{Dev_Naif}')
      if not r.get(f'Custom:{Dev_Naif}&text={m.text}'):
         return m.reply(quote=True,text=f'{k} هذا الأمر مو مضاف')
      r.srem(f'listCustom:{Dev_Naif}', m.text)
      r.delete(f'Custom:{Dev_Naif}&text={m.text}')
      m.reply(quote=True,text=f'{k} من「 {m.from_user.mention} 」\n{k} ابشر مسحت الأمر العام\n☆')
      return
   
   
      