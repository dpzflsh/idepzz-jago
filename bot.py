from telegram.ext import Updater, CommandHandler
import requests

# Fungsi untuk menangani perintah /ban
def ban(update, context):
    # Mendapatkan parameter dari pesan yang diterima
    args = context.args
    if len(args) != 2:
        update.message.reply_text('Format perintah salah. Gunakan /ban {country_code} {number}')
        return
    
    country_code, number = args[0].split('/')
    
    # Mengirim permintaan ke API eksternal
    api_url = f'https://api-bruxiintk.online/api/temp-ban?apikey=keybx&ddi={country_code}&numero={number}'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        update.message.reply_text('Pengguna berhasil diblokir sementara by @WhatsAppBanido')
    else:
        update.message.reply_text('Gagal memblokir pengguna. Mohon coba lagi.')

def main():
    # Inisialisasi bot
    updater = Updater("AAFtoO-ZMNOPT2B4BjAidRDHrj7pifOPVh0", use_context=True)
    dp = updater.dispatcher

    # Menambahkan handler untuk perintah /ban
    dp.add_handler(CommandHandler("ban", ban))

    # Memulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
