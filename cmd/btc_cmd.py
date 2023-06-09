import requests

def btc_cmd(update, context):
    response = requests.get("https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT")
    if response.status_code == 200:
        data = response.json()["data"]
        message = f"📈 BTC Price 📉\n\n"
        message += f"💰 Buy: {data['buy']} USDT\n"
        message += f"💰 Sell: {data['sell']} USDT\n"
        message += f"📈 Change Rate: {data['changeRate']}%\n"
        message += f"📉 Change Price: {data['changePrice']} USDT\n"
        message += f"🔼 High: {data['high']} USDT\n"
        message += f"🔽 Low: {data['low']} USDT\n"
        message += f"📊 Volume: {data['vol']} BTC\n"
        message += f"💵 Volume Value: {data['volValue']} USDT\n"
        message += f"🔄 Last Price: {data['last']} USDT\n"
        message += f"🌟 Average Price: {data['averagePrice']} USDT"

        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Failed to fetch BTC price.")
