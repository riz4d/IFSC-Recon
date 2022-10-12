from pyrogram import *
import requests as req
from Config import *


app=Client('IFSC-Recon',
           api_id=API_ID,
           api_hash=API_HASH,
           bot_token=BOT_TOKEN)

@app.on_message(filters.command('start'))
async def start_msg(client,message):
    await message.reply('**Hey '+message.from_user.first_name+"  🖐**\n\n__I'm IFSC Recon Bot, I can retrive information from IFSC Code by Just senting here the IFSC Code\n\nDev : @riz4d__")
    
@app.on_message(filters.command('help'))
async def help_msg(client,message):
    await message.reply('__Just sent here the IFSC Code (:__')
     
@app.on_message(filters.command('about'))
async def about_msg(client,message):
    await message.reply('__Developer : @riz4d (:\n\nSource Code : [GitHub Repo](https://github.com/riz4d/IFSC-Recon)__')
  
    
@app.on_message(filters.text)
async def ifsc_data(client,message):
    
   query=message.text.upper()
   try:
    url_request=req.get(url+query)
    url_json=url_request.json()
    
    #datas
    swift='Swift :   `'+str(url_json['SWIFT'])+'`\n'
    city='City :   `'+str(url_json['CITY'])+'`\n'
    upi='UPI :   `'+str(url_json['UPI'])+'`\n'
    iso='ISO3166 :   `'+str(url_json['ISO3166'])+'`\n'
    neft='NEFT :   `'+str(url_json['NEFT'])+'`\n'
    imps='IMPS :   `'+str(url_json['IMPS'])+'`\n'
    rtgs='RTGS :   `'+str(url_json['RTGS'])+'`\n'
    centre='Centre :   `'+str(url_json['CENTRE'])+'`\n'
    address='Address :   `'+str(url_json['ADDRESS'])+'`\n\n'
    branch='Branch :   `'+str(url_json['BRANCH'])+'`\n'
    micr='MICR :   `'+str(url_json['MICR'])+'`\n'
    contact='Contact :   `'+str(url_json['CONTACT'])+'`\n'
    dist='District :   `'+str(url_json['DISTRICT'])+'`\n'
    state='State :   `'+str(url_json['STATE'])+'`\n'
    bank='Bank :   `'+str(url_json['BANK'])+'`\n'
    bankcd='Bank Code :   `'+str(url_json['BANKCODE'])+'`\n'
    ifsc='IFSC :   `'+str(url_json['IFSC'])+'`\n'
    
    result=head+'**__'+bank+bankcd+ifsc+micr+state+dist+city+branch+address+contact+upi+iso+neft+imps+rtgs+swift+'__**'
        
    await message.reply(result)
   except:
       await message.reply("**__Sorry ,`'"+query+"'` is Invalid IFSC Code 😕__**")
       await message.reply("__if you're facing a error or else ping @riz4d 🤝__")
app.run()
