# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re

cl = LINETCR.LINE()
cl.login(qr=True)
cl.loginResult()

ki = LINETCR.LINE()
ki.login(qr=True)
ki.loginResult()

kk = LINETCR.LINE()
kk.login(qr=True)
kk.loginResult()

kc = LINETCR.LINE()
kc.login(qr=True) 
kc.loginResult()

kd = LINETCR.LINE()
kd.login(qr=True)
kd.loginResult()

ke = LINETCR.LINE()
ke.login(qr=True)
ke.loginResult()

kf = LINETCR.LINE()
kf.login(qr=True)
kf.loginResult()

kg = LINETCR.LINE()
kg.login(qr=True)
kg.loginResult()

kh = LINETCR.LINE()
kh.login(qr=True)
kh.loginResult()

kj = LINETCR.LINE()
kj.login(qr=True)
kj.loginResult()

kl = LINETCR.LINE()
kl.login(qr=True)
kl.loginResult()

print "BOT Siap"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""         ♻♻♻ By.TON Seft BOT ♻♻♻

➡ Me/Kontak Tiap Bot
➡ Mid/Mid Tiap Bot
➡ Speed Bot
➡ Test/Cek Jumlah Bot
➡ Absen
➡ Baris
➡ Respon
➡ Ban Dengan Tag Nama
➡ Ban Dengan Share Kontak
➡ Ban Satu Grup
➡ Unban Dengan Tag Nama
➡ Unban Dengan Kirim Kontak
➡ Unban Satu Grup
➡ Reject Invite
➡ KillBan
➡ Banlist
➡ Daftar Admin
➡ Invite Dengan Mid
➡ Invite Dengan Kontak
➡ Kick Dengan Mid
➡ Kick Dengan Tag
➡ Block Dengan Tag
➡ Mentionall
➡ Mid Dengan Tag
➡ Cek Sider
➡ Copy Dengan Tag
➡ Broadcast
➡ Info Grup
➡ Copy Profile
➡ Creator Grup
➡ Creator Bot
➡ Daftar Grup
➡ Daftar Bot
➡ Daftar Block
➡ Owner
➡ Spam/Up
➡ Ratakan
➡ K On/Off
➡ Protect QR
➡ Protect Cancel
➡ Protect Invite
➡ Cek Mid Kirim Kontak
➡ Auto Text Join/Leave/Kick
       ⭐⭐TON⭐⭐👈\n\nhttp://line.me/ti/p/K_CcmJ9rX1
"""
KAC=[cl,ki,kk,kc,kd,ke,kf,kg,kh,kj,kl]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
Gmid = kg.getProfile().mid
Hmid = kh.getProfile().mid
Imid = kj.getProfile().mid
Jmid = kl.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]
admin=["u0085b75fb3d15b36647a8a01101fe847"]
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':False,
    'message':"👉Auto Like by ⭐⭐TON⭐⭐👈\n\nhttp://line.me/ti/p/K_CcmJ9rX1 ",
    "lang":"JP",
    "comment":"👉Auto Like by ⭐⭐TON⭐⭐👈\n\nhttp://line.me/ti/p/K_CcmJ9rX1 ",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True,
    "ProtectQR":False,
    "Protectguest":False,
    "Protectcancel":False,
    "atjointicket":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\nã»" + Name
                wait2['ROM'][op.param1][op.param2] = "ã»" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    
        if op.type == 17:
            if op.param2 in Bots:
                return
            ginfo = cl.getGroup(op.param1)
            kk.sendText(op.param1, "Selamat Datang Di Grup " + str(ginfo.name))
            kk.sendText(op.param1, "Pemilik Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
            print "Anggota Masuk"
        if op.type == 15:
            if op.param2 in Bots:
                return
            kk.sendText(op.param1, "Ciee Kakak Gabetah")
            print "Anggota Kel"
        
        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)

                if op.param3 in Cmid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        #-----------------NOTIFED MEMBER KICKOUT GROUP
        if op.type == 1002:
            if op.param2 in Bots:
                return
            kk.sendText(op.param1,cl.getContact(op.param2).displayName + " Hayoo Kakak Ngapain")
            print "Anggota Grup Di Kick"
        #-----------------NOTIFED MEMBER KICKOUT GROUP

        if op.type == 19:
                if not op.param2 in admin and Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return


                    except Exception, e:
                        print e


        if op.type == 11:
                if not op.param2 in admin and Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return


                    except Exception, e:
                        print e       
                                        
        if op.type == 19:
           if op.param3 in admin:
              cl.kickoutFromGroup(op.param1,[op.param2])
              cl.inviteIntoGroup(op.param1,admin)
           else:
               pass
               
        #------FUNGSI KICK USER YANG NGEKICK-------

        if op.type == 700:
            if op.param2 not in admin:
                 kk.kickoutFromGroup(op.param1,[op.param2])
                 wait["blacklist"][op.param2] = True
                 print "Member Dimusnahkan"
            else:
                pass

        #-------FUNGSI KICK USER SELESAI------

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the groupã\n["+op.param1+"]\nã®\n["+op.param2+"]\nãè¹´ãäºãã§ãã¾ããã§ããã\nãã©ãã¯ãªã¹ãã«è¿½å ãã¾ãã")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãè¹´ãè¦å¶orã°ã«ã¼ãã«å­å¨ããªãçºã\n["+op.param1+"]\nã®\n["+op.param2+"]\nãè¹´ãäºãã§ãã¾ããã§ããã\nãã©ãã¯ãªã¹ãã«è¿½å ãã¾ãã")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    kf.acceptGroupInvitationByTicket(op.param1,Ti)
                    kg.acceptGroupInvitationByTicket(op.param1,Ti)
                    kh.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãè¹´ãè¦å¶orã°ã«ã¼ãã«å­å¨ããªãçºã\n["+op.param1+"]\nã®\n["+op.param2+"]\nãè¹´ãäºãã§ãã¾ããã§ããã\nãã©ãã¯ãªã¹ãã«è¿½å ãã¾ãã")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientãè¹´ãè¦å¶orã°ã«ã¼ãã«å­å¨ããªãçºã\n["+op.param1+"]\nã®\n["+op.param2+"]\nãè¹´ãäºãã§ãã¾ããã§ããã\nãã©ãã¯ãªã¹ãã«è¿½å ãã¾ãã")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                  if msg.from_ in admin:  
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == profile.mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
                
       
        
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"Sudah Ada")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
               elif "เอาโปรไฟล์" in msg.text:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("เอาไฟล์ ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Gak da orange")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Berhasil Dihapus")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak Ada Dalam Daftar Blacklist")
               elif wait["wblacklist"] == True:
                 if msg.from_ in admin: 
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Sudah Ada")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Berhasil Ditambahkan")

               elif wait["dblacklist"] == True:
                 if msg.from_ in admin: 
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Berhasil Dihapus")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Tidak Ada Dalam Da ftar Blacklist")
               elif wait["contact"] == True:
                 if msg.from_ in admin: 
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLÃ¢â â\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key"]:
              if msg.from_ in admin:   
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif "เอาปก @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("เอาปก @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass    
            #-----------------------------------------------
            elif ".Youtube " in msg.text:
                 query = msg.text.replace(".Youtube ","")
                 with requests.session() as s:
                     s.headers['user-agent'] = 'Mozilla/5.0'
                     url    = 'http://www.youtube.com/results'
                     params = {'search_query': query}
                     r    = s.get(url, params=params)
                     soup = BeautifulSoup(r.content, 'html5lib')
                     for a in soup.select('.yt-lockup-title > a[title]'):
                         if '&List' not in a['href']:
                               cl.sendText(msg.to,'http://www.youtube.com' + a['href'] + a['title'])
#-----------------------------------------------
            elif ("Bye " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass                        
                    
            elif ("Gn " in msg.text):
              if msg.from_ in admin:  
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Angel Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Angel Gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Shani Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Shani Gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Yona Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Yona Gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:  
                midd = msg.text.replace("Kick ","")
                cl.kickoutFromGroup(msg.to,[midd])
            elif "Angel Kick " in msg.text:
                midd = msg.text.replace("Angel Kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Shani Kick " in msg.text:
                midd = msg.text.replace("Shani Kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Yona Kick " in msg.text:
                midd = msg.text.replace("Yona Kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin: 
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Angel Invite " in msg.text:
                midd = msg.text.replace("Angel Invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Shani Invite " in msg.text:
                midd = msg.text.replace("Shani Invite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Yona Invite " in msg.text:
                midd = msg.text.replace("Yona Invite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["Me"]:
              if msg.from_ in admin: 
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            elif msg.text in ["Angel."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)
            elif msg.text in ["Shani."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["Yona."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
            elif msg.text in ["Aya."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kd.sendMessage(msg)
            elif msg.text in ["Devi."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ke.sendMessage(msg)
            elif msg.text in ["Celine."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kf.sendMessage(msg)
            elif msg.text in ["Cinhap."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                kg.sendMessage(msg)
            elif msg.text in ["Jinan."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                kh.sendMessage(msg)
            elif msg.text in ["Yupi."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                kj.sendMessage(msg)
            elif msg.text in ["Kyla."]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Jmid}
                kl.sendMessage(msg)
            elif msg.text in ["Ã¦ââºÃ£ÂÂ®Ã£ÆâÃ£ÆÂ¬Ã£âÂ¼Ã£ÆÂ³Ã£ÆË","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Ã¦ââºÃ£ÂÂ®Ã£ÆâÃ£ÆÂ¬Ã£âÂ¼Ã£ÆÂ³Ã£ÆË","Cv1 gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Ã¦ââºÃ£ÂÂ®Ã£ÆâÃ£ÆÂ¬Ã£âÂ¼Ã£ÆÂ³Ã£ÆË","Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["Ã¦ââºÃ£ÂÂ®Ã£ÆâÃ£ÆÂ¬Ã£âÂ¼Ã£ÆÂ³Ã£ÆË","Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["Ã¦ââºÃ£ÂÂ®Ã£ÆâÃ£ÆÂ¬Ã£âÂ¼Ã£ÆÂ³Ã£ÆË","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel"]:
              if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Tidak Ada Yang Diundang")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot Cancel"]:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"Tidak Ada Yang Diundang")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
                        
        #---------------Fungsi Gcreator Start---------------#
            elif msg.text in ["Gcreator"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                      msg.contentType = 13
                      ginfo = cl.getGroup(msg.to)
                      gCreator = ginfo.creator.mid
                      try:
                          msg.contentMetadata = {'mid': gCreator}
                          gCreator1 = ginfo.creator.displayName
                        
                      except:
                        gCreator = "Error"
                      cl.sendText(msg.to, "Group Creator : " + gCreator1)
                      cl.sendMessage(msg)
        

     

#----------------------------------------------------------------------------


                if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 k3.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Maaf, " + _name + " Ada Dalam Daftar Blacklist")
                                 k4.sendText(msg.to,"Panggil Admin Untuk Menggunakan Key Ini \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     k3.findAndAddContactsByMid(target)
                                     k3.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Berhasil Mengundang: \n➡" + _name)
                                     wait["winvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Negative, Err0r Detected")
                                          wait["winvite"] = False
                                          break


            elif msg.text in ["Invite"]:
            	  if msg.from_ in admin:
                   wait["riconvite"] = True
                   cl.sendText(msg.to,"Kirim Kontak")

            elif "Spam Contact @" in msg.text:
                _name = msg.text.replace("Spam Contact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Cie Kena")
                       kk.sendText(g.mid,"Cie Kena")  
                       ki.sendText(g.mid,"Cie Kena")  
                       kc.sendText(g.mid,"Cie Kena")
                       kd.sendText(g.mid,"Cie Kena")
                       ke.sendText(g.mid,"Cie Kena")
                       kf.sendText(g.mid,"Cie Kena")
                       kg.sendText(g.mid,"Cie Kena")
                       kh.sendText(g.mid,"Cie Kena")
                       kj.sendText(g.mid,"Cie Kena")
                       kl.sendText(g.mid,"Cie Kena")
                       cl.sendText(msg.to, "Berhasil Spam Kontak")
                       print "Berhasil Spam Kontak"

            elif "Contact Bc " in msg.text:
              if msg.from_ in admin:
                  bctxt = msg.text.replace("Contact Bc ", "")
                  t = cl.getAllContactIds()
                  t = 100
                  while(t):
                    cl.sendText(msg.to, (bctxt))
                    t-=1
                    
            elif msg.text in ["Mad On"]:
              if msg.from_ in admin:
                 if wait["Protectcancel"] == True:
                     if wait["lang"] == "JP":
                         cl.sendText(msg.to,"Protect Cancel Nyala")
                     else:
                         cl.sendText(msg.to,"done")
                 else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Nyala")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Mad Off","mad off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Mati")
                    else:
                        cl.sendText(msg.to,"done")

            elif "Copy @" in msg.text:
            	if msg.from_ in admin:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Tidak Ditemukan")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Berhasil Copy Profil")
                            except Exception as e:
                                print e
            elif msg.text in ["Backup"]:
              if msg.from_ in admin:
                    try:
                       cl.updateDisplayPicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Berhasil Backup")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))

            elif msg.text in ["Reject Invite"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Semua Undangan Grup Dibatalkan")
                    else:
                        cl.sendText(msg.to,"Done")

            elif "Ban All" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Ban]ok"
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Berhasil Menambahkan")
                            except:
                                cl.sendText(msg.to,"Gagal")
            elif "Unban All" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban]ok"
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found ~")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Berhasil Menghapus")
                            except:
                                cl.sendText(msg.to,"Berhasil Menghapus")

            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Ourl"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Terbuka")
                    else:
                        cl.sendText(msg.to,"Masih Terbuka")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Angel Ourl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Sudah Terbuka")
                    else:
                        ki.sendText(msg.to,"Masih Terbuka")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Shani Ourl"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Sudah Terbuka")
                    else:
                        kk.sendText(msg.to,"Masih Terbuka")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yona Ourl"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Sudah Terbuka")
                    else:
                        kc.sendText(msg.to,"Masih Terbuka")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Curl"]:
              if msg.from_ in admin: 
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah Tertutup")
                    else:
                        cl.sendText(msg.to,"Masih Tertutup")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Angel Curl"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Sudah Tertutup")
                    else:
                        ki.sendText(msg.to,"Masih Tertutup")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Shani Curl"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Sudah Tertutup")
                    else:
                        kk.sendText(msg.to,"Masih Tertutup")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yona Curl"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Sudah Tertutup")
                    else:
                        kc.sendText(msg.to,"Masih Tertutup")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
              if msg.from_ in admin: 
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,msg.to)
            elif "All Mid" == msg.text:
              if msg.from_ in admin: 
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                kd.sendText(msg.to,Dmid)
                ke.sendText(msg.to,Emid)
                kf.sendText(msg.to,Fmid)
                kg.sendText(msg.to,Gmid)
                kh.sendText(msg.to,Hmid)
                kj.sendText(msg.to,Imid)
                kl.sendText(msg.to,Jmid)
            elif "My Mid" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
            elif "Angel Mid" == msg.text:
                ki.sendText(msg.to,Amid)
            elif "Shani Mid" == msg.text:
                kk.sendText(msg.to,Bmid)
            elif "Yona Mid" == msg.text:
                kc.sendText(msg.to,Cmid)
            elif "Aya Mid" == msg.text:
                kd.sendText(msg.to,Dmid)
            elif "Devi Mid" == msg.text:
                ke.sendText(msg.to,Emid)
            elif "Celine Mid" == msg.text:
                kf.sendText(msg.to,Fmid)
            elif "Cinhap Mid" == msg.text:
                kg.sendText(msg.to,Gmid)
            elif "Jinan Mid" == msg.text:
                kh.sendText(msg.to,Hmid)
            elif "Yupi Mid" == msg.text:
                kj.sendText(msg.to,Imid)
            elif "Kyla Mid" == msg.text:
                kl.sendText(msg.to,Jmid)
            elif msg.text in ["Wkwk"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galon"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
              if msg.from_ in admin:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Angel Rename "]:
                string = msg.text.replace("Angel Rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Shani Rename "]:
                string = msg.text.replace("Shani Rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin: 
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Guest On"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Nyala")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Nyala")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Guest Off"]:
              if msg.from_ in admin:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Guest Stranger Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Lock QR Nyala")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Lock QR Nyala")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off"]:
              if msg.from_ in admin:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Lock QR Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Lock QR Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Cek Kontak Nyala")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Cek Kontak Nyala")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Cek Kontak Mati")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Cek Kontak Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Ã©â¬Â£Ã§ÂµÂ¡Ã¥â¦Ë:Ã£âÂªÃ£ÆÂ³","K on","Contact on","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©ââ¹"]:
              if msg.from_ in admin: 
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Masih Menyala")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Masih Menyala")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Ã©â¬Â£Ã§ÂµÂ¡Ã¥â¦Ë:Ã£âÂªÃ£Æâ¢","K off","Contact off","Ã©Â¡Â¯Ã§Â¤ÂºÃ¯Â¼Å¡Ã©âÅ"]:
              if msg.from_ in admin: 
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Masih Mati")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Masih Mati")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Ã¨â¡ÂªÃ¥â¹â¢Ã¥ÂâÃ¥Å  :Ã£âÂªÃ£ÆÂ³","Join on","Auto join:on","Ã¨â¡ÂªÃ¥â¹â¢Ã¥ÂÆÃ¥Å  Ã¯Â¼Å¡Ã©ââ¹"]:
              if msg.from_ in admin: 
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Masih Menyala")
                    else:
                        cl.sendText(msg.to,"Auto Join Nyala")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Masih Menyala")
                    else:
                        cl.sendText(msg.to,"Auto Join Nyala")
            elif msg.text in ["Ã¨â¡ÂªÃ¥â¹â¢Ã¥ÂâÃ¥Å  :Ã£âÂªÃ£Æâ¢","Join off","Auto join:off","Ã¨â¡ÂªÃ¥â¹â¢Ã¥ÂÆÃ¥Å  Ã¯Â¼Å¡Ã©âÅ"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Masih Mati")
                    else:
                        cl.sendText(msg.to,"Auto Join Mati")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Masih Mati")
                    else:
                        cl.sendText(msg.to,"Auto Join Mati")
            elif msg.text in ["Gcancel:"]:
              if msg.from_ in admin:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"Ã¥â¦Â³Ã¤Âºâ Ã©ââ¬Ã¨Â¯Â·Ã¦â¹âÃ§Â»ÂÃ£â¬âÃ¨Â¦ÂÃ¦âÂ¶Ã¥Â¼â¬Ã¨Â¯Â·Ã¦Åâ¡Ã¥Â®Å¡Ã¤ÂºÂºÃ¦â¢Â°Ã¥ÂâÃ©â¬Â")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "Ã¤Â½Â¿Ã¤ÂºÂºÃ¤Â»Â¥Ã¤Â¸â¹Ã§Å¡âÃ¥Â°ÂÃ§Â»âÃ§âÂ¨Ã¨â¡ÂªÃ¥Å Â¨Ã©ââ¬Ã¨Â¯Â·Ã¦â¹âÃ§Â»Â")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["Ã¥Â¼Â·Ã¥ËÂ¶Ã¨â¡ÂªÃ¥â¹â¢Ã©â¬â¬Ã¥â¡Âº:Ã£âÂªÃ£ÆÂ³","Leave on","Auto leave:on","Ã¥Â¼Â·Ã¥ËÂ¶Ã¨â¡ÂªÃ¥â¹â¢Ã©â¬â¬Ã¥â¡ÂºÃ¯Â¼Å¡Ã©ââ¹"]:
              if msg.from_ in admin: 
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Masih Menyala")
                    else:
                        cl.sendText(msg.to,"Auto Leave Nyala")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Leave Nyala")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ Ã¥Â¼â¬Ã£â¬â")
            elif msg.text in ["Ã¥Â¼Â·Ã¥ËÂ¶Ã¨â¡ÂªÃ¥â¹â¢Ã©â¬â¬Ã¥â¡Âº:Ã£âÂªÃ£Æâ¢","Leave off","Auto leave:off","Ã¥Â¼Â·Ã¥ËÂ¶Ã¨â¡ÂªÃ¥â¹â¢Ã©â¬â¬Ã¥â¡ÂºÃ¯Â¼Å¡Ã©âÅ"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Leave Masih Mati")
                    else:
                        cl.sendText(msg.to,"Mode Leave Mati")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["Ã¥â¦Â±Ã¦Åâ°:Ã£âÂªÃ£ÆÂ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Share Masih Menyala")
                    else:
                        cl.sendText(msg.to,"Mode Share Menyala")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ Ã¥Â¼â¬Ã£â¬â")
            elif msg.text in ["Ã¥â¦Â±Ã¦Åâ°:Ã£âÂªÃ£Æâ¢","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Share Masih Mati")
                    else:
                        cl.sendText(msg.to,"Mode Share Mati")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ Ã¥â¦Â³Ã¦âÂ­Ã£â¬â")
            elif msg.text in ["Set"]:
              if msg.from_ in admin:
                md = ""
                if wait["Protectcancel"] == True: md+=" Protect Cancel : on\n"
                else: md+=" Protect Cancel : off\n"
                if wait["ProtectQR"] == True: md+=" Protect Qr      : on\n"
                else: md+=" Protect Qr   : off\n"
                if wait["Protectguest"] == True: md+=" Block Invite : on\n"
                else: md+=" Block Invite : off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"Ã§âºÂ¸Ã¥â ÅÃ¦Â²Â¡Ã¥ÅÂ¨Ã£â¬â")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "Ã¤Â»Â¥Ã¤Â¸â¹Ã¦ËÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡âÃ§âºÂ¸Ã¥â Å"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"Ã§âºÂ¸Ã¥â ÅÃ¦Â²Â¡Ã¥ÅÂ¨Ã£â¬â")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "Ã¤Â»Â¥Ã¤Â¸â¹Ã¦ËÂ¯Ã¥Â¯Â¹Ã¨Â±Â¡Ã§Å¡âÃ§âºÂ¸Ã¥â Å"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "Ã¥Ë Ã©â¢Â¤Ã¤Âºâ Ã¤Âºâ¹Ã§Å¡âÃ§âºÂ¸Ã¥â ÅÃ£â¬â")
            elif msg.text in ["Group id","Ã§Â¾Â¤Ã§ÂµâÃ¥â¦Â¨id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"Ã¦â¹âÃ§Â»ÂÃ¤Âºâ Ã¥â¦Â¨Ã©ÆÂ¨Ã§Å¡âÃ©ââ¬Ã¨Â¯Â·Ã£â¬â")
            elif "album removeÃ¢â â" in msg.text:
                gid = msg.text.replace("album removeÃ¢â â","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "Ã¥Ë Ã©â¢Â¤Ã¤Âºâ Ã¤Âºâ¹Ã§Å¡âÃ§âºÂ¸Ã¥â ÅÃ£â¬â")
            elif msg.text in ["Ã¨â¡ÂªÃ¥â¹â¢Ã¨Â¿Â½Ã¥Å  :Ã£âÂªÃ£ÆÂ³","Add on","Auto add:on","Ã¨â¡ÂªÃ¥â¹â¢Ã¨Â¿Â½Ã¥Å  Ã¯Â¼Å¡Ã©ââ¹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Masih Menyala")
                    else:
                        cl.sendText(msg.to,"Mode Auto Add Nyala")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Auto Add Nyala")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ Ã¥Â¼â¬Ã£â¬â")
            elif msg.text in ["Ã¨â¡ÂªÃ¥â¹â¢Ã¨Â¿Â½Ã¥Å  :Ã£âÂªÃ£Æâ¢","Add off","Auto add:off","Ã¨â¡ÂªÃ¥â¹â¢Ã¨Â¿Â½Ã¥Å  Ã¯Â¼Å¡Ã©âÅ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Masih Mati")
                    else:
                        cl.sendText(msg.to,"Mode Auto Add Mati")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mode Auto Add Mati")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ Ã¥â¦Â³Ã¦âÂ­Ã£â¬â")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"Pesan Terganti")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan Terganti")
                else:
                    cl.sendText(msg.to,"doneÃ£â¬â")
            elif msg.text in ["Message","Ã¨â¡ÂªÃ¥â¹â¢Ã¨Â¿Â½Ã¥Å  Ã¥â¢ÂÃ¥â¬â¢Ã¨ÂªÅ¾Ã§Â¢ÂºÃ¨ÂªÂ"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsÃ£â¬â\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Pesan Terganti")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["Ã£âÂ³Ã£ÆÂ¡Ã£ÆÂ³Ã£ÆË:Ã£âÂªÃ£ÆÂ³","Comment on","Comment:on","Ã¨â¡ÂªÃ¥â¹â¢Ã©Â¦âÃ© ÂÃ§â¢â¢Ã¨Â¨â¬Ã¯Â¼Å¡Ã©ââ¹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Nyala")
                    else:
                        cl.sendText(msg.to,"Masih Menyala")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ Ã¥Â¼â¬Ã£â¬â")
            elif msg.text in ["Ã£âÂ³Ã£ÆÂ¡Ã£ÆÂ³Ã£ÆË:Ã£âÂªÃ£Æâ¢","Comment on","Comment off","Ã¨â¡ÂªÃ¥â¹â¢Ã©Â¦âÃ© ÂÃ§â¢â¢Ã¨Â¨â¬Ã¯Â¼Å¡Ã©âÅ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment Mati")
                    else:
                        cl.sendText(msg.to,"Masih Mati")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"Ã¨Â¦ÂÃ¤Âºâ Ã¥â¦Â³Ã¦âÂ­Ã£â¬â")
            elif msg.text in ["Comment","Ã§â¢â¢Ã¨Â¨â¬Ã§Â¢ÂºÃ¨ÂªÂ"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Angel Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Shani Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yona Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)                                    
            elif msg.text in ["qqqqqq"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            elif msg.text in ["qqq"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Masih Mati")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            elif msg.text in ["qqq"]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["qqq"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Dimohon Menyalakan Jam Dahulu")
                    
            elif msg.text == "Cek":
                    cl.sendText(msg.to, "Mengecek Sider")
                    try:
                      del wait2['readPoint'][msg.to]
                      del wait2['readMember'][msg.to]
                    except:
							          pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Cyduk":
						        if msg.to in wait2['readPoint']:
							          if wait2["ROM"][msg.to].items() == []:
								            chiya = ""
							          else:
								            chiya = ""
								            for rom in wait2["ROM"][msg.to].items():
									              print rom
									              chiya += rom[1] + "\n"

							          cl.sendText(msg.to, "Semua Yang Membaca%s\nHanya Itu\n\nYang Mengabaikan\n%sHayoo Ngapain Diabaikan\n\nWaktu Pengecekan:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
						        else:
							          cl.sendText(msg.to, "Cek Untuk Melihat Sider")
                                          
#-----------------------------------------------
	
            elif "Admin add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"Admin Ditambahkan")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Perintah Ditolak")
                    cl.sendText(msg.to,"Butuh Izin Admin")

            elif "Admin remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Admin remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Admin Dihapus")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Perintah Ditolak")
                    cl.sendText(msg.to,"Butuh Izin Admin")

            elif msg.text in ["Daftar Admin"]:
                if admin == []:
                    cl.sendText(msg.to,"Daftar Admin Kosong")
                else:
                    cl.sendText(msg.to,"Tunggu")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Staff Dieksekusi"

            elif msg.text in ["Daftar Grup"]:
              if msg.from_ in admin:
            					gid = cl.getGroupIdsJoined()
            					h = ""
            					for i in gid:
            						h += "[➡] %s  \n" % (cl.getGroup(i).name + " | " + msg.to + " : " + str(len (cl.getGroup(i).members)))
            					cl.sendText(msg.to, "⚠「Daftar Grup」⚠\n"+ h +"Total Group : " +str(len(gid)))
                
            elif ("Cn " in msg.text):
              if msg.toType == 2:
                profile = cl.getProfile()
                X = msg.text.replace("Cn ","")
                profile.displayName = X
                cl.updateProfile(profile)
                cl.sendText(msg.to,"Nama " + X + " Berhasil Diubah")
              else:
                cl.sendText(msg.to,"Gagal Mengubah Nama")
                
            elif "Add @" in msg.text:
                if msg.from_ in owner:
                    print "Menambah Anggota Bot"
                    _name = msg.text.replace("Leo Add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                Bots.append(target)
                                cl.sendText(msg.to,"Berhasil Menambahkan")
                            except:
                                pass
                    print "Bot Ditambahkan"
                else:
                    cl.sendText(msg.to,"Gagal")
                    cl.sendText(msg.to,"Butuh Izin Dari Pemilik")

            elif "Remove @" in msg.text:
                if msg.from_ in admin:
                    print "Staff Bot Dieksekusi"
                    _name = msg.text.replace("Leo Remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Kontak Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                Bots.remove(target)
                                cl.sendText(msg.to,"Berhasil Menghapus Dari Daftar")
                            except:
                                pass
                    print "Bot Dihapus"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Owner permission required.")
            elif msg.text in ["Daftar Bot"]:
              if msg.from_ in admin:
                if Bots == []:
                    cl.sendText(msg.to,"Daftar Bot Kosong")
                else:
                    cl.sendText(msg.to,"Tunggu")
                    mc = ""
                    for mi_d in Bots:
                        mc += "➳" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,"「Leo BOT」\n" + mc +"Total : "+ str(len(Bots)))
                    print "[Command]Whitelist executed"                
                
            elif ("Ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Berhasil Ditambahkan")
                   except:
                      pass
                      

            elif "Block @" in msg.text:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("Block @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.blockContact(target)
                               cl.sendMessage(msg.to, "Success block contact~")
                            except Exception as e:
                               print e
                

            elif msg.text.lower() == 'Daftar Blok':
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Tunggu")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="Daftar Akun Diblokir\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i Blocked User(s)" % len(kontak)
                cl.sendText(msg.to, msgs)                                
                
            elif msg.text in ["งง"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.1)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print "Sudah Masuk Semua"
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)

            elif msg.text in ["Angel Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Devi Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ke.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

            elif msg.text in ["Celine Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kf.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Kyla Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Shani Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Jinan Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kh.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Yupi Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kj.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Cinhap Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kg.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Aya Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kd.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Yona Masuk"]:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = kk.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(msg.to)

#-----------------------------------------------
	
            elif msg.text in ["เชค"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kf.leaveGroup(msg.to)
                        kg.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
                        kj.leaveGroup(msg.to)
                        kl.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kd.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ke.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kf.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kg.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kh.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kj.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["มาครับ"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kl.leaveGroup(msg.to)
                    except:
                        pass
#-----------------------------------------------
            elif msg.text in ["Tagall"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(5)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(6)
                    akh = akh + 1
                    cb2 += "@nrik\n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print error
                    
            elif "K1 upstatus: " in msg.text:
                string = msg.text.replace("K1 upstatus: ","")
                if len(string.decode('utf-8')) <= 500:
                    profile_B = ki.getProfile()
                    profile_B.statusMessage = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"display message " + string + " done")
            
            elif msg.text in ["Kill"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Mantap Kak")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Ratakan" in msg.text:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Ratakan","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    ki.sendText(msg.to,"Waduh")
                    kk.sendText(msg.to,"Grup Kalian Kami Bersihkan Ya Kak")
                    kc.sendText(msg.to,"Maaf Ya Kak")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                klist=[ki,kk,kc]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg.to,"Grup Dibersihkan")
                                kk.sendText(msg.to,"Membersihkan Cache")
                                kc.sendText(msg.to,"Sudah Siap Kembali")
            elif "Nk " in msg.text:
              if msg.from_ in admin:          
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"Pengguna Tidak Diketahui")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[cl]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    cl.sendText(msg.to,"Mantap Yekan")
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin: 
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = ki2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Tidak Ditemukan")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    k3.sendText(msg.to,"Berhasil")
                                except:
                                    ki.sendText(msg.to,"Gagal")
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Ban]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found Cv")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Berhasil Ditambahkan")
                            except:
                                cl.sendText(msg.to,"Gagal")
            elif "Unban @" in msg.text:
              if msg.from_ in admin:   
                if msg.toType == 2:
                    print "[Unban]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Berhasil Dihapus")
                            except:
                                cl.sendText(msg.to,"Berhasil Dihapus")
#-----------------------------------------------
            elif msg.text in ["kam"]:
              if msg.from_ in admin:
                ginfo = cl.getGroup(msg.to)
                cl.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                cl.sendText(msg.to,"Pemilik Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )      

            elif msg.text in ["Creator"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u0085b75fb3d15b36647a8a01101fe847'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Powered By TON")         
#-----------------------------------------------
            elif "Bc " in msg.text:
              if msg.from_ in admin:
				bctxt = msg.text.replace("Bc ","")
				kk.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				kd.sendText(msg.to,(bctxt))
				ke.sendText(msg.to,(bctxt))
				kf.sendText(msg.to,(bctxt))
				kg.sendText(msg.to,(bctxt))
				kh.sendText(msg.to,(bctxt))
				kj.sendText(msg.to,(bctxt))
				kl.sendText(msg.to,(bctxt))
#-----------------------------------------------
            elif msg.text in ["Test"]:
              if msg.from_ in admin:
                kk.sendText(msg.to,"มาครับ")
                ki.sendText(msg.to,"มาครับ")
                kd.sendText(msg.to,"มาครับ")
                ke.sendText(msg.to,"มาครับ")
                kf.sendText(msg.to,"มาครับ")
                kg.sendText(msg.to,"มาครับ")
                kh.sendText(msg.to,"มาครับ")
                kj.sendText(msg.to,"มาครับ")
                kl.sendText(msg.to,"มาครับ")
                kc.sendText(msg.to,"มาครับ")
                
            elif msg.text in ["นับ"]:
              if msg.from_ in admin:
                kk.sendText(msg.to,"1")
                ki.sendText(msg.to,"2")
                kd.sendText(msg.to,"3")
                ke.sendText(msg.to,"4")
                kf.sendText(msg.to,"5")
                kg.sendText(msg.to,"6")
                kh.sendText(msg.to,"7")
                kj.sendText(msg.to,"8")
                kl.sendText(msg.to,"9")
                kc.sendText(msg.to,"10")
#-----------------------------------------------	
            elif msg.text in ["Shani"]:
              if msg.from_ in admin: 
                kk.sendText(msg.to,"Apa Say?")
            elif msg.text in ["Angel"]:
              if msg.from_ in admin: 
                ki.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Yona"]:
              if msg.from_ in admin: 
                kc.sendText(msg.to,"Apa Say?")
            elif msg.text in ["Aya"]:
              if msg.from_ in admin: 
                kd.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Devi"]:
              if msg.from_ in admin: 
                ke.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Celine"]:
              if msg.from_ in admin: 
                kf.sendText(msg.to,"Iya Kak?")
            elif msg.text in ["Cinhap"]:
              if msg.from_ in admin: 
                kg.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Jinan"]:
              if msg.from_ in admin: 
                kh.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Yupi"]:
              if msg.from_ in admin: 
                kj.sendText(msg.to,"Apa Kak?")
            elif msg.text in ["Kyla"]:
              if msg.from_ in admin: 
                kl.sendText(msg.to,"Apa Kak?")
                                   
#-----------------------------------------------	
            elif msg.text in ["Owner"]:
              if msg.from_ in admin: 
                cl.sendText(msg.to,"BOT By ⭐⭐TON⭐⭐👈http://line.me/ti/p/K_CcmJ9rX1")
                cl.sendText(msg.to,"BOT By ⭐⭐TON⭐⭐👈http://line.me/ti/p/K_CcmJ9rX1")                
#-----------------------------------------------	
            elif msg.text in ["Absen"]:
              if msg.from_ in admin: 
                kk.sendText(msg.to,"Shani")
                ki.sendText(msg.to,"Angel")
                kc.sendText(msg.to,"Yona")
                kd.sendText(msg.to,"Aya")
                ke.sendText(msg.to,"Devi")
                kf.sendText(msg.to,"Celine")
                kg.sendText(msg.to,"Cinhap")
                kh.sendText(msg.to,"Jinan")
                kj.sendText(msg.to,"Yupi")
                kl.sendText(msg.to,"Kyla")

            elif msg.text in ["Up"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kc.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kd.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ke.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kf.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kg.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kh.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kj.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
#-----------------------------------------------
            elif msg.text in ["Sp"]:
              if msg.from_ in admin: 
                start = time.time()
                cl.sendText(msg.to, "Tunggu")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s Detik" % (elapsed_time))
#------------------------------------------------------------------
            elif msg.text in ["Ban"]:
              if msg.from_ in admin: 
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Unban"]:
              if msg.from_ in admin: 
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim Kontak")
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:  
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada")
                else:
                    cl.sendText(msg.to,"Daftar Blacklist")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["CekBan"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["KillBan"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak Ada Blacklist")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Berhasil Dikeluarkan")
            elif msg.text in ["Clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random:" in msg.text:
              if msg.from_ in admin: 
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Tidak Berhasil")
            elif "albumÃ¢â â" in msg.text:
                try:
                    albumtags = msg.text.replace("albumÃ¢â â","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Tidak Berhasil")
            elif "fakecÃ¢â â" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecÃ¢â â","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
                        
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n." + Name
                        wait2['ROM'][op.param1][op.param2] = "." + Name
                else:
                    cl.sendText
            except:
                  pass                        
                        
        if op.type == 59:
            print op


    except Exception as error:
        print error
 
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
